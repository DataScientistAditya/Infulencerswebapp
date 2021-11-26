from django.urls import path
from . import views

urlpatterns = [
    path("<Amountid>", views.AmountChangeRequest, name="AmountChangeRequest"),
]