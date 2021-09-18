## PLAYLIST TO YOUTUBE


### STEPS in local:
 
  #### clone the repo and setup a virtual environment with ide. Now open a terminal and run the following:

    $ source venv/bin/activate   
    $ pip3 install -r requirements.txt 

  ### Run the script src/run.py

    $ python  src/run.py
      
  ### test with some data, edit the file paths.
  
     $  curl --request POST --url 'http://172.28.98.151:5051/api/fetch_path' --header 'content-type: application/json'  --header 'timestamp':'2021-01-09 10:00:00' --header 'modelversion':'1.0.0'  --data '{}'


### You shall see the result coming up as json
 
### STEPS for docker:
  ### build docker file
  
     $ docker build -t playlist-to-youtube:1.0.0 .
     
    
   ### start the flask app
  
      $ docker run -p 5000:5000 playlist-to-youtube:1.0.0
      
  ### test with some data
  
      $ curl --request POST --url 'http://0.0.0.0:5000/api/fetch_path' --header 'content-type: application/json' --header 'timestamp':'2021-01-09 10:00:00' --header 'modelversion':'1.0.0'  --data '{}'

### You shall see the result coming up as json


