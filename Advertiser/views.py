from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .form import Advertisement_Form, Ad_Search,Search_Options
from .models import Advertisement_Create
from django.shortcuts import redirect, render
from App.models import Influencer_Details, Details_Advertiser, Acount_Influencer
from notifications.signals import notify
from App.Utility import Get_Recipent_User
from .Utility import Get_Ads_Names, Get_User_Advertiser, Searching_Result

# Create your views here.


def Create_Advertisement(request):
    if request.method == "POST":
        Product_Form = Advertisement_Form(request.POST,request.FILES)
        if Product_Form.is_valid():
            Name = Product_Form.cleaned_data["Product_Name"]
            Cost = Product_Form.cleaned_data["Product_Cost"]
            Description = Product_Form.cleaned_data["Product_Description"]
            Cat =  Product_Form.cleaned_data["Category"]
            Subs = Product_Form.cleaned_data["Subcategories"]
            Aud = Product_Form.cleaned_data["Audience"]
            Social = Product_Form.cleaned_data["Social_Media_Wanted"]
            Inf_Labl = Product_Form.cleaned_data["Influencer_Lavel"]
            Trg_Cnt = Product_Form.cleaned_data["Target_Country"]
            Img = request.FILES["Product_image"]
            Shipping = Product_Form.cleaned_data["Is_Shipping"]
            User_id = request.user.id
            print(Img)
            print(Trg_Cnt)
            Adv_Obj = Advertisement_Create(User = User_id,Product_Name =Name, Product_Cost = Cost, Product_Description = Description,Category = Cat,Subcategories =Subs,Audience =Aud,Social_Media_Wanted = Social,Influencer_Lavel = Inf_Labl,Target_Country =Trg_Cnt ,Product_image = Img, Is_Shipping = Shipping )
            Adv_Obj.save()
            Recpnt_users = Get_Recipent_User()
            notify.send(request.user,recipient= Recpnt_users, verb= "{} Created a New Advertisement, Check it Out".format(request.user.username))
            return redirect("All_Adv")
        else:
            Product_Form = Advertisement_Form()
            return render(request, "CreateADS.html",{"AdvForm":Product_Form,"Error":"Form is not Valid"})
    else:
        Product_Form = Advertisement_Form()
    return render(request, "CreateADS.html",{"AdvForm":Product_Form})
        
