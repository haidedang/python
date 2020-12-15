# How the Instabot works 

Docker image has the Ubuntu Image 18.04 as an base image. This image has already chrome and a VNC instance installed. This means this Image is already able to run GUI applications on its own. The image also has a VNC server installed. That means this instance is like a “virtual PC instance” already and read to stream its "monitor" content.

Your local machine, this can be your MAC, or Windows can now connect to this docker instance as an VNC client and receive this content. 

No matter where this docker image runs,  it bind its selenium and VNC port to its  docker host. This docker host can be another PC or a cloud deployed virtual machine. Now your VNC client , your Mac or Windows is able to connect to that port through a VNC Viewer. Your deployed virtual machine does not even need a GUI! Because Docker has that GUI running inside its own container. And that really is awesome. 

The Docker image is hosted on Docker Hub. This docker image now has actually a stateless container running. That is why the virtual machine on the cloud has to pull GitHub repo. The docker binds this folder living on the virtual pc and mounts it into the container. From there the script is accessing these files and posting them on Instagram. To allow for full automation, docker image has a cronfile installed. Once docker is running as 24/7 background service on the Digital droplet which is basically your 24/7 PC living in the cloud, you have to manually start the CRON service once. 

`crontab -e` allows for editing the task automation schedule file of the user. 

The instabot itself runs with certain chrome options. First log in requires credentials. After that user credentials will be saved in a folder called selenium and every time the script runs Chrome will access this folder and launch a instagram session with cookies. This prevents a new user login authentification every time. 

# Summary 

- pull the instabot docker image 
`docker pull haidedang/instabot`

- pull the github repo and install to /home on your host 
`cd /home`
`git clone https:github.com/haidedang/python.git`
    
- Run the image on the host machine 
`docker run  -it  -d -p 4444:4444 -p 5900:5900 --name insta  -v /home/python/Instagram:/home/seluser/Instagram haidedang/instabot`

Note: All dependencies are already installed on the image. No need to install it on your remote host anymore. 

- Open docker terminal of the running container 
`docker exec -it insta bash `

- Start the cron service 
`sudo /etc/init.d/cron start`

