# SpotifyClone-Django
Made using Django, this was made for the groups final project in Database Systems.

## Selfhosting the website
- clone the repo
- the manage.py should already be able to run the server

## Troubleshooting: 
Make sure you have proper django version, the porject uses Django 4.0.4
  - ```python -m django --version```
If you made any changes to the models then you'll have to make migrations in order to update the db
  - ```./manage.py makemigrations```
  - ```./manage.py migrate```
