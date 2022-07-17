from django.shortcuts import render, get_object_or_404
from jobs.models import Job

def jobs(request):
    jobs = Job.objects
    return render(request, 'jobs/jobs.html', {'jobs':jobs})

def jobpage(request, jobs_id):
    jobpage = get_object_or_404(Job, pk=jobs_id)
    return render(request, 'jobs/jobpage.html', {'job':jobpage})