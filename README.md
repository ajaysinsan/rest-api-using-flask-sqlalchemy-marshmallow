# My RESP API

 REST API using Flask, SQLAlchemy and Mashmallow

## Clone

Clone the repo to your system

```bash
git clone https://github.com/ajaysinsan/rest-api-using-flask-sqlalchemy-marshmallow.git
```

## Installation

Create a virtual environment to run the project:

```bash
python3 -m venv venv
```


activate the virtual environment:

```bash
source venv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install -r requirements.txt
```


## Setup SQLITE Database

Go to terminal and start python shell to create tables in db:

```python
from app import db
db.create_all()
```

Add DB config to app.py

## Running Project

Change your directory to project directory and run the following command:

```python
python app.py 
```

## Usage
Please navigate to http://localhost:5000 and other urls through postman to hit the api.
