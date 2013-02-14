# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.template.loader import get_template
from django import template
from sorl.thumbnail.shortcuts import get_thumbnail
import time
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404, get_list_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from gba.models import *
from django.template.context import RequestContext
from django.core.files.base import ContentFile
import datetime, unicodedata
import guestbook.urls
from gba.forms import AddGuBook, RecaptchaForm

		

def home(request, ording='down', sorting='date', page = 0):
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
			image = cd['image']
			date = datetime.datetime.now()
			record = GuBook(username=username, email=email, homepage=homepage, text=text, ip=ip, browser=browser, date=date, image=image)
			fls = ContentFile(request.FILES['image'].read())
			record.image.save(request.FILES['image'].name, fls)
			resize_fls = get_thumbnail(record.image, '60x80', crop='center', quality=99)
			image = resize_fls.url
			record.save()
			return HttpResponseRedirect('/')
	else:
		form = AddGuBook()
	try:
		sorttype = {
			('up', 'date'): 'date',
			('down', 'date'): '-date',
			('up', 'username'): 'username',
        		('down', 'username'): '-username',
			('up', 'email'): 'email',
        		('down', 'email'): '-email',
		}[(ording, sorting)]
		currentort = {
			'up': 'down',
			'down': 'up',
		}[ording]
	except:
		sorttype = '-date'
		currentort = 'down'
	mesgs = GuBook.objects.all().order_by(sorttype)
	paginator = Paginator(mesgs, 10)
	try:
		page = int(page)
		tbl = paginator.page(page)
	except:
		tbl = paginator.page(1)
	uri = '/' + ording + '/' + sorting + '/'
	return render_to_response('2.html', 
	{
		'form': form,
		'tbl': tbl,
		'ording': currentort,
		'page': page,
		'uri': uri
	}
	)
