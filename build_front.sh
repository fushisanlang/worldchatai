#!/bin/bash
datestr=`date +%s`
cd /home/admin/cws-code/worldchatai
docker build . -t front:${datestr}
docker run  --rm front front:${datestr} /bin/sh -c "sleep 15"
rm -fr /home/admin/cws/cws_index/
docker cp front:/app/dist /home/admin/cws/cws_index/
sleep 15
docker rmi front:${datestr}
