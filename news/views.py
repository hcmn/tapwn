from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import Http404
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from tapwn.news.models import Headline, Jumbotron
from tapwn.news.forms import HeadlineForm, LoginForm

def login_page(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = "You logged in with success"
                else:
                    message = "Your user is inactive"
            else:
                message = "Invalid username and/or password"
    else:
        form = LoginForm()
    return render_to_response('login.html',{'message':message,'form':form}, context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return redirect('home')

def about(request):
    return render_to_response('about.html')

def home(request):
    headline_list = Headline.objects.all().filter(schedule_content__lte=datetime.now()).order_by("-publication_date")
    right_now = datetime.now()
    jumbotron = Jumbotron.objects.filter(schedule_content_start__lt=right_now, schedule_content_end__gte=right_now).latest("schedule_content_start")
    # from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
    #try:
    #except (ObjectDoesNotExist, MultipleObjectsReturned) as e:
    #    if e is ObjectDoesNotExist:
    #        jumbotron = Jumbotron.objects.get(pk=1)
    #    if e is MultipleObjectsReturned:
    #        jumbotron = Jumbotron.objects.filter(...).latest(...)
    paginator = Paginator(headline_list, 10) # show 2 headlines per page
    notification = ""
    # make sure page request is an int.  If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    # if page request (9999) is out of range, deliver last page of results.
    try:
        headlines = paginator.page(page)
    except (EmptyPage, InvalidPage):
        headlines = paginator.page(paginator.num_pages)
    #return redirect('maintenance')
    return render_to_response('news/home.html', {'right_now':datetime.utcnow(), 'headlines':headlines, 'jumbotron':jumbotron, 'right_now':right_now, 'notification':notification})

def headline_index(request):
    headline_list = Headline.objects.all().order_by("-publication_date")
    paginator = Paginator(headline_list, 2) # show 2 headlines per page
    # make sure page request is an int.  If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    # if page request (9999) is out of range, deliver last page of results.
    try:
        headlines = paginator.page(page)
    except (EmptyPage, InvalidPage):
        headlines = paginator.page(paginator.num_pages)
    return render_to_response('news/headline_index.html', {'headlines':headlines})

def headline_detail(request, headline_id):
    try:
        headline = Headline.objects.get(pk=headline_id)
    except Headline.DoesNotExist:
        raise Http404
    return render_to_response('news/headline_detail.html', {'headline':headline})

@login_required
def headline_create(request):
    if request.method == 'POST':
        form = HeadlineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('headlines')
    else:
        form = HeadlineForm()
    return render_to_response('news/headline_create.html', {'form':form}, context_instance=RequestContext(request))

@login_required
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

@login_required
def headline_delete(request, headline_id):
    try:
        headline = Headline.objects.get(pk=headline_id)
        headline.delete()
        return render_to_response('news/headline_delete.html')
    except Headline.DoesNotExist:
        raise Http404

def maintenance(request):
    return render_to_response('maintenance.html')