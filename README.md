# Team Albuquerque
## Mental stress monitoring 


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
