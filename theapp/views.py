from django.shortcuts import render
from theapp.models import AppUser, Comments, Likes, Dislikes
from django.http import HttpResponse, Http404


appname = 'Newspaper'


# Create your views here.
def index(request):
    return render(request, 'theapp/signup.html')

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
        return render(request, 'mainapp/login.html', context)
    else:
        u = request.POST['username']
        p = request.POST['password']
        try:
            member = AppUser.objects.get(pk=u)
        except AppUser.DoesNotExist:
            return HttpResponse("User does not exist")
        if p == member.password:
            request.session['username'] = u;
            request.session['password'] = p;
            return render(request, 'mainapp/login.html', {
                'appname': appname,
                'username': u,
                'loggedin': True}
            )
        else:
            return HttpResponse("Wrong password")

@loggedin
def logout(request):
    if 'username' in request.session:
        u = request.session['username']
        request.session.flush()
        context = {
            'appname': appname,
            'username': u
        }
        return render(request, 'mainapp/logout.html', context)
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
