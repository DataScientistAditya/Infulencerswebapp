from django.shortcuts import redirect, render
from Checkout.models import Project_Creation
from .form import Amountchangeform
from .models import AmountChange
from notifications.signals import notify
from App.Utility import Get_Recipent_User
from App.models import Account
# Create your views here.


def AmountChangeRequest(request, Amountid):
    Project_Id = int(Amountid)
    if request.method == "POST":
        Amnt_Form = Amountchangeform(request.POST)
        if Amnt_Form.is_valid():
            Amnt = Amnt_Form.cleaned_data["Amount"]
            Msg = Amnt_Form.cleaned_data["Messege"]
            Proj_Id = Project_Creation.objects.filter(Product_Id = Project_Id)[0]
            
            Amnt_Obj = AmountChange(Project_Id = Proj_Id,Change_Amount = Amnt,Meesege = Msg,is_Approved = False )
            Amnt_Obj.save()
            try:
                Created_For_User = Project_Creation.objects.all().filter(Created_For = request.user.id)
            except:
                Created_By_User = Project_Creation.objects.all().filter(Created_By = request.user.id)
            if Created_For_User is not None:
                User_Receiver_Id = Project_Creation.objects.all().filter(Product_Id =Project_Id).values("Created_By")[0]["Created_By"]
                User_Receiver = Account.objects.filter(id = User_Receiver_Id)[0]
                notify.send(request.user,recipient= User_Receiver , verb= "{} Has Requested to Change Amount".format(request.user.username) + f'''<a href ="/Approval/{Amountid}">Approve</a>''')
            elif Created_By_User is not None:
                User_Recv_Id = Project_Creation.objects.all().filter(Product_Id =Project_Id).values("Created_For")[0]["Created_For"]
                User_Recvr = Account.objects.filter(id = User_Recv_Id)[0]
                notify.send(request.user,recipient= User_Recvr , verb= "{} Has Requested to Change Amount".format(request.user.username) + f'''<a href ="/Approval/{Amountid}">Approve</a>''')
            return redirect("All_Adv")
        else:
            Amnt_Form = Amountchangeform()
            return render(request,'Amountchange.html',{"Rel_Form":Amnt_Form,"Error":"Need First Url as Input"})
    else:
        Amnt_Form = Amountchangeform()
    return render(request,'Amountchange.html',{"Rel_Form":Amnt_Form})
