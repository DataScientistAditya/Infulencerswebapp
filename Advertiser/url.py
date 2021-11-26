from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    
    path("",views.Create_Advertisement,name="CreateAdvertisement"),
    path("All_Adv",views.All_Adv,name="All_Adv"),
    path("<int:id>",views.All_Adv,name="AdsDetails"),
    path('Autocomplete', views.Autocomplete,name='Autocomplete'),
]


    