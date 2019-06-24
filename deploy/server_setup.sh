#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/dev-tanvir/drf_users_api.git'

PROJECT_BASE_PATH='/usr/local/apps'
VIRTUALENV_BASE_PATH='/usr/local/virtualenvs'

# Set Ubuntu Language
locale-gen en_US.UTF-8

# Install Python, SQLite and pip
echo "Installing dependencies..."
apt-get update
apt-get install -y python3-dev python3-venv sqlite python-pip supervisor nginx git

mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH/users_api

mkdir -p $VIRTUALENV_BASE_PATH
python3 -m venv $VIRTUALENV_BASE_PATH/users_api

$VIRTUALENV_BASE_PATH/users_api/bin/pip install -r $PROJECT_BASE_PATH/users_api/requirements.txt

# Run migrations
cd $PROJECT_BASE_PATH/users_api/src

# Setup Supervisor to run our uwsgi process.
cp $PROJECT_BASE_PATH/users_api/deploy/supervisor_users_api.conf /etc/supervisor/conf.d/users_api.conf
supervisorctl reread
supervisorctl update
supervisorctl restart users_api

# Setup nginx to make our application accessible.
cp $PROJECT_BASE_PATH/users_api/deploy/nginx_users_api.conf /etc/nginx/sites-available/users_api.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/users_api.conf /etc/nginx/sites-enabled/users_api.conf
systemctl restart nginx.service

echo "DONE! :)"