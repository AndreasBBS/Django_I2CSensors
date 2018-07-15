# Django_I2CSensors
Django backend App with REST API (djangorestframework) to run on RaspberryPi and access I2C sensors.

## Requirements
```
pip3 install djangorestframework django-filter
```
## Installing
Open (workspace)/(DjangoProject)/(DjangoProject)/settings.py, find:
```
INSTALLED_APPS = [ ... ] , add:
-'rest_framework'
-'filter'
-'I2CSensors'
```
