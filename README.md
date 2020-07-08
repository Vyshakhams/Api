# Api

Django application with User and ActivityPeriod models, write
a custom management command to populate the database with some dummy data, and design
an API to serve that data in the json

* Install a virtual environment using pip.
  >> pip install virtualenvwrapper-win
* Created a virtual environment.
  >> mkdirvirtualenv FTL
* Create a new Django project as myproj.
  >> django-admin start project myproj
* Created a new app as api. 
  >> python manage.py startapp api
* Created a models called ActivityPeriod, User and ok.
  >> ActivityPeriod table contains start_time and end_time   
  >> User table contains id, real_name, tz and activity_periods(Foreign of ActivityPeriod table)
  >> ok table contains member(Foreign of User table)
* Used rest_framework for the serializers of JSON.   
  >> Added rest_framework in INSTALLED_APPS 
* Created classes and using Meta class in views.py and initialized model, fields and depth.
* Fetching data in views.py file using get_queryset method.
* Added path in url.py. 
