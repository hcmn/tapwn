from datetime import datetime

from django.shortcuts import render_to_response
from tapwn.news.models import Headline

def home(request):
    headlines = Headline.objects.all()
    return render_to_response('news/home.html', {'right_now':datetime.utcnow(), 'headlines':headlines})