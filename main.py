import argparse
import re
import os
import sys

import os
import requests
import base64


class FirstDispatcher():

    def __init__(self, args):
        self.base_folder_url = "{}/alfresco/api/-default-/public/cmis/versions/1.1/browser/root/{}"
        self.headers = self.setHeader(args.username, args.password)
        self.output = open(args.output, 'w')
        self.args = args
        self.dispatch(args)

    def setHeader(self, username, password):
        data = "{}:{}".format(username, password)
        encoded = str(base64.b64encode(data.encode("utf-8")), "utf-8")
        return {
            'Content-Type': "application/json",
            'Authorization': "Basic {}".format(encoded),
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
        }

    def get_root_node_children(self, url):
        responses = requests.request("GET", url, headers=self.headers)
        if responses.status_code == 200:
            return responses.json()
        return None

    def node_hierachy(self, al_folders):
        nodes = []
        for item in al_folders["objects"]:
            node = None
            path = None
            object_id = None
            title = None
            for it in item["object"]["properties"]:
                if it == "cmis:name":
                    node = item["object"]["properties"][it]['value']
                if it == "cmis:path":
                    path = item["object"]["properties"][it]['value']
                if it == "cmis:objectId":
                    object_id = item["object"]["properties"][it]['value']
                if it == "cm:title":
                    title = item["object"]["properties"][it]['value']
            nodes.append({"name": node, "path": path,
                          "object_id": object_id,
                          "service": path.split("/")[-1],
                          "is_folder": True,
                          "title": title})
        return nodes

    def recursive_folder_loader(self, path, h, autoload):
        # Build URL
        base_url = None
        if autoload:
            base_url = path
        else:
            base_url = self.build_url(path)

        response = self.get_root_node_children(base_url)
        if response is not None:
            nodes = self.isFolders(response, base_url, h)
            if nodes:
                for node in nodes:
                    if node['is_folder']:
                        self.recursive_folder_loader(
                            node['path'], node['path'], True)

    def isFolders(self, folders, base_url, ph):
        nodes = []
        for item in folders["objects"]:
            isFolder = False
            node = None
            path = None
            object_id = None
            title = None
            for it in item["object"]["properties"]:
                if it == "cmis:objectTypeId":
                    if item["object"]["properties"][it]['value'] == "cmis:folder":
                        isFolder = True
                if it == "cmis:name":
                    node = item["object"]["properties"][it]['value']
                if it == "cmis:path":
                    path = item["object"]["properties"][it]['value']
                if it == "cmis:objectId":
                    object_id = item["object"]["properties"][it]['value']
                if it == "cm:title":
                    title = item["object"]["properties"][it]['value']
            output = ""
            if isFolder:
                nodes.append({"path": base_url + "/" +
                              node, "is_folder": isFolder})
                base_ = path.split("/")[2]

                path = base_ + "/" + node
                output = node + ";" + path + ";" + object_id + ";" + title + ";is_folder"

            else:
                path = base_url + "/" + node
                output = node + ";" + path + ";" + object_id + ";is_file"
            self.output.write(output + "\r\n")

        return nodes

    def dispatch(self, args):
        path = '{}/{}'.format(args.root_folder, args.servicename)
        url = self.build_url(path)
        nodes = self.node_hierachy(self.get_root_node_children(url))
        for node in nodes:
            self.recursive_folder_loader(node["path"], node["name"], False)
        self.output.close()

    def build_url(self, path):
        return self.base_folder_url.format(self.args.hostname, path)


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-sn', '--servicename',
                        help='Service name', required=True)
    parser.add_argument('-hn', '--hostname',
                        help='Alfresco host url or hostname')
    parser.add_argument('-rf', '--root_folder', help='Alfresco base folder')
    parser.add_argument('-bsf', '--base_storage_folder',
                        help='Storage path for local system')
    parser.add_argument('-u', '--username', help='Alfresco auth username')
    parser.add_argument('-p', '--password', help='Alfresco auth password')
    parser.add_argument('-o', '--output', help='Output file', required=True)
    parser.add_argument(
        '--verbose', help='Show command output', action='store_true')
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    FirstDispatcher(arg_parser())
