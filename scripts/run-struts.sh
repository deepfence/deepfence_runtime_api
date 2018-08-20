#!/bin/bash
echo "Running Apache Struts app container"
docker rm -f struts
docker run -d --name=struts -p 8080:8080 --net=host --security-opt seccomp:unconfined -v /tmp:/tmp deepfenceio/deepfence_apache_struts_app
sleep 30;
curl 127.0.0.1:8080

