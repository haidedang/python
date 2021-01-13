#!/bin/bash

# start VPN 
docker run -ti -d --cap-add=NET_ADMIN --device /dev/net/tun --name vpn -p 4444:4444 -p 5900:5900  -e RANDOM_TOP=10 -e COUNTRY=Germany -e USER=rafael@uzarowski.de -e PASS=KyFn3ztnZW8 azinchen/nordvpn

# start docker 
docker run  -it  -d --name insta --net=container:vpn -v /Users/Hai/github/python/Instagram:/home/seluser/Instagram haidedang/instabot:latest 

