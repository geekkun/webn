from django.shortcuts import render
from theapp.models import AppUser, Comments, Likes, Dislikes, Article
from django.http import HttpResponse, Http404
from django.views import generic
from django.template import loader
import hashlib


appname = 'Newspaper'


# Create your views here.
def index(request):
    return render(request, 'theapp/signup.html')

def registerUser(request):
    if 'email' in request.POST:
        email = request.POST["email"]
        password = request.POST["password"]
        name = request.POST["name"]
        phone = request.POST["phone"]
        user = AppUser(username = email, password = password, name = name, phone = phone)
        user.save()
        context = {"Registration has been successful, you can now log in."}
        return render(request, 'theapp/login.html')

# decorator that tests whether user is logged in
def loggedin(f):
    def test(request):
        if 'username' in request.session:
            return f(request)
        else:
            return render(request, 'theapp/not-logged-in.html', {})
    return test

def login(request):
    if 'username' not in request.POST:
        context = { 'appname': appname }
        return render(request, 'theapp/login.html', context)
    else:
        u = request.POST['username']
        p = hashlib.sha224((request.POST['password']).encode('utf-8')).hexdigest()
        try:
            member = AppUser.objects.get(pk=u)
        except AppUser.DoesNotExist:
            return HttpResponse("User does not exist")
        if p == member.password:
            request.session['username'] = u;
            request.session['password'] = p;
            return render(request, 'theapp/login.html', {
                'appname': appname,
                'username': u,
                'loggedin': True}
            )
        else:
            print (p)
            return HttpResponse("Wrong password test")

@loggedin
def logout(request):
    if 'username' in request.session:
        u = request.session['username']
        request.session.flush()
        context = {
            'appname': appname,
            'username': u
        }
        return render(request, 'theapp/logout.html', context)
    else:
        raise Http404("Can't logout, you are not logged in")

def logCheckUser(request):
    if 'username' in request.POST:
        u = request.POST['username']
        try:
            member = AppUser.objects.get(pk=u)
            return HttpResponse("<span class='available'>&nbsp;&#x2714; Valid username</span>")
        except AppUser.DoesNotExist:
            return HttpResponse("<span class='taken'>&nbsp;&#x2718; Unknown username</span>")
    else:
        return HttpResponse("")

    
class NewsListView(generic.ListView):
    model = Article
    context_object_name = "articles"
    queryset = Article.objects.all()
    template_name = "news.html"

    def news(request):
        template = loader.get_template('news.html')
        articles = Article.objects.all()
        context = {
            'articles': articles
        }
        return HttpResponse(template.render(context,request))

    def sport(request):
        template = loader.get_template('news.html')
        articles = Article.objects.filter(category="Sport")
        context = {
            'articles': articles
        }
        return HttpResponse(template.render(context, request))

    def business(request):
        template = loader.get_template('news.html')
        articles = Article.objects.filter(category='SP')
        context = {
            'articles': articles
        }
        return HttpResponse(template.render(context, request))
