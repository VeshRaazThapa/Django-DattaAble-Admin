# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from app import models
from app.forms import MemberInfoForm
from django.http import HttpResponseRedirect

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
        context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    # try:
        
        load_template = request.path.split('/')[-1]
        # context['segment'] = load_template

        if 'member_table' in load_template:
            context['membersinfo'] = models.MemberInfo.objects.all()
            load_template = 'ui-tables.html'

        if 'add_members' in load_template:
            load_template = 'ui-forms.html'
            #custom membermodel
            context['member_form'] = MemberInfoForm
            if request.method == 'POST':
                memberform = MemberInfoForm(request.POST)
                if memberform.is_valid():
                    memberform.save()
                    return HttpResponseRedirect('index.html')
            else:
                memberform = MemberInfoForm()

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))
        
    # except template.TemplateDoesNotExist:
    #
    #     html_template = loader.get_template( 'page-404.html' )
    #     return HttpResponse(html_template.render(context, request))

    # except :
    #
    #     html_template = loader.get_template( 'page-500.html' )
    #     return HttpResponse(html_template.render(context, request))

# def member_table (request):
#     context = {}
#
#     load_template = request.path.split('/')[-1]
#     context['segment'] = load_template
#     html_template = loader.get_template('ui-tables.html')
#     return HttpResponse(html_template.render(context, request))