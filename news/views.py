from datetime import datetime
from django.http import Http404
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from tapwn.news.models import Headline
from tapwn.news.forms import HeadlineForm

def home(request):
    headlines = Headline.objects.all()
    return render_to_response('news/home.html', {'right_now':datetime.utcnow(), 'headlines':headlines})

def headline_index(request):
    headlines = Headline.objects.all()
    return render_to_response('news/headline_index.html', {'headlines':headlines})

def headline_detail(request, headline_id):
    try:
        headline = Headline.objects.get(pk=headline_id)
    except Headline.DoesNotExist:
        raise Http404
    return render_to_response('news/headline_detail.html', {'headline':headline})

def headline_create(request):
    if request.method == 'POST':
        form = HeadlineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('headlines')
    else:
        form = HeadlineForm()
    return render_to_response('news/headline_create.html', {'form':form}, context_instance=RequestContext(request))

def headline_update(request, headline_id):
    try:
        headline = Headline.objects.get(pk=headline_id)
        if request.method == 'POST':
            form = HeadlineForm(request.POST, instance=headline)
            if form.is_valid:
                form.save()
                return redirect('headline_detail', headline_id)
        else:
            form = HeadlineForm(instance=headline)
        return render_to_response('news/headline_update.html', {'form':form}, context_instance=RequestContext(request))
    except Headline.DoesNotExist:
        raise Http404

def headline_delete(request, headline_id):
    try:
        headline = Headline.objects.get(pk=headline_id)
        headline.delete()
        return render_to_response('news/headline_delete.html')
    except Headline.DoesNotExist:
        raise Http404