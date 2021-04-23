## 🚀 Features

- Django 3.1 & Python 3.8
- Install via [Pip](https://pypi.org/project/pip/), [Pipenv](https://pypi.org/project/pipenv/), or [Docker](https://www.docker.com/)
- User log in/out, sign up, password reset via [django-allauth](https://github.com/pennersr/django-allauth)
- Static files configured with [Whitenoise](http://whitenoise.evans.io/en/stable/index.html)
- Styling with [Bootstrap v4](https://github.com/twbs/bootstrap)
- Debugging with [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)
- DRY forms with [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms)

----

## Table of Contents
* **[Installation](#installation)**
  * [Pip](#pip)
  * [Pipenv](#pipenv)
  * [Docker](#docker)
* [Setup](#setup)
* [Contributing](#contributing)
* [Support](#support)
* [License](#license)

----

## 📖 Installation
Can be installed via Pip, Pipenv, or Docker depending upon your setup. To start, clone the repo to your local computer and change into the proper directory.

```
$ git clone https://github.com/rigelk/magiciendose
$ cd magiciendose
```

### Pip

```
$ python3 -m venv magiciendose
$ source magiciendose/bin/activate
(magiciendose) $ pip install -r requirements.txt
(magiciendose) $ python manage.py migrate
(magiciendose) $ python manage.py createsuperuser
(magiciendose) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```

### Pipenv

```
$ pipenv install
$ pipenv shell
(magiciendose) $ python manage.py migrate
(magiciendose) $ python manage.py createsuperuser
(magiciendose) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```

## Setup

```
# Run Migrations
(magiciendose) $ python manage.py migrate

# Create a Superuser
(magiciendose) $ python manage.py createsuperuser

# Confirm everything is working:
(magiciendose) $ python manage.py runserver

# Load the site at http://127.0.0.1:8000
```

----

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

## License

[The MIT License](LICENSE)
