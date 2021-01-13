#!/bin/bash

# copy cronfile to directory 
yes | cp -rf /home/seluser/Brunettes/root /var/spool/cron/crontabs

service cron start

