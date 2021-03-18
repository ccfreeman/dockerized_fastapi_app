 Docker commands to run application:
 ```
 >> docker build -t flask-app .
 >> docker run -d -p 5000:5000 flask-app
```
The first command builds the image of your project. This will be used to build the container itself with the proper environment. The second command launches your (detached) container from the image you've just built, and maps port 5000 on your local machine to port 5000 in the container's directory.

Get the name of your container:
 ```
 >> docker ps
...CONTAINER ID   IMAGE       COMMAND                  CREATED          STATUS         PORTS                    NAMES
...3f1b1e2f1f20   flask-app   "/bin/sh -c ./entry-…"   10 seconds ago   Up 8 seconds   0.0.0.0:5000->5000/tcp   upbeat_beaver
```
** Note that the name of your image and your container are different. 
Stop running your container:
```
>>> docker stop [container_name]
```
To completely clean your containers and images from the directory:
```
>>> docker system prune -a
```