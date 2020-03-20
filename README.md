# 307_web_app

## Backend Set Up

Set up a Python virtual environment for the backend:

```
python3 -m venv env

source env/bin/activate
```

Once the environment is activated, install requirements:

```
pip install -r requirements.txt
```

CD into the correct directory:

```
cd backend/mysite
```

To run the Django backend:
```
python manage.py runserver
```

## Frontend Set Up

To run the frontend, you will need to install the [Quasar CLI](https://quasar.dev/quasar-cli/installation) and **version 3 or higher** of the [Vue CLI](https://cli.vuejs.org/guide/installation.html). If you have an older version of Vue CLI installed, you will need to uninstall it and re-install the latest version.

To install dependencies, run `npm install` or `yarn install` in the `frontend` folder. To run the frontend from the `frontend folder`:

```
quasar dev
```
