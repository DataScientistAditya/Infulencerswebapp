from django.urls import path
from . import views

urlpatterns = [
    path("<int:offerid>", views.ReleaseRequest, name="ReleaseRequest"),
]