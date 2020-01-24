from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from .forms import NewJobForm,ProfileForm,UserForm
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    applicant=Applicant.objects.all()
    return render(request,'index.html',locals())


def search_results(request):
    
    if 'applicant' in request.GET and request.GET["applicant"]:
        search_term = request.GET.get("applicant")
        searched_applicant = Applicant.search_by_job(search_term)
        message = f"{search_term}"

        return render(request, 'all-jobs/search.html',{"message":message,"applicant": searched_applicant})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-jobs/search.html',{"message":message})


def applicant(request,applicant_id):
    try:
        applicant = Applicant.objects.get(id = applicant_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-job/job.html", locals())

@login_required(login_url='/accounts/login/')
def new_applicant(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewJobForm(request.POST, request.FILES)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.user = current_user
            applicant.save()
        return redirect('index')

    else:
        form = NewJobForm()
    return render(request, 'new_applicant.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile_update(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            my_user_form = user_form.save(commit=False)
            my_profile_form = profile_form.save(commit=False)
            my_profile_form.user_id = request.user.id
            my_profile_form.save()
            my_user_form.save()
            messages.success(request, f'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, f'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm()
    forms= {
        'user_form': user_form,
        'profile_form': profile_form
        }
    
    return render(request,'profile/profile_update.html',forms)

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id = request.user.id)
    images = request.user.applicant_set.all()
    user_x=User.objects.get(id=request.user.id)
    applicant = Applicant.objects.all()
    print(applicant)
    return render(request,'profile/profile.html',locals())


