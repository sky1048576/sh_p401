from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate
from .forms import ReistrationForm

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core import urlresolvers
from django.http import HttpResponseRedirect


def register(request, ):
    form = ReistrationForm(request.POST or None)

    if form.is_valid():
        new_user = form.save(commit=False)
        # ba dastoore zir mitavan first_name ra ham az inja meghdardehi kard
        # new_user.first_name = "justi"
        new_user.save()
        return redirect('persons:show_homes')
    context = {

        "form": form
    }
    return render(request, "registration/register.html", context)
