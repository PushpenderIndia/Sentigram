# Sentigram
We've developed this Project for a Hackathon (CreaTech Larson & Toubro 2024), where our team was semi finalist by competing amoung 13,362 Teams

## Overview:
- Sentigram is an innovative web solution designed to monitor social media platforms, enabling companies to assess public sentiment towards their brand in real time. 
- By leveraging advanced sentiment analysis techniques, Sentigram fetches tweets and messages from social media to classify sentiment as positive, negative, or neutral.

## Key Features:

- Real-Time Monitoring: Continuously scans social media channels for mentions of the company, providing up-to-the-minute insights into public perception.
Sentiment Analysis: Utilizes natural language processing (NLP) algorithms to analyze the tone of messages, accurately predicting the overall sentiment.

- Mood Meter: Displays a dynamic mood meter that visually represents the sentiment landscape based on the volume and nature of tweets at any given time.

## Objective:
- The primary goal of Sentigram is to swiftly identify negative sentiments related to the company, allowing for timely interventions to mitigate potential public relations issues. 
- By addressing negative feedback proactively, Sentigram aims to foster a trustworthy brand image and cultivate a loyal customer base.
- We have Developed an AI model to understand the sentiments about the company using social media feeds (such as Twitter, Facebook, Linkedin, and other digital media inputs)

## Data Source
- Twitter Data Source https://www.kaggle.com/kazanova/sentiment140

## Technologies Used
- Django
- PostgresSQL

## Video Demo
[Video](Demos/L&T_Final.mp4)

## TODO
- [ ] Integrate Twitter Sentimental Analysis Model
- [ ] Notify Concerned Department if the Mood Meter is negative 
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
