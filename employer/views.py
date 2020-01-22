from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse,Http404



# Create your views here.
def index(request):
    applicant=Applicant.objects.all()
    return render(request,'index.html',locals())


def search_results(request):
    
    if 'applicant' in request.GET and request.GET["applicant"]:
        search_term = request.GET.get("applicant")
        searched_applicants = Applicant.search_by_jobs(search_term)
        message = f"{search_term}"

        return render(request, 'all-jobs/search.html',{"message":message,"applicants": searched_applicants})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-jobs/search.html',{"message":message})

