from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .ml_utils import predict_sentiment
from .serializers import SentimentSerializer
from Home.models import Company, TweetSentiment

class SentimentAnalysisView(APIView):
    def post(self, request):
        input_text = request.data.get('text', '')  # Use get() to provide a default value if key is missing
        company_name = request.data.get('company', 'Google') 

        # Get or create the Company instance
        company_instance, created = Company.objects.get_or_create(name=company_name)

        # Predict sentiment
        predicted_label = predict_sentiment(input_text)

        # Create TweetSentiment instance
        tweet_sentiment = TweetSentiment.objects.create(
            company=company_instance,
            tweet_text=input_text,
            mood=predicted_label
        )

        return Response({'predicted_sentiment': predicted_label}, status=status.HTTP_201_CREATED)
