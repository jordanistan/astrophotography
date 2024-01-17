<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Astrophotography" />

  &#xa0;

  <!-- <a href="https://astrophotography.netlify.app">Demo</a> -->
</div>

<h1 align="center">Astrophotography</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/jordanistan/astrophotography?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/jordanistan/astrophotography?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/jordanistan/astrophotography?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/jordanistan/astrophotography?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/jordanistan/astrophotography?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/jordanistan/astrophotography?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/jordanistan/astrophotography?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Astrophotography 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/jordanistan" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Here's a Python script that allows you to input the number of photos and the exposure time for each photo. It will then calculate the total time required for taking all the photos.


## :checkered_flag: Starting ##


# Clone this project

```
$ git clone https://github.com/jordanistan/astrophotography
```


# Access
```
$ cd astrophotography
```


#Create a Dockerfile: First, you need a Dockerfile to build a Python environment.

  Dockerfile

```
# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Run the script when the container launches
CMD ["python", "./time-teller.py"]
```


  Create a docker-compose.yml File: Next, create a docker-compose.yml file to define the service.

```
version: '3.8'
services:
  python-app:
    build: .
    stdin_open: true
    tty: true
```

This Compose file defines one service python-app, which is built from the Dockerfile in the current directory. stdin_open and tty are set to true to allow interactive input (like input() in your Python script).

Place Your Python Script in the Same Directory: Ensure your Python script (your_script.py) is in the same directory as your Dockerfile and docker-compose.yml.

Running the Docker Compose: To run your Docker Compose, use the following commands in the directory where your files are located:

```
docker-compose build
docker-compose up -d
docker exec -ti astrophotography-time-teller-1 python time-teller.py

```

This setup will create a Docker container that runs your Python script, allowing for interactive input as required by your script. Remember to install any additional Python packages you might need by updating the Dockerfile accordingly (using RUN pip install commands).

## :Demo: ##

[![Demo](timer-teller-demo.mp4)](timer-teller-demo.mp4)


Made with :heart: by <a href="https://github.com/jordanistan" target="_blank">Jordan</a>

&#xa0;

<a href="#top">Back to top</a>
