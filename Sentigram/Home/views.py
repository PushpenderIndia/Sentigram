from django.shortcuts import render, redirect
from .models import Company, TweetSentiment

def home(request):
    return redirect('/company')

def company(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        company = Company.objects.create(name=name)
        # Perform Twitter search and sentiment analysis here (not implemented in this code snippet)
        return redirect('result/?company='+name)
    return render(request, 'company.html')

def result(request):
    # Get the 'company' parameter from the GET request
    company_name = request.GET.get('company')

    # Filter tweets based on the company name if provided, otherwise get all tweets
    if company_name:
        sentiments = TweetSentiment.objects.filter(company__name=company_name)
    else:
        sentiments = TweetSentiment.objects.all()

    total = len(sentiments)
    positive = sentiments.filter(mood='Positive').count()
    negative = sentiments.filter(mood='Negative').count()
    orientation_percentage = (negative+1)/(total+1) * 100

    return render(request, 'result.html', {'sentiments': sentiments, 'orientation_percentage': orientation_percentage, 'total': total, 'negative': negative, 'positive': positive})
