#!/bin/sh

docker stop test_mtid && docker rm $(docker ps -a -q -f status=exited)