from django.shortcuts import redirect, render
from .form import ReleaseReqForm
from Offers.models import Offer_Details
from Checkout.models import Project_Creation
from App.models import Account
from notifications.signals import notify

# Create your views here.
def ReleaseRequest(request,offerid ):
    if request.method == "POST":
        Rel_Form = ReleaseReqForm(request.POST)
        Project_id = int(offerid)
        Proj_Id = Project_Creation.objects.filter(Product_Id = Project_id)[0]
        print(Proj_Id)
        if Rel_Form.is_valid():
            Url1 = Rel_Form.cleaned_data["Completion_Url"]
            Url2 = Rel_Form.cleaned_data["Completion_Url_Sc"]
            Url3 = Rel_Form.cleaned_data["Completion_Url_Thr"]
            Msg = Rel_Form.cleaned_data["Messege"]
            print(Url1)
            Ofr_Obj = Offer_Details(Project_Id = Proj_Id,Proof_Url = Url1, Proof_Url_Scnd =Url2, Proof_Url_Third = Url3, Messege =Msg )
            Ofr_Obj.save()
            Project_Creation.objects.all().filter(Product_Id = Project_id).update(Is_Realesed_Requested = True)
            Released_Money_From = Project_Creation.objects.filter(Product_Id = Project_id).values("Created_By").last()["Created_By"]
            User_Receiver = Account.objects.get(id = int(Released_Money_From))
            Update_Is_Url = Project_Creation.objects.all().filter(Product_Id = Project_id).values("Is_Proof_Url").last()["Is_Proof_Url"]
            if Update_Is_Url == False:
                Project_id = Project_Creation.objects.all().filter(Product_Id = Project_id).values("id").last()["id"]
                Project_Creation.objects.all().filter(id = Project_id).update(Is_Proof_Url = True)
            notify.send(request.user,recipient= User_Receiver , verb= "{} Has Updated Urls for Completing the Projects".format(request.user.username))
            return redirect("All_Adv")
        else:
            Rel_Form = ReleaseReqForm()
            return render(request, 'Release.html',{"Rel_Form":Rel_Form,"Error":"Need First Url as Input"})
    else:
        Rel_Form = ReleaseReqForm()
    return render(request, 'Release.html',{"Rel_Form":Rel_Form})