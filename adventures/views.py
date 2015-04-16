from django.shortcuts import render, render_to_response, redirect

from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required

from django.http.request import HttpRequest

from django.conf import settings

# csrf
from django.core.context_processors import csrf

from adventures.models import *

# Create your views here.
def home(request):
  args = {}
  args.update(csrf(request))
  args['user'] = request.user
  return render_to_response('pages/index.html',args)

def adventures(request):
  args = {}
  args.update(csrf(request))
  args['user'] = request.user
  args['trips'] = Trips.objects.all()
  return render_to_response('pages/adventures.html',args)

def package(request, path):
  args = {}
  args.update(csrf(request))
  args['user'] = request.user
  if path:
    return render_to_response('pages/packages/'+path+'.html',args)
  return render_to_response('pages/packages.html',args)

def packages(request):
  args = {}
  args.update(csrf(request))
  args['user'] = request.user
  return render_to_response('pages/packages.html',args)

def chart(request):
  args = {}
  args.update(csrf(request))
  args['user'] = request.user
  return render_to_response('pages/chart.html',args)

def about(request):
  args = {}
  args.update(csrf(request))
  args['user'] = request.user
  return render_to_response('pages/about.html',args)

def faq(request):
  args = {}
  args.update(csrf(request))
  args['user'] = request.user
  return render_to_response('pages/faq.html',args)

def contact(request):
  args = {}
  args.update(csrf(request))
  args['user'] = request.user
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

def terms(request):
  args = {}
  args.update(csrf(request))
  args['user'] = request.user
  return render_to_response('pages/terms.html',args)

def register(request):
  args = {}
  args.update(csrf(request))
  args['user'] = request.user
  if request.method == 'POST':
    form = request.POST
    user = AdventureUser()
    django_user = User.objects.create_user(form['email'], form['email'], form['password'])
    django_user.save()
    user.django_user = django_user
    user.first_name = form['m_field_id_1']
    user.last_name = form['m_field_id_2']
    
    user.street_address = form['m_field_id_3']
    user.city = form['m_field_id_4']
    user.state = form['m_field_id_5']
    user.zipcode = form['m_field_id_6']
    
    user.bday_month = form['bday_m']
    user.bday_day = form['bday_d']
    user.bday_year = form['bday_y']

    user.gender = form['m_field_id_7']

    user.phone = form['m_field_id_8']
    
    user.found_us = form['m_field_id_9']
    user.allergies = form['m_field_id_10']
    user.save()
    return render_to_response('pages/index.html',args)
  return render_to_response('registration/register.html',args)

def loggin(request):
  args = {}
  args.update(csrf(request))
  args['user'] = request.user
  try:
    if request.method == 'POST':
      form = request.POST
      user = authenticate(username=form['username'], password=form['password'])
      if user is not None:
        auth_login(request, user)
        return redirect('/account')
    elif user.is_authenticated:
      return redirect('/account')
  except Exception as e:
    print(e)
  return render_to_response('registration/login.html',args)

def loggout(request):
  args = {}
  args.update(csrf(request))
  auth_logout(request)
  return redirect('/')

@login_required
def account(request):
  args = {}
  args.update(csrf(request))
  args['user'] = request.user
  adv_user = AdventureUser.objects.filter(django_user=request.user.id)
  trips = UserTrips.objects.filter(user=adv_user)
  args['trips'] = trips
  return render_to_response('pages/account.html',args)
