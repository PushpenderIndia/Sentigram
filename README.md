# Sentigram
Develop an AI model to understand the sentiments about the company using social media feeds (such as Twitter, Facebook, Linkedin, and other digital media inputs)

## Data Source
- Twitter Data Source https://www.kaggle.com/kazanova/sentiment140

## Technologies Used
- Django
- PostgresSQL

## Django Admin Creds
- Username: admin
- Email: pushpender@witeso.com
- Password: SentigramAdmin#@666
- URL: https://sentigram.witeso.com/admin

## Video Demo
[Video](Demos/L&T_Final.mp4)

## TODO
- [ ] Integrate Twitter Sentimental Analysis Model
- [ ] Improve Frontend

## Run Application
```
# Download Project
git clone https://github.com/WitesoAI/Sentigram.git

# Navigate to project
cd Sentigram/Sentigram

# Create Virtual Environment (Only for once)
virtualenv venv

# Active Virtual Environment (Linux)
source venv/bin/activate

# Active Virtual Environment (Windows)
venv\Scripts\activate

# Install Dependencies
pip install -r requirements.txt

# Create DB (Only Once)
python manage.py makemigrations
python manage.py migrate

# Run Python Server
python manage.py runserver
```

## Routes

- [ ] `/company`: Page to Take Details about the company
- [ ] `/result`: Page to should Sentimental Analysis of Social Media Feed
