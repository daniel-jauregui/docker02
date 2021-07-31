# My Steps

1. Create an app.py file and add my application

2. Enter in a python environment and install
  
    `pip3 install Flask`

    `pip3 freeze > requirements.txt`

3. Create a Dockerfile and setup layers for new image

4. To build application with tag

    `docker build . -t ruleof3:0.1`

5. add tag for dockerhub

    `docker tag ruleof3:0.1 leinadx4/ruleof3:daniel.jauregui`

6. Login to dockerhub and push the image

    `docker push leinadx4/ruleof3:daniel.jauregui`

7. Configured the my local nexusts but looks like I need license to upload own images:

8. I used the Nexus 3 OSS on (10.24.48.191)

    `docker push 10.24.48.191:8082/ruleof3:daniel.jauregui`

9. For docker.jala.pro

    `docker tag ruleof3:0.1 docker.jala.pro/docker-training/ruleof3:daniel.jauregui`

# How to deploy ?

1. In you docker machine execute the following:

    `docker pull leinadx4/ruleof3:daniel.jauregui`

2. When image is in your machine execute the following:

    `docker run -d -p 5000:5000 --name rule2  leinadx4/ruleof3:daniel.jauregui`

3. Open you browser and go to:

    `http://<your_ip>:5000`

4. Enjoy!


