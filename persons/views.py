from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from persons.models import Home,Picture
from django.template import loader,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.forms import ModelForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import HomeForm,ImageForm


class State:
    def __init__(self,name):
        self.name = name
        self.citis = []
lorestan = State("lorestan")
lorestan.citis = ["noorabad","dorood","alashtar","broojerd"]
khoozestan = State("khoozestan")
khoozestan.citis = ["ahvaz","shooshtar","dezfull","behbahan"]

# khoozestan = State("khoozestan","shooshtar,ahvaz,dezfull")
# esfahan = State("esfahan","dorche,najafabad,vilashahr")

# iran = [lorestan,khoozestan,esfahan]
iran = [lorestan,khoozestan]



#-------------------------------------------------------------------#
@login_required
def addHome(request):
    current_user = request.user

    template_name='persons/add_home.html'

    form1 = HomeForm(request.POST or None, request.FILES or None)
    form2 = ImageForm(request.POST or None, request.FILES or None)
    if form1.is_valid():
        print("#############################################################")
        # print("state is: "+request.POST.get('s'))
        print("#####################################################")
        # print("shahrestan is: "+request.POST.get('c'))
        print("#####################################################")
        if form2.is_valid():
            _home=form1.save(commit=False)
            _image=form2.save(commit=False)
            _home.member_id= current_user.id
            _home.shahrestan= request.POST.get('c')
            _home.save()
            _image.homeid= _home
            _image.save()
            return redirect('persons:show_homes')
    context={
        "form1":form1,
        "form2":form2,
        "iran":iran,
                }

    return render(request,template_name,context)



#-------------------------------------------------------------------#
@login_required
def yourHomes(request):
	current_user = request.user
	#f = User.objects.filter(pk=h.member_id)

	_yourHomes= Home.objects.filter(member_id=current_user.id) 
	template_name='persons/yourHomes.html'

	return render(request,template_name,{'yourHomes':_yourHomes})
	


#@login_required
def showHome(request):
	current_user = request.user
	template_name = 'persons/showHome.html'
	images = Picture.objects.all().distinct('homeid')
	
	return render(request,template_name,{'images':images,'user':current_user})



def detail_home(request,home_id):
    h = Home.objects.get(pk=home_id)
    f = User.objects.get(pk=h.member_id)
    im_of_this_house = Picture.objects.filter(homeid=home_id).order_by('-timestamp')
    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        _image=form.save(commit=False)
        _image.homeid=h
        _image.save()
    return render(request,'persons/detail_home.html',{'home':h,'owner':f,'pictures':im_of_this_house,'form':form})

def detail_user(request,user_id):
	user = User.objects.get(pk=user_id)
	return render(request,'persons/detail_user.html',{'u':user})

def home_delete(request,home_id = None):
    instance = get_object_or_404(Home,id=home_id)
    instance.delete()
    messages.success(request,"deleted")
    return redirect("persons:show_homes")

def home_update(request,home_id = None):
    instance = get_object_or_404(Home,id=home_id)
    form = HomeForm(request.POST or None,instance = instance)
    if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())

    context = {
            "instance": instance,
            "form":form,
        }
    template_name = 'persons/home_update.html'
    return render(request, template_name, context)
def delete_image(request,img_id = None):
    img = get_object_or_404(Picture,id=img_id)
    p = img.homeid
    print(img.get_absolute_url())
    img.delete()
    return HttpResponseRedirect(img.get_absolute_url())