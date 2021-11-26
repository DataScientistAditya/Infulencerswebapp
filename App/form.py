from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from django.db.models import fields
from django.forms import Form
from django.forms.models import ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

from AmountChangeRequest import form
from .models import Account, Acount_Influencer, Influencer_Details, Usa_Tax_Payer, Gigs, Details_Advertiser
from .backends import AccountAuth


class Register_Forms(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(),validators=[validate_password])
	class Meta:
		model = Account
		fields = ("email", "username", "password")
		label = {

			"email": "Email",
			"username": "Username",
			"password": "Password",

		}



class AccountAuthenticationForm(forms.Form):
    email = forms.EmailField(label="Email", required=True)
    password =  forms.CharField(widget=forms.PasswordInput(), label="Password", required=True)

class Is_Influencer_Form(ModelForm):
	class Meta:
		model = Acount_Influencer
		fields = ("Is_Influencer","Is_Hiring_Influencer")
		label = {

			"Is_Influencer": "I'll Work",
			"Is_Hiring_Influencer": "I'll Hire",

		}
		



class Details_Inf(ModelForm):
	Tiktok_Link = forms.CharField(max_length=500, required=False,widget=forms.TextInput(attrs={"class":"Tiktok_Class", "id":"TikTok", "placeholder":"TikTok Profile Link"}))
	Instagram_Link = forms.CharField(max_length=500, required=False,widget=forms.TextInput(attrs={"class":"Insta_Class", "id":"Insta", "placeholder":"Instagram Profile Link"}))
	Youtube_Link = forms.CharField(max_length=500, required=False,widget=forms.TextInput(attrs={"class":"YouTube_Class", "id":"YouTube", "placeholder":"Youtube Profile Link"}))

	class Meta:
		model = Influencer_Details
		fields = ("First_Name","Last_Name","Profile_Picture","Descriptions","Audience","Country","Tiktok_Link","Instagram_Link","Youtube_Link","Phone_Number")
		label = {

			"First_Name": "First Name",
			"Last_Name": "Last Name",
			"Profile_Picture" : "Profile Picture",
			"Descriptions":"Tell us more about you",
			"Audience":"Audience",
			"Country":"Country",
			"Tiktok_Link":"Tiktok Link",
			"Instagram_Link":"Instagram Link",
			"Youtube_Link":"Youtube Link",
			"Phone_Number":"Phone Number(With Area Code)",
		}


class OTP_form(forms.Form):
	Otp = forms.IntegerField(label="Enter OTP to Verify")



Tax_Clssification_Options = (
	("Individual/sole proprietor or single-member LLC", "Individual/sole proprietor or single-member LLC"),
	("C Corporation", "C Corporation"),
	("S Corporation", "S Corporation"),
	("Partnership", "Trust/estate"),
	("Limited liability company.(corporation)", "Limited liability company.(corporation)"),
	("Limited liability company.(corporation)", "Limited liability company.(corporation)"),
	("Limited liability company.(Partnership)", "Limited liability company.(Partnership)"),
	("Other", "Other "),
)

