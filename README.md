
### Commands 

#### Launch virtual environement and install dependencies
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Run development server
```
FLASK_ENV=development FLASK_APP=application flask run
```