# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django import template
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404, get_list_or_404
from gba.models import *
from django.template.context import RequestContext
import datetime, unicodedata
import guestbook.settings

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
