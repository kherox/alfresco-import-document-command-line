# alfresco-import-document-command-line

compatibility : python3.5 + <br>

Dependencies : <br>
pip install requests <br>

<p>This <strong>app</strong> help alfresco developper to export all folder structure .</p>

usage: python main.py [-h] -sn SERVICENAME [-hn HOSTNAME][-rf root_folder]
[-bsf BASE_STORAGE_FOLDER][-u username] [-p PASSWORD] -o
OUTPUT

<h3>arguments</h3>
<p>
<strong>-h, --help</strong> show this help message and exit <br>
<em>-sn </em> SERVICENAME, --servicename SERVICENAME Service name <br>
-hn HOSTNAME, --hostname HOSTNAME Alfresco host url or hostname <br>
-rf ROOT_FOLDER, --root_folder ROOT_FOLDER Alfresco base folder <br>
-bsf BASE_STORAGE_FOLDER, --base_storage_folder BASE_STORAGE_FOLDER <br>
Storage path for local system <br>
-u USERNAME, --username USERNAME Alfresco auth username <br>
-p PASSWORD, --password PASSWORD Alfresco auth password <br>
-o OUTPUT, --output OUTPUT Output file in csv <br>
</p>

<h4> Explain </h4>

<p>
<strong> SERVICENAME </strong>: Is endpoint you want to crawl <br>
<strong> ROOT_FOLDER </strong>: Is base endpoint <br>
Example : ROOT_FOLDER : DSI , SERVICENAME : Network <br>
</p>
