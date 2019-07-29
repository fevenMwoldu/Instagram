from django.shortcuts import render
from django.http  import HttpResponse,HttpResponseRedirect
from . models import Image, Profile, Comment
from django.contrib.auth.models import User
from .forms import photoForm, ProfileForm, ImageForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user    

    if not Profile.user_has_profile(current_user.id):
        return HttpResponseRedirect('profile')

    if request.method == 'POST':
        params = request.POST
        image_id = params.get(key="image_id", default=None)
        comment = params.get(key="comment", default=None)

        if comment is not None and image_id is not None:
            image = Image.objects.get(id = image_id)
            profile = Profile.objects.get(user=current_user)
            cmt = Comment(comment=comment, image=image, profile= profile)
            cmt.save_comment()

    photos = Image.objects.select_related().all()
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


def search_results(request):

    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        searched_photos = Image.search_by_imagename(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})


