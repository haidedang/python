#!/bin/bash

# start docker 
docker run  -it  -d -p 4444:4444 -p 5900:5900 --name insta  -v /Users/Hai/github/python/Instagram:/home/seluser/Instagram instabot 