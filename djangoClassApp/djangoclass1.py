# MVT - Model, Views, Template
# URLs - Routing of webpages
# Road Map to setting your django project
# 1. create a folder - mkdir foldername
# 2. change directory to the folder name - cd folder name
# 3. Install virtual environment for your project - virtualenvwrapper.win (you must make sure that you have python installed into your system and a python package manager called PIP)
# 4. Create the virtual envirnment - (mkvirtualenv djangoClassApp) 
# 5. Activate the virtual environment - (windows 10 - workon djangoClassApp)
# (windows 11 - python -m venv djangoClassApp)

# (windows 11 - djangoClassApp\Scripts\activate.bat)
# 6. Install django into the virtual environment - pip install django
# 7. create your project (django-admin startproject projectname)
# 8. change directory to the project directory - cd djangoClass
# 9. runserver (python manage.py runserver)
# 10. Create app using (python manage.py startapp djangoClassApp)


# ASSIGNMENT
# Create your own project work.
# Virtual env - myFirstApp
# project name - myFirstProject
# project app - myFirstApp

# How to set up your Models.py file for your database
# 1. create your model class
# 2. do your migrations - python manage.py makemigrations (appname)
# 3. do your migrate - python manage.py migrate (appname)
# 4. create superuser - python manage.py createsuperuser