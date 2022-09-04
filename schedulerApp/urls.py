from django.urls import path
from .views import (SchedulerApiView)

urlpatterns = [
    path('request', SchedulerApiView.as_view(), name='index'),
]