# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from forms import RegistrationForm

def root(request):
   # return render_to_response('main/root.html',context_instance=RequestContext(request))
    return render_to_response('main/root.html')
    
def about(request):
    return render_to_response('main/about.html')
  
  
def loggedin(request):
    return render_to_response('main/loggedin.html',
                              {'username': request.user.username})
  
  
def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('complete')

    else:
       # form = UserCreationForm()
        form = RegistrationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('main/registration_form.html', token)

def registration_complete(request):
    return render_to_response('main/registration_complete.html')
    
#from django.shortcuts import render_to_response
#from django.http import HttpResponseRedirect
#from main.forms import CustomUserCreationForm
#from django.core.context_processors import csrf


#def root(request):
   ## return render_to_response('main/root.html',context_instance=RequestContext(request))
    #return render_to_response('main/root.html')
    
#def about(request):
    #return render_to_response('main/about.html')
  
  
#def loggedin(request):
    #return render_to_response('main/loggedin.html',
                              #{'username': request.user.username})
#def register(request):
    #if request.method == 'POST':
        #form = CustomUserCreationForm(request.POST)
        #if form.is_valid():
            #form.save()
            #return HttpResponseRedirect('complete')

    #else:
        #form = CustomUserCreationForm()
    #token = {}
    #token.update(csrf(request))
    #token['form'] = form

    #return render_to_response('main/registration_form.html', token)


#def registration_complete(request):
   #return render_to_response('main/registration_complete.html')
    
    
    
    
    