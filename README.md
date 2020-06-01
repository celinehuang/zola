# Buy& Sell Marketplace for Music
Built By
[Celine Huang](https://github.com/celinehuang)
[Jim Prescott](https://github.com/jimprescott)
[Jacek Dziewonski](https://github.com/JDziewonski98)

![github-small](https://github.com/celinehuang/zola/blob/screenshots/pics/zola1.PNG)
![github-small](https://github.com/celinehuang/zola/blob/screenshots/pics/zola2.PNG)
![github-small](https://github.com/celinehuang/zola/blob/screenshots/pics/zola3.PNG)
![github-small](https://github.com/celinehuang/zola/blob/screenshots/pics/zola4.PNG)
![github-small](https://github.com/celinehuang/zola/blob/screenshots/pics/zola5.PNG)

## Backend Set Up

IMPORTANT:
Please note that the correct backend folder is named "newbackend" !!!!!!

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

The project comes without a database or any migrations.
To set up the database before the first time you run it:

```
python manage.py makemigrations vueapi
python manage.py migrate
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

## Registering a user

To access the site, you must make an account.
Certain things, like a password that is too simple, or an incorrect email format, will make account registration fail.
We recommend you use the following to register if you're having trouble registering and logging into the site:

Username : johndoe
Password : testzolapass123
email : jdoe@gmail.com

