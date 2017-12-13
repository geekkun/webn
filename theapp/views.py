from django.shortcuts import render, redirect, get_object_or_404
from theapp.models import AppUser, Comments, Likes, Dislikes, Article
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.template import loader
import hashlib
import json


appname = 'Newspaper'


# Create your views here.
def index(request):
    return render(request, 'theapp/signup.html')

def deleteComment(request, comment_id, article_id):
    if 'username' in request.session:
        loggedin = True
        Comments.objects.filter(id=comment_id).delete()
        return redirect("/news/" + article_id)
    else:
        loggedin = False
        return HttpResponse("Login to delete comment")

def postComment(request, article_id):
    if 'username' in request.session:
        loggedin = True
        if request.method == "POST" and 'comment' in request.POST:
            commentToPost = request.POST["comment"]
            userEmail = AppUser.objects.get(pk=request.session['username'])
            article = Article.objects.get(pk=article_id)
            if commentToPost != "":
                comment = Comments(content=commentToPost, article_id=article , user_id=userEmail)
                comment.save()
                return redirect("/news/"+article_id)

            else:
                return HttpResponse("Cannot post empty comment")
        else:
            return HttpResponse("Something went wrong. Try Again.")
    else:
        loggedin = False
        return HttpResponse("Login to post Comments")

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
    email=member.email
    first_name=member.name
    if 'email' in request.POST:
        # if user posted changes. it doesnt have to be username, but username only will do
        first_name = request.POST['fname']
        email = request.POST['email']
        phone = request.POST['phone']
        member.email = email
        member.phone=phone
        member.name=first_name
        if 'new_password' in request.POST:
            new_password = hashlib.sha224((request.POST['new_password']).encode('utf-8')).hexdigest()
            member.password = new_password
        member.save()
        request.session['username']=email
        u=email

    return render(request, 'theapp/profile.html', {
        'appname': appname,
        'username': u,
        'phone' : phone,
        'email_addr':email,
        'first_name':first_name,
        'loggedin': True}
        )
def changePassword(request):
    u = request.session['username']
    member = AppUser.objects.get(pk=u)
    phone=member.phone
    email=member.email
    first_name=member.name
    if 'new_password' in request.POST:
     new_password = hashlib.sha224((request.POST['new_password']).encode('utf-8')).hexdigest()
     member.password = new_password
     member.save()

    return render(request, 'theapp/changePassword.html', {
        'appname': appname,
        'username': u,
        'phone' : phone,
        'email_addr':email,
        'first_name':first_name,
        'loggedin': True,
        'message': 'Your password has been changed'}
        )


    
def news(request):
    template = loader.get_template('theapp/news.html')
    articles = Article.objects.all()
    if 'username' in request.session:
        loggedin = True
    else:
        loggedin = False
    context = {
        'articles': articles,
        'loggedin':loggedin
    }
    return HttpResponse(template.render(context,request))


def checkpassword(request):
    username = request.session['username']
    ip = request.GET['passw']
    entered_password=hashlib.sha224((request.GET['passw']).encode('utf-8')).hexdigest()
    print(entered_password)
    member = AppUser.objects.get(pk=username)
    actual_pass = member.password
    correctPassword = 'False'
    if actual_pass==entered_password:
        correctPassword ='True'
    context = {'list': correctPassword, 'ip' :ip}
    return HttpResponse(json.dumps(context))





def sport(request):
    template = loader.get_template('theapp/news.html')
    articles = Article.objects.filter(category="SP")
    if 'username' in request.session:
        loggedin = True
    else:
        loggedin = False
    context = {
        'articles': articles,
        'loggedin':loggedin
    }
    return HttpResponse(template.render(context, request))

def business(request):
    template = loader.get_template('theapp/news.html')
    articles = Article.objects.filter(category='BS')
    if 'username' in request.session:
        loggedin = True
    else:
        loggedin = False
    context = {
        'articles': articles,
        'loggedin':loggedin
    }
    return HttpResponse(template.render(context, request))

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comm = Comments.objects.filter(article_id=article_id)
    user = None
    likes = None
    dislikes = None
    userLike = None
    userDislike = None
    try:
     likes = Likes.objects.filter(article_id=article_id).count()
     dislikes = Dislikes.objects.filter(article_id=article_id).count()
    except:Likes.DoesNotExist, Dislikes.DoesNotExist
    if 'username' in request.session:
        loggedin = True
        user = AppUser.objects.get(pk=request.session['username'])
        if likes != None or dislikes != None:
         try:
          userDislike = Dislikes.objects.filter(article_id=article_id, user_id=user.email).count()
          userLike= Likes.objects.filter(article_id=article_id, user_id=user.email).count()
         except: Dislikes.DoesNotExist, Likes.DoesNotExist
    else:
        loggedin = False
    return render(request, 'theapp/article.html', {'article': article,
        'loggedin':loggedin, 'comments': comm, 'user':user, 'likes': likes, 'dislikes':dislikes, 'userLike':userLike, 'userDislike':userDislike})

@loggedin
def likeDislike(request):
     likeOrDislike = request.POST['ld']
     username = request.session['username']
     art_id= request.POST['article_id']
     deleted=False
     if likeOrDislike=='like':
         try:
          userLike = Likes.objects.get(article_id=art_id, user_id=username)
          userLike.delete()
          deleted=True
          context = {'list': 'RemoveLike'}
          return HttpResponse(json.dumps(context))
         except:Likes.DoesNotExist
         if not deleted:
          like = Likes(user_id=username, article_id=art_id)
          like.save()
          context = {'list': 'AddLike'}
          return HttpResponse(json.dumps(context))
     else:
         try:
             userDislike = Dislikes.objects.get(article_id=art_id, user_id=username)
             userDislike.delete()
             deleted = True
             context = {'list': 'RemoveDislike'}
             return HttpResponse(json.dumps(context))
         except:Dislikes.DoesNotExist
         if not deleted:
          dislike = Dislikes(user_id=username, article_id=art_id)
          dislike.save()
          context =  {'list':'AddDislike'}
          return HttpResponse(json.dumps(context))
     context = {'list': 'ERROR'}
     return HttpResponse(json.dumps(context))