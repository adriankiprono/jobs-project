from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required




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

