from Checkout.models import Project_Creation
from App.models import Initial_Data, Pkg_Form_Data



def Find_Product(Id):
    try:
        List_Product =[]
        Product = Project_Creation.objects.all().filter(Product_Id = int(Id)).values("is_Completed").last()["is_Completed"]
        if Product == False:
            Data = Pkg_Form_Data.objects.all().filter(Gig_Id = int(Id))
            Init_Data =Initial_Data.objects.all().filter(id = int(Id)) 
            Projcet_Type = Project_Creation.objects.all().filter(Product_Id = int(Id)).values("Product_Type").last()["Product_Type"]
            List_Product.append([Init_Data,Data, Projcet_Type])
            return List_Product
        else:
            return None
    except:
        return None

def Find_Legit_User_Offer(Product, User):
    try:
        Project_ID_Created_For = Project_Creation.objects.all().filter(Product_Id = Product).values("Created_For").last()["Created_For"]
        Project_ID_Created_by = Project_Creation.objects.all().filter(Product_Id = Product).values("Created_By").last()["Created_By"]

        #Advertiser = Project_ID[-1]["Created_By"]
        #Influencer = Project_ID[-1]["Created_For"]
        if Project_ID_Created_by == User:
            return "Adv"
        elif Project_ID_Created_For == User:
            return "Inf"
        else:
            return None
    except:
        return None
