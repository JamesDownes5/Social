# Social

Hey everyone,

Hope you had a good christmas, new year, exam season and break before Semester 2. My late christmas present for you all, getting this project rolling so we have something to talk about next meeting.

## Git Rules

1. Never commit to the master branch.
2. Only merge changes to the master branch once approved by the whole group.
2. When working on the code base, work on your own seperate branch.

## Set Up

If you are developing on anything other than GNU/Linux, I heartly recommend that you obtain access to a GNU/Linux machine, be that a VM or Kilburn machine, before starting to work on this project, just to save you from any more work than nessecary. The following commands are for a GNU/Linux machine.

1. Create a directory called social in the your home directory (mkdir social)

2. Inside of this directory, clone the git repository

### MySQL Server

The MySQL server is how Django interacts with the database to obtain data.

1. Install MySQL server (sudo apt install mysql-server)

2. Run MySQL (sudo mysql)

Run all following commands in the mysql shell

3. Create a database (CREATE DATABASE social_db;)

You can do (SHOW DATABASES;) to see if it's there.

4. Create a user, replacing password with the one in settings.py (CREATE USER 'django'@'localhost' IDENTIFIED BY 'password';)

5. Grant user all privileges (GRANT ALL ON social_db.* TO 'django'@'localhost';)

6. Commit privilege changes (FLUSH PRIVILEGES;)

Control-D to get back to terminal

7. Install MySQL connector packages (sudo apt install libmysqlclient-dev default-libmysqlclient-dev build-essential)

### Python Virtual Enviroment

https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment
https://docs.python.org/3/library/venv.html

The python virtual environment will ensure that everyone is using the same versions of each of the python packages in the project to avoid any errors arising from different versions of modules being used.

I have decided to use Python 3.8 because it's the version that currently ships with most GNU/Linux distros and therefore is stable

1. Check that you are using Python 3.8 (python3 --version)

2. Inside ~/social/ create a virtual evironment (python3 -m venv venv). You might have to install python3-dev if this doesn't work (Just do what the error message says)

3. Now start the virtual environment (source venv/bin/activate). A little thing, (venv), should appear on the left side of the terminal

4. Install the python packages that are required (python3 -m pip install -r requirements.txt)

Whenever you are working on the project, make sure the virtual enviroment is running.

If you ever install more python packages make sure to add them to the requirments.txt, before commiting changes (python3 -m pip freeze > social/requirements.txt)

### Django

Make sure virtual environment is running and you are in ~/social/social/

1. Make migrations with MySQL database (python manage.py migrate)

2. Then run django web development server (python manage.py runserver)

You should then be able to access the server through your browser on http://127.0.0.1:8000/
