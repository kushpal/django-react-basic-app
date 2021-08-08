# A React and Django Rest Framework authentication +  file upload
This is a django-react app for simple authentication, uploading json file, and viewing the json file data

### Functionality:

* [x] Login with JWT
* [x] Middleware for JWT refresh if expiring
* [x] Logs in with username and password / logs out
* [x] Upload a json file
* [x] View the json file content in proper format
* [x] Screen size responsive components


### How to use:

- Clone the repo
#### my-app
1. cd my-app && npm install
2. Need to install 4 more packages (Material ui core, Material ui icon, Axios, and React router dom)  
3. npm start
#### SimpleProject
1. cd SimpleProject, create a virtualenv, activate it and install -r requirements.txt
2. python manage.py makemigrations , python manage.py migrate , createsuperuser
3. python manage.py runserver
#### File upload
  - format for the json file to be uploaded is given in this file: json_file_format.json 


