# QA-KPI

sh ./client/fileclient.sh
sh ./server/fileserver.sh

docker exec -it *containter* /bin/bash

I used named volumes just because task was "Create a volume **by name** "servervol"" It also helps to save your data after restarting or removing container and can be found under a specific host directory.

