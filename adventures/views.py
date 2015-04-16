from django.shortcuts import render, render_to_response, redirect

from django.http.request import HttpRequest

from django.conf import settings

# csrf
from django.core.context_processors import csrf

# Create your views here.
def home(request):
  args = {}
  args.update(csrf(request))
  # set arguments for header
  # set arguments for navbar
  #args['nav'] = block_element_variables.set_navbar_variables(request)
  # set arguments for footer
  #args['foot'] = block_element_variables.set_footer_variables(request)
  return render_to_response('pages/index.html',args)

def adventures(request):
  args = {}
  args.update(csrf(request))
  # set arguments for header
  return render_to_response('pages/adventures.html',args)

def package(request, path):
  print("path is"+path)
  args = {}
  args.update(csrf(request))
  # set arguments for header
  if path:
    return render_to_response('pages/packages/'+path+'.html',args)
  return render_to_response('pages/packages.html',args)

def packages(request):
  args = {}
  args.update(csrf(request))
  # set arguments for header
  return render_to_response('pages/packages.html',args)

def chart(request):
  args = {}
  args.update(csrf(request))
  # set arguments for header
  return render_to_response('pages/chart.html',args)

def about(request):
  args = {}
  args.update(csrf(request))
  # set arguments for header
  return render_to_response('pages/about.html',args)

def faq(request):
  args = {}
  args.update(csrf(request))
  # set arguments for header
  return render_to_response('pages/faq.html',args)

def contact(request):
  args = {}
  args.update(csrf(request))
  # set arguments for header
  if request.method == 'POST':
    form = request.POST
    email = form['from']
    subject = form['subject']
    message = form['message']
    print("email: "+email)
    print("subject: "+subject)
    print("message: "+message)
    return render_to_response('pages/contact_successful.html',args)
  return render_to_response('pages/contact.html',args)

def account(request):
  args = {}
  args.update(csrf(request))
  # set arguments for header
  return render_to_response('pages/account.html',args)

def register(request):
  args = {}
  args.update(csrf(request))
  # set arguments for header
  return render_to_response('registration/register.html',args)
