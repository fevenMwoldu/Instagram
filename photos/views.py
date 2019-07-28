from django.shortcuts import render
from django.http  import HttpResponse,HttpResponseRedirect
from . models import Image, Profile
from .forms import photoForm, ProfileForm, ImageForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user

    if not Profile.user_has_profile(current_user.id):
        return HttpResponseRedirect('profile')

    photos = Image.objects.all()
    return render(request, 'index.html',{"photos" : photos})


@login_required(login_url='/accounts/login/')
def posts(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"index.html")

@login_required(login_url='/accounts/login/')
def new_posts(request):
    current_user = request.user
    if request.method == 'POST':
        form = photoForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image = current_user
            image.save()
        # return redirect('newsToday')

    else:
        form = photoForm()
    return render(request, 'new_post.html', {"form": form})


@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'add_profile.html', {"form": form})


@login_required(login_url='/account/login/')
def add_image(request):
    print('add_image is called ....')
    current_user = request.user
    form = ImageForm()
    
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.Likes = 0
            image.profile = Profile.objects.filter(user_id = current_user.id).first()
            image.save()
            print('Saved image {}'.format(image))
    
            return HttpResponseRedirect('/')
        
    return render(request, 'add_image.html', {"form": form})
