from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobs, name='jobs'),
    path('<int:jobs_id>/', views.jobpage, name="jobpage"),
]