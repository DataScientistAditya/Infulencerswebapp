from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from django.db.models import fields
from django.forms import Form, widgets
from django.forms.models import ModelForm
from .models import Advertisement_Create


Categories_Choices =(
    ("Select", "Select"),
	("Automotive","Automotive"),
	("Beauty/Cosmetics","Beauty/Cosmetics"),
	("Electronics","Electronics"),
	("Employments/Jobs","Employments/Jobs"),
	("Entertainment","Entertainment"),
	("Fashion","Fashion"),
	("Fitness","Fitness"),
	("Food/Restaurant","Food/Restaurant"),
	("Household","Household"),
	("Media/Publishing","Media/Publishing"),
	("Outdoor","Outdoor"),
	("Software/Technology","Software/Technology"),
	("Sports","Sports"),
 	("Travel","Travel"),
	
)


Audience_CHOICES = (
	("Select", "Select"),
    ("6 and Under", "6 and Under"),
    ("7 to 12", "7 to 12"),
    ("13 to 17", "13 to 17"),
    ("18 to 30", "18 to 30"),
    ("31 to 40", "31 to 40"),
    ("41 to 50", "41 to 50"),
    ("50 and older", "50 and older"),
)

Skills = (
    ("Select","Select"),
	("Instagram Post","Instagram Post"),
	("TikTok - Post","TikTok - Post"),
)

class Advertisement_Form(forms.Form):
    Product_Name = forms.CharField()
    Product_Cost = forms.IntegerField(min_value=0,max_value=60)
    Product_Description = forms.CharField(widget=forms.TextInput(attrs={"maxlength":1800,"minlength":80}))
    Category = forms.ChoiceField(choices=Categories_Choices)
    Subcategories=forms.CharField()
    Audience = forms.ChoiceField(choices=Audience_CHOICES)
    Influencer_Lavel = forms.CharField()
    Target_Country = forms.CharField(widget=forms.TextInput(attrs={"id":"tags","placeholder":"Start Typing......... and Select Autosuggested Country"}))
    Social_Media_Wanted =forms.ChoiceField(choices=Skills)
    Is_Shipping = forms.BooleanField(required=False)
    Product_image = forms.ImageField()



Country_CHOICES = (
	("Select","Select"),
    ("Afghanistan", "Afghanistan"),
    ("Armenia", "Armenia"),
    ("Azerbaijan", "Azerbaijan"),
	("Albania", "Albania"),
	("Andorra", "Andorra"),
	("Austria", "Austria"),
	("Argentina", "Argentina"),
    ("Bahrain", "Bahrain"),
    ("Bangladesh", "Bangladesh"),
    ("Bhutan", "Bhutan"),
    ("Brunei", "Brunei"),
	("Burma", "Burma"),
	("Belarus", "Belarus"),
	("Belgium", "Belgium"),
	("Bulgaria", "Bulgaria"),
	("Bosnia and Herzegovina", "Bosnia and Herzegovina"),
	("Brazil", "Brazil"),
	("Croatia", "Croatia"),
	("Czech Republic", "Czech Republic"),
	("Cambodia", "Cambodia"),
	("Colombia", "Colombia"),
	("China", "China"),
	("Cameroon", "Cameroon"),
	("Cyprus", "Cyprus"),
	("Central African Republic", "Central African Republic"),
	("Canada", "Canada"),
	("Chile", "Chile"),
	("Democratic Republic of the Congo", "Democratic Republic of the Congo"),
	("Denmark", "Denmark"),
	("Egypt", "Egypt"),
	("Ethiopia", "Ethiopia"),
	("Finland", "Finland"),
	("France", "France"),
	("Germany", "Germany"),
	("Greece", "Greece"),
	("Ghana", "Ghana"),
	("Georgia", "Georgia"),
	("Hungary", "Hungary"),
	("India", "India"),
	("Iceland", "Iceland"),
	("Ireland", "Ireland"),
	("Italy", "Italy"),
	("Indonesia", "Indonesia"),
	("Iran", "Iran"),
	("Iraq", "Iraq"),
	("Israel", "Israel"),
	("Japan", "Japan"),
	("Jordan", "Jordan"),
	("Kazakhstan", "Kazakhstan"),
	("Kuwait", "Kuwait"),
	("Kyrgyzstan", "Kyrgyzstan"),
	("Kenya", "Kenya"),
	("Laos", "Laos"),
	("Lebanon", "Lebanon"),
	("Malaysia", "Malaysia"),
	("Morocco", "Morocco"),
	("Mexico", "Mexico"),
	("Nepal", "Nepal"),
	("Norway", "Norway"),
	("Netherlands", "Netherlands"),
	("Pakistan", "Pakistan"),
	("Palestine", "Palestine"),
	("Philippines", "Philippines"),
	("Poland", "Poland"),
	("Portugal", "Portugal"),
	("Romania", "Romania"),
	("Russia", "Russia"),
	("Qatar", "Qatar"),
	("Saudi Arabia", "Saudi Arabia"),
	("Singapore", "Singapore"),
	("South Africa", "South Africa"),
	("South Korea", "South Korea"),
	("Sri Lanka", "Sri Lanka"),
	("Spain", "Spain"),
	("Sweden", "Sweden"),
	("Switzerland", "Switzerland"),
	("Thailand", "Thailand"),
	("Turkey", "Turkey"),
	("United Arab Emirates", "United Arab Emirates"),
	("Uganda", "Uganda"),
	("Ukraine", "Ukraine"),
	("United Kingdom", "United Kingdom"),
	("United States", "United States"),
	("Uruguay", "Uruguay"),
	("Zimbabwe", "Zimbabwe"),
	

)

        
class Ad_Search(forms.Form):
    Search = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"w-full pl-8 pr-2 text-sm text-gray-700 placeholder-gray-600 bg-gray-100 border-0 rounded-md dark:placeholder-gray-500 dark:focus:shadow-outline-gray dark:focus:placeholder-gray-600 dark:bg-gray-700 dark:text-gray-200 focus:placeholder-gray-500 focus:bg-white focus:border-purple-300 focus:outline-none focus:shadow-outline-purple form-input","placeholder":"Search Ads...","id":"tags"}))

class Search_Options(forms.Form):
    Country = forms.ChoiceField(choices=Country_CHOICES)
    Category = forms.ChoiceField(choices=Categories_Choices, required=False)

    


