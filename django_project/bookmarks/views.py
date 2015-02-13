# -*- coding: utf-8 -*- 
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext
from bookmarks.forms import *

def main_page(request):
        
#     template = get_template('main_page.html')
#     variables = Context({
#         'user':request.user
#     })
#     
#     output = template.render(variables)
#     return HttpResponse(output)
    bookmarks = ''
    
    if request.user.username :
        us = User.objects.get(username=request.user.username)
        bookmarks = us.bookmark_set.all()
        
    return render_to_response(
        'main_page.html',RequestContext(request,{'username':request.user.username,'bookmarks':bookmarks})
    )
    

def user_page(request,username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('사용자를 찾을 수 없습니다.')
    
    bookmarks = user.bookmark_set.all()
    
    template = get_template('user_page.html')
    variables = RequestContext(request,{
        'username':username,
        'bookmarks':bookmarks
    })
    
    return render_to_response('user_page.html',variables)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST) 
        if form.is_valid():
            user = User.objects.create_user( 
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password1'], 
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/') 
    else:
        form = RegistrationForm()
    
    variables = RequestContext(request, {
        'form': form 
    })
    
    return render_to_response('registration/register.html',variables )
