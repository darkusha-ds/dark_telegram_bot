#!/bin/sh

docker stop mtid_lessons && docker rm $(docker ps -a -q -f status=exited)