#!/bin/bash

# heroku login
# heroku container:login

heroku container:push worker --app discord-bot-mecab && \
heroku container:release worker --app discord-bot-mecab
