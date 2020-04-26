#!/bin/bash

# heroku login
# heroku container:login

heroku container:push web --app discord-bot-mecab && \
heroku container:release web --app discord-bot-mecab