def All_Adv(request):
    if request.session.has_key('uid'):
        usid = request.user.id
        Adv = Acount_Influencer.objects.all().filter(User = usid).values("Is_Hiring_Influencer")[0]["Is_Hiring_Influencer"]
        try:
            User_Name = Influencer_Details.objects.all().filter(User = usid).values("Slug_Name")[0]["Slug_Name"]
            Profile_Pic= Influencer_Details.objects.all().filter(User = usid).values("Profile_Picture")[0]["Profile_Picture"]
            Profile_Pic_Url = "../../media/{}".format(Profile_Pic)
            Profile_Url = "{}_{}".format(usid,User_Name)
        except:
            User_Name = Details_Advertiser.objects.all().filter(User = usid).values("Adv_Slugname")[0]["Adv_Slugname"]
            Profile_Pic= Details_Advertiser.objects.all().filter(User = usid).values("Profile_Picture")[0]["Profile_Picture"]
            Profile_Pic_Url = "../../media/{}".format(Profile_Pic)
            Profile_Url = "{}_{}".format(usid,User_Name)
        if request.method == "POST":
            Ads_frm = Ad_Search(request.POST)
            Search_Form = Search_Options(request.POST)
            if Ads_frm.is_valid():
                Search_Input = Ads_frm.cleaned_data["Search"]
                Search_Data = Get_Ads_Names(Ads_Name=Search_Input)
                try:
                    Search_Values = Search_Data[1][0] 
                except:
                    Search_Values = None
                obj_list =[]
                if Search_Data is not None and Search_Values is not None:
                    for i in Search_Data[1][0]:
                        Image = i["Product_image"]
                        Img_Ul = "../../media/{}".format(Image)
                        obj_list.append([i["Product_Name"],i["Product_Description"],i["Category"],i["Subcategories"],i["Audience"],i["Social_Media_Wanted"],i["Influencer_Lavel"],i["Target_Country"],Img_Ul,i["id"]])
                    return render(request,"Adv.html",{"Context_Gig":obj_list,"Profile_Name":User_Name,"Srch_Ad":Ads_frm,"Search":Search_Form,"Profile_Pic":Profile_Pic_Url,"Profile_Url":Profile_Url,"Adv":Adv})
                else:
                    return render(request,"Adv.html",{"Objs":"No Ads are Available","Profile_Name":User_Name,"Srch_Ad":Ads_frm,"Search":Search_Form,"Profile_Pic":Profile_Pic_Url,"Profile_Url":Profile_Url,"Adv":Adv})
            elif Search_Form.is_valid():
                Cnt= Search_Form.cleaned_data["Country"]
                Cat= Search_Form.cleaned_data["Category"]
                Search_Results = Searching_Result(Country = Cnt, Category = Cat)
                print("Data Is",Search_Results)
                try:
                    Search_data =Search_Results[0]
                except:
                    Search_data = None
                if Search_data is not None :
                    #Attachment_Url_Defs = "../../media/Thunbnail/glass_Full.png"
                    obj_list_ADS =[]
                    for i in Search_Results[0]:
                        img_Url = i["Product_image"]
                        Adv_Img_Urls = "../../media/{}".format(img_Url)
                        obj_list_ADS.append([i["Product_Name"],i["Product_Description"],i["Category"],i["Subcategories"],i["Audience"],i["Social_Media_Wanted"],i["Influencer_Lavel"],i["Target_Country"],Adv_Img_Urls,i["id"]])
                
                    return render(request,"Adv.html",{"Context_Gig":obj_list_ADS,"Profile_Name":User_Name,"Srch_Ad":Ads_frm,"Search":Search_Form,"Profile_Pic":Profile_Pic_Url,"Profile_Url":Profile_Url,"Adv":Adv})
                else:
                    return render(request,"Adv.html",{"Objs":"No Ads are Available","Profile_Name":User_Name,"Srch_Ad":Ads_frm,"Search":Search_Form,"Profile_Pic":Profile_Pic_Url,"Profile_Url":Profile_Url,"Adv":Adv})
            else:
                pass       
        else:
            Ads_frm = Ad_Search()
            Search_Form = Search_Options()
            result = request.GET.get('result', None)
            print(result)
            if result is not None:
                User_Advertiser = Get_User_Advertiser(Ads_id=int(result))
                user_id =request.user.id
                User_Name = Influencer_Details.objects.all().filter(User = user_id).values("Slug_Name")[0]["Slug_Name"]
                Profile_Name = "{}_{}".format(user_id,User_Name)
                notify.send(request.user,recipient= User_Advertiser, verb= "Shown Intrerest For Your Advertisement" + f'''<a href ="/Profile/{Profile_Name}">Visit Profile</a>''')
            List = []
            try:
                All_Advs = Advertisement_Create.objects.all().values("Product_Name","Product_Description","Category","Subcategories","Audience","Social_Media_Wanted","Influencer_Lavel","Target_Country","Product_image","User","id")
                for i in All_Advs:
                    Profile_Image = i["Product_image"]
                    Img_Url = "../../media/{}".format(Profile_Image)
                    List.append([i["Product_Name"],i["Product_Description"],i["Category"],i["Subcategories"],i["Audience"],i["Social_Media_Wanted"],i["Influencer_Lavel"],i["Target_Country"],Img_Url,i["id"]])
                print(List)
                return render(request,"Adv.html",{"Context_Gig":List,"Profile_Name":User_Name ,"Srch_Ad":Ads_frm,"Search":Search_Form,"Profile_Pic":Profile_Pic_Url,"Profile_Url":Profile_Url,"Adv":Adv})
            except:
                return render(request,"Adv.html",{"Objs":"No Ads are Available","Profile_Name":User_Name,"Srch_Ad":Ads_frm,"Search":Search_Form,"Profile_Pic":Profile_Pic_Url,"Profile_Url":Profile_Url,"Adv":Adv})
    else:
        return redirect("/Logout")
    
def Autocomplete(request):
    try:
        Query = request.GET
        Query_Terms = Query.get('term')
        Results = Get_Ads_Names(Ads_Name= Query_Terms)
        if Results is not None:
            Product_Names = Results[0]
            Autocomplete_List = []
            if Product_Names is not None:
                for i in Product_Names:
                    Autocomplete_List.append(i)
                return JsonResponse(Autocomplete_List,safe=False)
    except:
        return JsonResponse([],safe=False)