class USA_W_Nine_Form(ModelForm):
	Federal_tax_classification = forms.ChoiceField(choices=Tax_Clssification_Options, required=True)
	Exempt_payee_code = forms.IntegerField(required=False,widget=forms.NumberInput(attrs={"class":"Payee", "id":"Payee_Id", "placeholder":"Enter Your Exempt payee code (if any)"}))
	Exempt_FATCA_code = forms.CharField(required=False,widget=forms.TextInput(attrs={"class":"FATCA", "id":"FATCA_Id","placeholder":"Enter Your Exempt FATCA code (if any)"}))
	Social_security_number = forms.IntegerField(required=False, widget= forms.NumberInput(attrs={"class":"Ss_Number", "id":"Ss_Number_Id","placeholder":"Enter Your Social security number"}))
	Employer_identification_number = forms.IntegerField(required=False,widget=forms.NumberInput(attrs={"class":"EIN", "id":"EIN_Id","placeholder":"Enter Your Employer identification number"}))
	Signature = forms.CharField(required=False,widget=forms.TextInput(attrs={"class":"Sign", "id":"Sign_Id","placeholder":"By Entering Your Name Here You agreeing that our terms and conditions"}))
	class Meta:
		model = Usa_Tax_Payer
		fields = ("Name","Business_Name","Federal_tax_classification","Exempt_payee_code","Exempt_FATCA_code","Address","City","State","Zip_Code","Social_security_number","Employer_identification_number","Certification","Signature")
		label = {
			"Name":"Name",
			"Business_Name": "Business Name",
			"Federal_tax_classification" : "Select any Federal tax classification of the person whose name is entered",
			"Exempt_payee_code" : "Exempt payee code",
			"Exempt_FATCA_code" : "Exempt FATCA code",
			"Address" : "Address",
			"City": "City",
			"State":"State" ,
			"Zip_Code": "Zip Code",
			"Social_security_number": "Social security number",
			"Employer_identification_number":"Employer identification number",
			"Certification": "Please Check the box before submitting",
			"Signature":"Signature",
		}





Skills = (
    ("Select","Select"),
	("Instagram Post","Instagram Post"),
	("TikTok - Post","TikTok - Post"),
)


Post = (
	("Hours","Hours"),
	("Days","Days"),
	("Week","Week"),
)

Video = (
	("Sec","Sec"),
	("Min","Min"),
	("Hr","Hr"),
)

class Create_Gig_Form_Initial(forms.Form):
	Title = forms.CharField(widget=forms.TextInput(attrs={"class":"input--style-1","id":"Input_id"}),label="Create Your Gig Title")
	Descriptions = forms.CharField(widget=forms.TextInput(attrs={"class":"input--style-1","id":"Input_id_2"}),label="Describe Your Gig", min_length=50, max_length=100)
	Category_Service = forms.ChoiceField(choices=Skills, label="Choose Your Category")
	Search_Tags = forms.CharField(widget=forms.TextInput(attrs={"class":"input--style-1","id":"Input_id_3"}),label="Create Search Tags")
	

