# Test Report
**I have been facing much errors with thhis test** 
1. Packages installation with **flask8 and guicorn** 
I have change guicorn with unicorn and i will plan to change the flask8 with ruff for the python test to be done.

2. Copying the code manuling is not a good idea for candidates 
3. Runtime issue since you have not provide any internet connection for candidate all this docker images building cannot be done
4. How can someone write a dockerfile test it,create a CI/CD pipeline and test it host this code on github for this CI/CD and test the erhpipeline  use kubernetes in 3 hours without any external help in 3hours bro it is just too much to build in only 3 hours wthout taking the copying of the code provide with my hands on the machine before even starting to work.

   
# Application setup 

1. **Task 1:Production Dockerfile**
I used python3.12-slim as base images for me docker which can seen on the image where i listed all my docker images.This is mainly done in the build stage then i have run the apt install command mainly to install our packages,,Move the whole installation inside an app directory  then Copy all the files from the requirements.txt file  Then remove all this Binaries in the second stage and create a newuser for the application and add him permission. Then just run the app from the containers using the Run script 

2. **Task 2 :API-Redis**
Here we are to write the docker-compose file that have to run our 3 services that is Redis,nginx and the application on each of their respective posts and also put them in network so that we can run all this services together and also add the volume to all this services 
