from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def root(request):
    return render_to_response('pages/root.html',context_instance=RequestContext(request))
def about(request):
    return render_to_response('pages/about.html',context_instance=RequestContext(request))