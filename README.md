# DJANGO Starter Template

This is the starter template for Django Projects mostly used by myself. 

First of all clone this Repository to Your local systerm by issuing the command

```
    ~$ git clone https://github.com/this-is-r-gaurav/django-dockerized-template.git
    ~$ cd django-dockerized-template
    ~/django-dockerized-tempalte$
```

1. With Docker
2. Without Docker


Before proceding to making it work, first of all do some changes, The first step is necessary and all remaining step are not necessary:

* Generate a secret key by issuing following Command in the console and Copy the text generated in the file `~/django-starter-template/src/starterTemplate/settings.py` to `SECRET_KEY` variable.

```
    ~$ python3 manage.py shell -c "from django.core.management import utils;print(utils.get_random_secret_key())"

```


* If You are building a specific project then you might want to change the name of the project from starterTemplate to specific Project You can do this by changing following files:

   * First of all change the name of `starterTemplate` directory in `src` directory to `yourProjectName`.
   * Then in `settings.py` change following variable `ROOT_URLCONF = 'starterTemplate.urls'` to `ROOT_URLCONF = 'yourProjectName.urls'`, `WSGI_APPLICATION = 'starterTemplate.wsgi.application'` to `WSGI_APPLICATION = 'yourProjectName.wsgi.application'
   * In `wsgi.py` file  `os.environ.setdefault("DJANGO_SETTINGS_MODULE", "starterTemplate.settings")` to `os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yourProjectName.settings")`
   * In `manage.py` file `os.environ.setdefault("DJANGO_SETTINGS_MODULE", "starterTemplate.settings")` to `os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yourProjectName.settings")`


## Run The Project(With Docker)

```
    ~/django-starter-template/$ docker build -t starter-template .
    ~/django-starter-template/$ docker-compose up -d starter
```

Then open the url `localhost:8000`. Your Application will be running.

## Run the project(without docker)

```
    ~$ virtualenv venv
    ~$ source venv/bin/activate
    ~$ cd django-starter-template
    ~/django-starter-template/$ pip3 install -r requirements.txt
    ~/django-starter-template/$ cd src
    ~/django-starter-template/src/$ python3 manage.py runserver
```

Then open the url `localhost:8000`. Your Application will be running.




