# Django_I2CSensors
Django backend App with REST API (djangorestframework) to run on RaspberryPi and access I2C sensors.

## Requirements
```
pip3 install djangorestframework django-filter
```

### Pre Installing (Skip if you already created your Django Proj)
Open terminal on your workspace folder, run:
```
django-admin startproject (DjangoProject)
NOTE: Choose any name you want for your project and replace with (DjangoProject)
```

## Installing
Open terminal on (workspace)/(DjangoProject), run:
```
git clone (thisRepoURL.git)
```

Open (workspace)/(DjangoProject)/(DjangoProject)/settings.py, find:
```
INSTALLED_APPS = [ ... ] , add:
-'rest_framework'
-'filter'
-'I2CSensors'
```

Open terminal on (workspace)/(DjangoProject), run:
```
python3 manage.py makemigrations

python3 manage.py migrate
```

### Pre Use (Skip if you already setup a superuser)
Open terminal on (workspace)/(DjangoProject), run:
```
python3 manage.py createsuperuser
Enter Username and Password (Use a strong Password)
```

## Use 

