# Emoji Test App
App for monitoring analog astronauts' emotion changes during the missions in form of simple test. Django, Angular, PostgreSQL

## Demo
Demo aviable at http://emoji-test-app.herokuapp.com/

## Local environment

$ python manage.py runserver --settings=emojisite.local_settings

$ ng build --prod --output-path ../emojiapp/static/ang --watch --output-hashing none

## Deploy

$ git push heroku master
