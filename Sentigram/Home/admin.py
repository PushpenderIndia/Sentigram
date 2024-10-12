from django.contrib import admin
from .models import Company
from .models import TweetSentiment

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(TweetSentiment)
class TweetSentimentAdmin(admin.ModelAdmin):
    list_display = ('company', 'tweet_text', 'mood')
    list_filter = ('company', 'tweet_text', 'mood')
    search_fields = ('company', 'tweet_text', 'mood',)
