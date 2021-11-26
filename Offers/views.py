from django.shortcuts import redirect, render
from django.http.response import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from .models import Offer_Details, Earned_by_Freelancer
from .forms import Project_Submit_Form, Chat_Text_Form
from .Backend import Find_Product, Find_Legit_User_Offer
from Checkout.models import Project_Creation
from App.models import Account, Pkg_Form_Data
from notifications.signals import notify

# Create your views here.
def Offer(request, id):
    User_Id = request.user.id
    Is_User = Find_Legit_User_Offer(Product=id, User=User_Id)
    if Is_User is not None:
        Detail = Find_Product(Id=id)
        result = request.GET.get('result', None)
        Offer_Id = request.GET.get('offer', None)
        Amount_Change = request.GET.get('amnt', None)
        print('Offer_id is',Offer_Id)
        print('result is',result)
        print("Chab=nge Amount id is",Amount_Change)
        if result is not None:
            Project_Creation.objects.filter(Product_Id = int(id)).update(Is_Realesed_Requested = True, is_Completed = True)
            Released_Money_To = Project_Creation.objects.filter(Product_Id = int(id) ).values("Created_For").last()["Created_For"]
            Released_Money_From = Project_Creation.objects.filter(Product_Id = int(id)).values("Created_By").last()["Created_By"]
            Amount = int(result)
            Earned_Obj = Earned_by_Freelancer(Money_Reciever = Released_Money_To, Money_Releser = Released_Money_From, Value =Amount)
            Earned_Obj.save()
            User_Receiver = Account.objects.get(id = int(Released_Money_To))
            notify.send(request.user,recipient= User_Receiver , verb= "{} Have Released Money".format(request.user.username),description ="{} Has Released Money".format(request.user.username) )
        if Offer_Id is not None:
            Update_Is_Url = Project_Creation.objects.all().filter(Product_Id = int(Offer_Id)).values("Is_Realesed_Requested").last()["Is_Realesed_Requested"]
            if Update_Is_Url == False:
                Project_id = Project_Creation.objects.all().filter(Product_Id = id).values("id").last()["id"]
                Project_Creation.objects.all().filter(id = Project_id).update(Is_Realesed_Requested = True)
                Released_Money_From = Project_Creation.objects.filter(Product_Id = int(id)).values("Created_By").last()["Created_By"]
                User_Request_Release_Rcvr = Account.objects.get(id = int(Released_Money_From))
                notify.send(request.user,recipient= User_Request_Release_Rcvr , verb= "{} Has Requested to Release Money".format(request.user.username))
        if request.method == "POST":
            Project_Sub = Project_Submit_Form(request.POST)
            if Project_Sub.is_valid():
                Prf_Url = Project_Sub.cleaned_data["Proof_Url"]
                Prf_Url_sc = Project_Sub.cleaned_data["Proof_Url_Scnd"]
                Prf_Url_thrd = Project_Sub.cleaned_data["Proof_Url_Third"]
                print("Url 1 is ",Prf_Url)
                Proj_Id = Project_Creation.objects.filter(Product_Id = int(id))[0]
                #try:
                ofr_obj = Offer_Details(Proof_Url = Prf_Url,Proof_Url_Scnd = Prf_Url_sc, Proof_Url_Third = Prf_Url_thrd, Project_Id = Proj_Id, Messege = "N/A" )
                ofr_obj.save()
                return redirect("/Gig")
                #except:
                    #ofr_obj = None
                    #pass
            else:
                return render(request,"Project.html",{"Prg_form":Project_Sub,"Data":Detail,"offer_id":id,"Error":"Somthing Went Wrong","Type_User":Is_User,"Type_Proj":Detail[0][2]})
        else:
            Project_Sub = Project_Submit_Form()
            return render(request,"Project.html",{"Prg_form":Project_Sub,"Data":Detail,"offer_id":id,"Type_User":Is_User,"Type_Proj":Detail[0][2]})
    else:
        return HttpResponseBadRequest()


def ReleasePayment(request):
    result = request.GET.get('result', None)
    print('result is',result)
    if result is not None:
        print(result)
    return JsonResponse('Data', safe=False)
