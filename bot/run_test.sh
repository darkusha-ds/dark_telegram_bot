#!/bin/sh

docker build -t darkushads/test_mtid . && docker run -d --name test_mtid darkushads/test_mtid