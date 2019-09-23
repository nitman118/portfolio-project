from django.shortcuts import render
#access to models
from .models import Job
# Create your views here.

def home(request):
    '''
    homepage view
    '''
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs':jobs})
