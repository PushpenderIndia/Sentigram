from django.urls import path
from .views import SentimentAnalysisView

urlpatterns = [
    path('twitter_sentimental', SentimentAnalysisView.as_view(), name='twitter_sentimental'),
]