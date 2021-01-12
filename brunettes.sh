#!/bin/bash

# start VPN 
docker run -ti -d --cap-add=NET_ADMIN --device /dev/net/tun --name vpn2 -p 4445:4444 -p 5901:5900  -e RANDOM_TOP=10 -e COUNTRY=Germany -e USER=rafael@uzarowski.de -e PASS=KyFn3ztnZW8 azinchen/nordvpn

# start docker 
# docker run  -it  -d -p 4445:4444 -p 5901:5900 --name insta  -v /Users/Hai/github/python/Brunettes:/home/seluser/Brunettes instabot 
docker run  -it  -d --name brunette --net=container:vpn2  -v $(pwd)"/Brunettes":/home/seluser/Brunettes instabot 
