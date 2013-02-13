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
from gba.forms import AddGuBook, RecaptchaForm


def home(request, page = 0):
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
	t = GuBook.objects.all().order_by('-date')
	page = int(page)
	if len(t) < page*10 + 10:
		page = 0
		t = t[:10]
	elif page*10<len(t)<page*10 + 10:
		t = t[page*10:]
	else:
		t = t[page*10:page*10+10]
	t = [obj.lst() for obj in t]
	return render_to_response('2.html', 
	{
		'form': form,
		'd': t,
		'page': page
	}
	)
