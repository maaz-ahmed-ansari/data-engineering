```docker run hello-world```

 - This will download and run docker image named: "hello-world" from docker hub

 ```docker run -it ubuntu bash``` 

- Everything comes before image name are parameters the container
- -it -> interactive terminal
- Ubuntu -> image, bash -> command on top of image
- Here docker will run ubuntu image and run bash command in ubuntu image
- Note: if we delete everything (e.g. rm -rf /) on the image and re-reun that image, it will go to original state. i.e. docker images run in isolation. If app running in image do some stupid things, host machine will not be affected

```docker run -it python:3.9```

- Here image name is python, and 3.9 is a tag, tag we can assume as specific version of the image

```docker run -it  --entrypoint=bash python:3.9```
- Here we are overwriting entrypoint, entrypoint is what executed when image is ran
- On top of python image, in bash terminal we can import libraries such as pandas, etc. which then can be used in python program on the container
	
- Since docker container runs in isolation and original image here python, do not have additional libraries we installed manually. When we rerun this image, all the additional libraries went away and only original image is there

- We can customize image (using Dockerfile) so that when we build and run, it installs all the apps mentioned in the Dockerfile
	- Dockerfile will start with FROM <base image name>, and additional lines such as RUN <command>, ENTRYPOINT ["<specify here>"] and other customizations
	- Build and run docker image with Dockerfile:
		○ $ docker build -t <name for image> <path to Dockerfile>
		○ e.g. $ docker build -t test:pandas .   # test:pandas is name of imagea
		○ To run: $ docker run -it test:pandas

- Can execute various commands e.g. run a python file that takes one command line argument and also importing pandas 
- e.g.
  
```
Dockerfile
	FROM python:3.11
	RUN pip install pandas
	ENTRYPOINT [ "bash" ]
```

```
Dockerfile:
	FROM python:3.11
	
	RUN pip install pandas
	
	WORKDIR /app
	
	COPY pipeline.py pipeline.py
	
	ENTRYPOINT [ "python", "pipeline.py" ]
```

```
pipeline.py 
	pipeline.py:
	
	import sys
	
	import pandas as pd
	
	print(sys.argv)
	
	day = sys.argv[1]
	
	print(f"job executed successfully for day {day}")
```

### Brief:
- Here on base image python:3.11, docker will install pandas library
- And create a workdir on image names app
- And copy pipeline.py from local machine in same folder where dockerfile is presnt (although you can give complete path of file) to docker image in workdir app with name specified pipeline,py in second place
- Also, docker will expose entrypoints in sequence specified python -> pipline.py 
- Meaning since pipeline.py file is expecting at least 1 command line argument, and it is exposed while attempt to running image, we need to give one argument while calling docker run
- e.g. 
		```winpty docker run test:pandas 2023-09-02```
		
### Docker compose:
- Docker Compose is a tool for defining and running multi-container applications. It is the key to unlocking a streamlined and efficient development and deployment experience.


### Setup Ubuntu UI and connect via Chrome RDP 
https://medium.com/@selvamraju007/install-and-launch-ubuntu-22-04-desktop-on-google-cloud-1fba8c0f9585![image](https://github.com/maaz-ahmed-ansari/data-engineering/assets/70753689/9c947450-e761-4c56-a719-ef02d88c2615)