class Create_Gig_Form_Pkg(forms.Form):
	Besic_Packages_Name = forms.CharField(widget=forms.TextInput(attrs={"class":"input--style-1","id":"Input_id"}), label="Basic Package Name")
	Standered_Packeges_Name = forms.CharField(widget=forms.TextInput(attrs={"class":"input--style-1","id":"Input_id_2"}), label="Standared Package Name")
	Premium_Packages_Name = forms.CharField(widget=forms.TextInput(attrs={"class":"input--style-1","id":"Input_id_3"}), label="Premium Package Name")

	Besic_Packages_Descriptions = forms.CharField(widget=forms.TextInput(attrs={"class":"input--style-1","id":"Input_id_4"}),label="Basic Package Descriptions",min_length=50, max_length=100)
	Standered_Packeges_Description =forms.CharField(widget=forms.TextInput(attrs={"class":"input--style-1","id":"Input_id_5"}),label="Standared Package Descriptions",min_length=50, max_length=100)
	Premium_Packages_Descriptions = forms.CharField(widget=forms.TextInput(attrs={"class":"input--style-1","id":"Input_id_6"}),label="Premium Package Descriptions",min_length=50, max_length=100)

	Besic_Delivery_Time = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"input--style-1","id":"Input_id_7"}),label="Bascis Package Delivery Time(in Days)", min_value=1)
	Premium_Delivery_Time = forms.IntegerField( widget=forms.NumberInput(attrs={"class":"input--style-1","id":"Input_id_8"}),label="Premium Package Delivery Time(in Days)", min_value=1)
	Standered_Delivery_Time = forms.IntegerField( widget=forms.NumberInput(attrs={"class":"input--style-1","id":"Input_id_9"}),label="Standared Package Delivery Time(in Days)", min_value=1)

	Besic_Packages_Price = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"input--style-1","id":"Input_id_10"}),label="Basic Package Starting Price", min_value=1)
	Standered_Packeges_Price = forms.IntegerField( widget=forms.NumberInput(attrs={"class":"input--style-1","id":"Input_id_11"}),label="Standared Package Starting Price", min_value=1)
	Premium_Packages_Price = forms.IntegerField( widget=forms.NumberInput(attrs={"class":"input--style-1","id":"Input_id_12"}),label="Premium Package Starting Price", min_value=1)
	

	Instagram_Image_to_Feed_Besic = forms.BooleanField(label="Insta Image to Feed",required=False)
	Instagram_Video_to_Feed_Besic = forms.BooleanField(label="Insta Video to Feed Besic",required=False)
	Instagram_Post_to_Story_Besic = forms.BooleanField(label="Insta Post to Story",required=False)
	Instagram_Post_to_Reel_Besic = forms.BooleanField(label="Insta Post to Reel",required=False)
	Instagram_Live_Product_Endorsment_Besic = forms.BooleanField(label="Insta Live Product Endorsment",required=False)
	TikTok_Post_to_Feed_Besic = forms.BooleanField(label="TikTok Post to Feed",required=False)
	TikTok_Post_Product_Review_Video_Besic = forms.BooleanField(label="Tiktok Post Product Review Video",required=False)
	TikTok_Product_Review_Short_Video_Besic = forms.BooleanField(label="TikTok Product Review Short Video",required=False)
	TikTok_Live_Product_Review_Besic = forms.BooleanField(label="TikTok Live Product Review",required=False)

	Instagram_Image_to_Feed_Std = forms.BooleanField(label="Insta Image to Feed",required=False)
	Instagram_Video_to_Feed_Std = forms.BooleanField(label="Insta Video to Feed Besic",required=False)
	Instagram_Post_to_Story_Std = forms.BooleanField(label="Insta Post to Story",required=False)
	Instagram_Post_to_Reel_Std = forms.BooleanField(label="Insta Post to Reel",required=False)
	Instagram_Live_Product_Endorsment_Std = forms.BooleanField(label="Insta Live Product Endorsment",required=False)
	TikTok_Post_to_Feed_Std = forms.BooleanField(label="TikTok Post to Feed",required=False)
	TikTok_Post_Product_Review_Video_Std = forms.BooleanField(label="Tiktok Post Product Review Video",required=False)
	TikTok_Product_Review_Short_Video_Std = forms.BooleanField(label="TikTok Product Review Short Video",required=False)
	TikTok_Live_Product_Review_Std = forms.BooleanField(label="TikTok Live Product Review",required=False)

	Instagram_Image_to_Feed_Prm = forms.BooleanField(label="Insta Image to Feed",required=False)
	Instagram_Video_to_Feed_Prm = forms.BooleanField(label="Insta Video to Feed Besic",required=False)
	Instagram_Post_to_Story_Prm = forms.BooleanField(label="Insta Post to Story",required=False)
	Instagram_Post_to_Reel_Prm = forms.BooleanField(label="Insta Post to Reel",required=False)
	Instagram_Live_Product_Endorsment_Prm = forms.BooleanField(label="Insta Live Product Endorsment",required=False)
	TikTok_Post_to_Feed_Prm = forms.BooleanField(label="TikTok Post to Feed",required=False)
	TikTok_Post_Product_Review_Video_Prm = forms.BooleanField(label="Tiktok Post Product Review Video",required=False)
	TikTok_Product_Review_Short_Video_Prm = forms.BooleanField(label="TikTok Product Review Short Video",required=False)
	TikTok_Live_Product_Review_Prm = forms.BooleanField(label="TikTok Live Product Review",required=False)


	Duration_Post_Besic = forms.IntegerField( widget=forms.NumberInput(attrs={"class":"input--style-1","id":"Input_id_13"}),label="Post Duration", min_value=1,max_value=60,required=False)
	Post_Select_Besic = forms.ChoiceField(choices=Post,required=False)
	Duration_Video_Besic = forms.IntegerField( widget=forms.NumberInput(attrs={"class":"input--style-1","id":"Input_id_14"}),label="Video Duration",min_value=1,max_value=3660,required=False)
	Video_Select_Besic = forms.ChoiceField(choices=Video,required=False)

	Duration_Post_Standared = forms.IntegerField( widget=forms.NumberInput(attrs={"class":"input--style-1","id":"Input_id_15"}),label="Post Duration", min_value=1,max_value=60,required=False)
	Post_Select_Standared = forms.ChoiceField(choices=Post,required=False)
	Duration_Video_Standared = forms.IntegerField( widget=forms.NumberInput(attrs={"class":"input--style-1","id":"Input_id_16"}),label="Video Duration",min_value=1,max_value=3660,required=False)
	Video_Select_Standared = forms.ChoiceField(choices=Video,required=False)

	Duration_Post_Premium = forms.IntegerField( widget=forms.NumberInput(attrs={"class":"input--style-1","id":"Input_id_17"}),label="Post Duration", min_value=1,max_value=60,required=False)
	Post_Select_Premium = forms.ChoiceField(choices=Post,required=False)
	Duration_Video_Premium = forms.IntegerField( widget=forms.NumberInput(attrs={"class":"input--style-1","id":"Input_id_18"}),label="Video Duration",min_value=1,max_value=3660,required=False)
	Video_Select_Premium = forms.ChoiceField(choices=Video,required=False)
	
