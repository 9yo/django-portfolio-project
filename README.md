# Contacts Book

![t](https://github.com/9yo/django-portfolio-project/blob/main/frontend/src/static/logo.png?raw=true)

[![Actions Status](https://github.com/9yo/django-portfolio-project/workflows/workflow-testing/badge.svg)](https://github.com/9yo/django-portfolio-project/actions)


**Table of Contents**

[TOCM]

[TOC]

#What it is?
A simple web project for storing and aggregating contacts.
#Functionality
With this app you can:
- Create/Edit/Delete Contacts
- Create/Edit/Delete Contacts books which is at is core a contact groups like family, friend, etc...
- Add/Remove contacts related to contact books.
- Find contacts/contact books by their name.

#Stack
Backend:
- Django
- PostgreSQL
- DRF
- JWT Authorization

Frontend:
- Vue.js
- Vuex
- Vuetify
- Axios


#Docker install
Just install Docker and start with
```console
	 docker-compose up

```
#Raw Install
First of all up PostgreSQL db and set it up as in backend/backend/settings.py.
The second step is execute this commands:
```console
	$ pip install venv
	$ python -m venv venv
	$ source venv/bin/activate
	$ pip install -r requirements.txt
	$ python backend/manage.py migrate
	$ python backend/manage.py runserver
	$ cd frontend
	$ npm install
	$ npm run serve
```
# After Install
After succesfull install you will be able to see:
- Backend server on localhost:8000
- Frontend server on localhost:8080

It is also possible to populate the database with folowing commands:
```console
	$ pip install requests
	$ python backend/contacts/test_utils/fill_db.py 
```
In backend docker container or just in terminal in case of raw install.
It will create a user with test login and password with auto generated contacts and contacts books.
