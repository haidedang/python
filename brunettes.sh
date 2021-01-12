#!/bin/bash

# start docker 
# docker run  -it  -d -p 4445:4444 -p 5901:5900 --name insta  -v /Users/Hai/github/python/Brunettes:/home/seluser/Brunettes instabot 
docker run  -it  -d -p 4445:4444 -p 5901:5900 --name brunette  -v $(pwd)"/Brunettes":/home/seluser/Brunettes instabot 
