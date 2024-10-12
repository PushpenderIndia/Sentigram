
#!/bin/bash

if [ -d "Sentigram/venv" ] 
then
    echo "Python virtual environment exists." 
else
    python3 -m virtualenv Sentigram/venv
fi

pwd
. Sentigram/venv/bin/activate

pip3 install -r Sentigram/requirements.txt
# python3 -m nltk.downloader punkt
python3 Sentigram/manage.py makemigrations
python3 Sentigram/manage.py migrate

if [ -d "logs" ] 
then
    echo "Log folder exists." 
else
    mkdir logs
    touch logs/error.log logs/access.log
fi

sudo chmod -R 777 logs