class Create_Gig_Form_Describe(forms.Form):
	Describe_About_Gig = forms.CharField(min_length=100, max_length=500)

class Create_Gig_Form_Attachment(forms.Form):
	
	Work_Thumbnails = forms.ImageField(label="Upload Thumbnail", widget=forms.FileInput(attrs={"class":"input-file", "id": "my-file"}))
	Attachments = forms.ImageField(label="Upload Your Image/Video", widget=forms.FileInput(attrs={"class":"input-file", "id": "my-file"}))

class Advertiser_details_form(ModelForm):
	class Meta:
		model = Details_Advertiser
		fields = ("First_Name","Last_Name","Profile_Picture",)
		label ={
			"First_Name":"First Name",
			"Last_Name": "Last Name",
			"Profile_Picture": "Profile Picture",

		}

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


class Gigs_Search(forms.Form):
    Search = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"w-full pl-8 pr-2 text-sm text-gray-700 placeholder-gray-600 bg-gray-100 border-0 rounded-md dark:placeholder-gray-500 dark:focus:shadow-outline-gray dark:focus:placeholder-gray-600 dark:bg-gray-700 dark:text-gray-200 focus:placeholder-gray-500 focus:bg-white focus:border-purple-300 focus:outline-none focus:shadow-outline-purple form-input","placeholder":"Search Gigs...","id":"tags"}))
    
class Search_Options(forms.Form):
    Country = forms.ChoiceField(choices=Country_CHOICES)
    Category = forms.ChoiceField(choices=Skills, required=False)
    
    
class Inf_Search(forms.Form):
    Search = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control mr-sm-2","placeholder":"Search Influencers...","id":"tags"}))

  
    
class Reset_Password_Form(forms.Form):
    Email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"placeholder":"Enter Your Registered Email"}))
    
class Reset_Password(forms.Form):
    Password_one = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"placeholder":"Please enter New Password"}))
    Password_two = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"placeholder":"Repeat Password"}))
    
class Reset_Insta_Link(forms.Form):
    Insta_Link = forms.URLField(required=True,widget=forms.URLInput(attrs={"placeholder":"Please Enter your new Insta Link"}))

class Reset_Yt_Link(forms.Form):
    Youtube_Link = forms.URLField(required=True,widget=forms.URLInput(attrs={"placeholder":"Please Enter your new Youtube Link"}))

class Phone_Number_Verify_Form(forms.Form):
    Phone = forms.CharField(required=True, widget=forms.TextInput({"placeholder":"Enter Phone Number with Area code","maxlength":"13","minlength":"13"}))

    
class Approved_Amountchange_Form(forms.Form):
    Approve_Amount_Change = forms.BooleanField()
    

