from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

class TweetSentiment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    tweet_text = models.TextField()
    mood = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

