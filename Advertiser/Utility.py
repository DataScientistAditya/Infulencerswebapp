from .models import Advertisement_Create
from App.models import Account

def Search(Value =None):
    if Value is not None:
        if len(Value)>1:
            try:
                Search = Value[0:3]
                return Search
            except:
                return None
        else:
            return None
    else:
        return None
    
def Get_Ads_Names(Ads_Name):
    try:
        List = []
        Product_List = []
        Data_Obj = []
        Search_Value = Search(Value=str(Ads_Name).lower())
        if Search_Value is not None:
            All_Gigs = Advertisement_Create.objects.all().values("Product_Name")
            for i in All_Gigs:
                List.append(i["Product_Name"])
            
            for j in List:
                String = str(j).lower()
                Found = String.find(Search_Value)
                if Found>-1:
                    Product_List.append(j)
            
            for x in Product_List:
                Data = Advertisement_Create.objects.all().filter(Product_Name = x).values("Product_Name","Product_Description","Category","Subcategories","Audience","Social_Media_Wanted","Influencer_Lavel","Target_Country","Product_image","User","id")
                Data_Obj.append(Data)
                    
            return Product_List, Data_Obj
        else:
            return None
    except:
        return None
    


def Get_User_Advertiser(Ads_id):
    try:
        Advertiser_id = Advertisement_Create.objects.all().filter(id = Ads_id).values("User")[0]["User"]
        Adv = Account.objects.get(id = Advertiser_id)
        return Adv
    except:
        return None
    
    
def Searching_Result(Country = "Select", Category = "Select"):
    if Category != "Select" and Country!="Select":
        try:
            List_Users_Cat = []
            List_User_Unique = []
            List_Users= []
            Data = Advertisement_Create.objects.all().filter(Category = Category).values("User")
            for i in Data:
                List_Users.append(i["User"])
            for x in List_Users:
                if x not in List_User_Unique:
                    List_User_Unique.append(x)
            for j in List_User_Unique:
                Country_User = Advertisement_Create.objects.all().filter(User = j).values("Target_Country")[0]["Target_Country"]
                if Country_User == Country:
                    UserCnt = j
                    #print(UserCnt)
                    Gig_Data_Cat = Advertisement_Create.objects.all().filter(User = UserCnt).filter(Category = Category).values("Product_Name","Product_Description","Category","Subcategories","Audience","Social_Media_Wanted","Influencer_Lavel","Target_Country","Product_image","User","id")
                    #print(Gig_Data_Cat)
                    List_Users_Cat.append(Gig_Data_Cat)
            return List_Users_Cat
        except:
            return None
    else:
        print("Yes")
        try:
            List_Users_Cnt = []
            List_usr_uniq = []
            Cnt_User_Data = Advertisement_Create.objects.all().filter(Target_Country = Country).values("User")
            for x in Cnt_User_Data:
                if x["User"] not in List_usr_uniq:
                    List_usr_uniq.append(x["User"])
            print("User is",Cnt_User_Data)
            for i in List_usr_uniq:
                Gigs_Data_Cnt = Advertisement_Create.objects.all().filter(User = i).values("Product_Name","Product_Description","Category","Subcategories","Audience","Social_Media_Wanted","Influencer_Lavel","Target_Country","Product_image","User","id")
                List_Users_Cnt.append(Gigs_Data_Cnt)
            print("Country Data is",List_Users_Cnt)
            return List_Users_Cnt
        except:
            return None