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

To run the Django backend:
```
python manage.py runserver
```

## Redis Set Up (for our marketplace chat room)
You should do this inside of your virtual environment as well!

### Mac OS
To install Redis:
```
brew update
brew install redis
```
To have launchd start redis now and restart at login:
```
brew services start redis
```
Test if Redis server is running.

```
redis-cli ping
```
If it replies “PONG”, then it’s good to go!

### Windows
Download a recent stable executable of Redis, and run redis-server.exe.
https://github.com/microsoftarchive/redis/releases

## Frontend Set Up

To run the frontend, you will need to install the [Quasar CLI](https://quasar.dev/quasar-cli/installation) and **version 3 or higher** of the [Vue CLI](https://cli.vuejs.org/guide/installation.html). If you have an older version of Vue CLI installed, you will need to uninstall it and re-install the latest version.

To install dependencies, run `npm install` or `yarn install` in the `frontend` folder. To run the frontend from the `frontend folder`:

```
quasar dev
```

