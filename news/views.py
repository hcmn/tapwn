from datetime import datetime
from django.http import Http404
from django.shortcuts import render_to_response
from tapwn.news.models import Headline

def home(request):
    headlines = Headline.objects.all()
    return render_to_response('news/home.html', {'right_now':datetime.utcnow(), 'headlines':headlines})

def headline_detail(request, headline_id):
    try:
        headline = Headline.objects.get(pk=headline_id)
    except Headline.DoesNotExist:
        raise Http404
    return render_to_response('news/headline_detail.html', {'headline':headline})