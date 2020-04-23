# Group Members:
Celine Huang 260707291
Jim Prescott 260738187
Jacek Dziewonski 260731690

# Buy& Sell Marketplace for Music

## Backend Set Up

Set up a Python virtual environment for the backend:

```
python3 -m venv env

source env/bin/activate
```
CD into the correct directory:

```
cd newbackend/Zola
```
Once the environment is activated, install requirements:

```
pip install -r requirements.txt
```
On windows, download a recent stable executable of Redis, and run redis-server.exe.
https://github.com/microsoftarchive/redis/releases

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
