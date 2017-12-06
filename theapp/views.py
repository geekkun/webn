from django.shortcuts import render, redirect
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
        user = AppUser(email = email, password = hashlib.sha224(password.encode('utf-8')).hexdigest(), name = name, phone = phone)
        user.save()
        mymessage = {"message":"Registration has been successful, you can now log in."}
        return redirect("/login/", context = mymessage)
    else:
        return HttpResponse('Failed')

# decorator that tests whether user is logged in
def loggedin(f):
    def test(request):
        if 'username' in request.session:
            return f(request)
        else:
            return render(request, 'theapp/not-logged-in.html', {})
    return test

def login(request):
    if 'username' in request.session:
        print('user is already logged in')
        return render(request, 'theapp/login.html', {
            'appname': appname,
            'loggedin': True}
                      )

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

@loggedin
def profile(request):
    u = request.session['username']
    member = AppUser.objects.get(pk=u)
    phone=member.phone
    email_addr=member.email
    name=member.name
    # if 'text' in request.POST:
    #     text = request.POST['text']
    #     if member.profile:
    #         member.profile.text = text
    #         member.profile.save()
    #     else:
    #         profile = Profile(text=text)
    #         profile.save()
    #         member.profile = profile
    #     member.save()
    # else:
    #     if member.profile:
    #         text = member.profile.text
    #     else:
    #         text = ""
    print(email_addr)
    return render(request, 'theapp/profile.html', {
        'appname': appname,
        'username': u,
        'phone' : phone,
        'email_addr':email_addr,
        'name':name,
        'loggedin': True}
        )

    
class NewsListView(generic.ListView):
    model = Article
    context_object_name = "articles"
    queryset = Article.objects.all()
    template_name = "theapp/news.html"

    def news(request):
        template = loader.get_template('theapp/news.html')
        articles = Article.objects.all()
        context = {
            'articles': articles
        }
        return HttpResponse(template.render(context,request))

    def sport(request):
        template = loader.get_template('theapp/news.html')
        articles = Article.objects.filter(category="Sport")
        context = {
            'articles': articles
        }
        return HttpResponse(template.render(context, request))

    def business(request):
        template = loader.get_template('theapp/news.html')
        articles = Article.objects.filter(category='SP')
        context = {
            'articles': articles
        }
        return HttpResponse(template.render(context, request))
