# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.template.loader import get_template
from django import template
import time
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404, get_list_or_404
from gba.models import *
from django.template.context import RequestContext
import datetime, unicodedata
import guestbook.settings
from gba.forms import AddGuBook

def gen_color(n):
	color = {
	0:'white',
	1:'gray',
	}
	return color[n]

def home(request):
	t = GuBook.objects.all()
	l = [obj.lst() for obj in t]
#	t =[[1111111,2222,333333333,555555555], [222,444,6666,7]]
	s = [gen_color(i%2) for i in xrange(len(t))]
        return render_to_response('1.html',
        {
		'd': list(zip(s, l))
        }
        )


def add(request):
	if request.method == 'POST':
		form = AddGuBook(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			username = cd['username']
                        email = cd['email']
                        homepage = cd['homepage']
                        text = cd['text']
			ip = request.META['REMOTE_ADDR']
			browser = request.META['HTTP_USER_AGENT']
			date = datetime.datetime.now()
			record = GuBook(username=username, email=email, homepage=homepage, text=text, ip=ip, browser=browser, date=date)
			record.save()
			return HttpResponseRedirect('/')
	else:
		form = AddGuBook()
	t = GuBook.objects.all()
	l = [obj.lst() for obj in t]
	s = [gen_color(i%2) for i in xrange(len(t))]
	return render_to_response('2.html', 
	{
		'form': form
	}
	)
