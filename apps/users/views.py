from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.vary import vary_on_cookie


@vary_on_cookie
def display_profile(request):
    return render_to_response(
        'users/profile.html', context_instance=RequestContext(request))


@vary_on_cookie
def edit_profile(request):
    return HttpResponse('edit profile page')
