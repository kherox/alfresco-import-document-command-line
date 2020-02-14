# alfresco-import-document-command-line

This program help you to export all alfresco content into ouput file

usage: main.py [-h] -sn SERVICENAME [-hn HOSTNAME][-rf root_folder]
[-bsf BASE_STORAGE_FOLDER][-u username] [-p PASSWORD] -o
OUTPUT

arguments:
-h, --help show this help message and exit
-sn SERVICENAME, --servicename SERVICENAME Service name
-hn HOSTNAME, --hostname HOSTNAME Alfresco host url or hostname
-rf ROOT_FOLDER, --root_folder ROOT_FOLDER Alfresco base folder
-bsf BASE_STORAGE_FOLDER, --base_storage_folder BASE_STORAGE_FOLDER
Storage path for local system
-u USERNAME, --username USERNAME Alfresco auth username
-p PASSWORD, --password PASSWORD Alfresco auth password
-o OUTPUT, --output OUTPUT Output file
