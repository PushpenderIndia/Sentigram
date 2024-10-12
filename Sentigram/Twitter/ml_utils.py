import pickle
from nltk.tokenize import word_tokenize
import re, os 
from django.conf import settings

CV_FILE = os.path.join(settings.STATICFILES_DIRS[0], 'models/CountVectorizer.pkl')
MODEL_FILE = os.path.join(settings.STATICFILES_DIRS[0], 'models/Twitter.pkl')

with open(CV_FILE, 'rb') as file:
    loaded_cv = pickle.load(file)

with open(MODEL_FILE, 'rb') as file:
    loaded_model = pickle.load(file)

# Preprocess text for prediction
def preprocess_text(text):
    text = text.lower()
    text = re.sub('[^A-Za-z0-9 ]+', ' ', text)
    tokens = word_tokenize(text)
    processed_text = ' '.join(tokens)
    return processed_text

# Make prediction using loaded model and vectorizer
def predict_sentiment(input_text):
    processed_input = preprocess_text(input_text)
    input_vector = loaded_cv.transform([processed_input])
    predicted_sentiment = loaded_model.predict(input_vector)
    return predicted_sentiment[0]
