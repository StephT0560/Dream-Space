# Dream-Space
A Book Social Network Platform

## Main Files:
`books.py` – provides book recommendation search
`app.py` – main site file
`model.py` –
`forms.py` – template to create forms for user registration/login

## Installations & Imports
#### Google Books API
In order to have access to the Google Books API, you will need to have a Google account. After you login to or create your Google account, you must do the following:
1. Visit console.cloud.google.com
2. Click on ***Select a Project*** in the menu bar and then select ***New Project*** and name the project something relevant.
3. After you have a project, locate the ***APIs & Services*** option in either the tabs on the side of the page or the ***Quick Access*** Dashboard and click. Once you have arrived at the ***APIs & Services*** page, select the ***ENABLE APIS AND SERVICES*** option at the top.
4. When you reach the ***Welcome to the API Library*** screen, search for books and select the ***Books API*** option. Enable the API. 
5. Once you have enabled the API, return to the ***APIs & Services*** Screen and select ***Credentials*** from the sidebar. Once on the page, select ***Create Credentials*** and create and store the generated key. This key is required in the URL for use of `GET` and `POST` requests with the Google Books API.
6. (Optional) To learn more about the requests you can use in the Google Books API, vist this guide on https://developers.google.com/books/docs/v1/using

#### books.py 
To begin, install the Google Books API on your terminal for python:
`pip install google-api-python-client`

After doing so, import necessary libraries:

``` python 
    import requests # access to `GET` & `POST` requests to extract info from the Google Books API, and access to json to parse that info
    import random # allows you to generate random integers
```


#### app.py, models.py, & forms.py
To begin, make the following installations in the terminal:
* `pip install Flask`
* `pip install flask_bcrypt`
* `pip install flask_login`
* `pip install peewee`

Import the following in `models.py`:
```python
from flask_bcrypt import generate_password_hash # allows you to use bcrypt hashing in Flask so you can ensure password security
from flask_login import UserMixin # handles user login, logout, and session memory in Flask
from peewee import * # helps with database mapping in framework
```

Import the following in `forms.py`:
```python
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, TextField 
from wtforms.validators import (
    DataRequired,
    ValidationError,
    Email,
    Length,
    EqualTo,
    Regexp,
) # uses wtforms to ensure users enter in valid information for login/registration
from models import User # imports function from our models.py
```

Import the following in `apps.py`:
```python
import models #imports our models.py
import forms #imports our forms.py
from flask import Flask, g, render_template, flash, redirect, url_for, abort # allows you to use Flask as app's web framework and its functions
from flask_bcrypt import Bcrypt, check_password_hash # allows you to use bcrypt hashing in Flask so you can ensure password security
from flask_login import ( 
    LoginManager,
    LoginManager,
    login_user,a
    logout_user,
    login_required,
    current_user,
) # handles user login, logout, and session memory in Flask
```

## Environment Functions and Important Variables
### Variables:
#### books.py
`api_key` – user's API key that will be used for the URL
`base_url` – base of url to be used for search-based `GET` requests to Google Books

#### app.py
`login_manager` – LoginManager Object

### Functions & Classes
#### books.py
`user_inputs` – function that takes in user inputs for user's preferred genre, author, or book that they want recommendations based on and returns info in tuple

`genre_recs` – function that returns dictionary of list of recommendations based on genre user inputted

`author_recs` – function that returns dictionary of list of recommendations based on author user inputted

`book_recs` – function that returns dictionary list of recommendations based on book user inputted

`output_recs` – function that runs the previous functions and prints each recommendation collected

### models.py
`User` ***FILL IN PLEASE***

`Post` ***FILL IN PLEASE***

`Relationship` ***FILL IN PLEASE***

### forms.py
`name_exist`, `email_exists` – functions that ensure that username and email user has submitted are legit/within databse of users

`Registration Form` – class that allows user to register for account on blog

`Login Form` – class that allows user to log in on blog

`PostForm` ***FILL IN PLEASE***


#### app.py
`register` – function that creates user registration by storing user details in `*Registration Form*` object from`forms.py`

`login` – function that performs user login using `forms.py`

`stream` – ***FILL IN PLEASE***

`view_post` – function that renders all posts in database

`follow` – function that allows one user to follow another using `User` class object from `models.py` to get user information

`post` – function that uses `PostForm` function from `forms.py` to let user make a post


## How the App Works
***FILL IN PLEASE***
