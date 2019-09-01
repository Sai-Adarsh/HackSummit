# Team Albuquerque
## Stress Monitoring

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)](https://forthebadge.com)

## Project Description
 
* Detection of Mental Health diseases with accuracy by means of generating a body heat map of the patient with the help of a thermal camera and applying techniques of image processing and Deep Learning image classification models to measure the magnitude of the detected disease.

* For working **photos and videos** [click here](https://github.com/Sai-Adarsh/ThermalAI/tree/master/WorkingPhotos).
* To know **information** more about the [problem & our solution](https://github.com/Sai-Adarsh/ThermalAI/blob/master/Phase1/Team%20Appendly%20-%20Shaastra%20AI%20Challenge%202018%20Phase%20I%20Ideation.pdf)


## Architecture 
![Architecture](https://i.imgur.com/7ddd0JV.jpg)

## Dataset !!

* [Dataset - Visual Computing and Image Processing Lab 
Oklahoma State University](http://vcipl-okstate.org/pbvs/bench/Data/04/download.html)
* [Sample Dataset - Visual Computing and Image Processing Lab 
Oklahoma State University](http://vcipl-okstate.org/pbvs/bench/Data/04/face01.zip) 

## TechStacks

![TechStacks](https://i.imgur.com/faiMtm6.png)
## Install

### Clone this repository
```
  git clone https://github.com/Sai-Adarsh/thermalboilerplate
  cd thermalboilerplate
``` 
### Create a virtualenv
```
  virtualenv venv
  cd venv/Scripts
  activate
```
### Install python dependencies
```
  pip install -r requirements.txt
```

### For Training:
  * Paste the dataset inside Train folder
```
  python train.py
```
### For Testing
```
  python test.py
```

### Run the webapp
```
  python app.py
```

### API usage
  * Open [API docs](https://github.com/Sai-Adarsh/thermalboilerplate/blob/master/docs/api.md) to use the api using curl
  ```
    curl -X POST http://thermalstress.herokuapp.com/api -F "file=@filename"
  ```  
