# Python_Django-basic
## Project setup

- `cd workshop`
- `source env/bin/activate`
- `cd workshop`
## Start Develop
- `python3 manage.py makemigrations backend`
- `python3 manage.py migrate`
- 
    ## init data
- `python3 manage.py loaddata ../models4workshop/shop_models.json`

- `python3 manage.py runserver`
- `go to (ctrl + left-click) url http://127.0.0.1:8000/`