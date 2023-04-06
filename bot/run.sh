#!/bin/sh

docker build -t darkushads/mtid_lessons . && docker run -d --name mtid_lessons darkushads/mtid_lessons