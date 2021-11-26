from typing import List
from Checkout.models import Project_Creation
from .models import Account, Acount_Influencer, Details_Advertiser, Initial_Data,Influencer_Details
from Offers.models import Earned_by_Freelancer
from Advertiser.models import Advertisement_Create




def Get_Project_Id(Id):
    List =[]

    try:
        Project_Id = Project_Creation.objects.all().filter(Created_For = Id).values("Product_Id","Product_Type","is_Completed")
        if Project_Id is not None:
            for i in range(len(Project_Id)):
                if Project_Id[i]["is_Completed"] == False:
                    List.append([Project_Id[i]["Product_Id"], Project_Id[i]["Product_Type"]])
            
            return List
        else:
            return None
    except:
        return None

def Get_Recipent_User():
    User_Recipent = []
    Id_All = Account.objects.all().values("id")
    for i in range(len(Id_All)):
        User_Recipent.append(Account.objects.get(id = Id_All[i]["id"]))
    return User_Recipent


def Get_Earned_Money(User_Id):
    try:
        List = []
        Dates = []
        Money=[]
        Chart_Data = Earned_by_Freelancer.objects.all().filter(Money_Reciever = User_Id)
        Counter = 0
        for Cht_Data in Chart_Data:
            Dates.append(Counter)
            Money.append(Cht_Data.Value)
            Counter = Counter+1
        return Dates, Money
    except:
        return None


def Get_Spend_Money(User_Id):
    Dates=[]
    Money = []
    try:
        Chart_Data = Earned_by_Freelancer.objects.all().filter(Money_Releser = User_Id)
        Counter = 0
        for Cht_Data in Chart_Data:
            Dates.append(Counter)
            Money.append(Cht_Data.Value)
            Counter = Counter+1
        return Dates, Money
    except:
        return None


def Get_Project_Adv(Id):
    List =[]

    try:
        Project_Id = Project_Creation.objects.all().filter(Created_By = Id).values("Product_Id","Product_Type","is_Completed")
        if Project_Id is not None:
            for i in range(len(Project_Id)):
                if Project_Id[i]["is_Completed"] == False:
                    List.append([Project_Id[i]["Product_Id"], Project_Id[i]["Product_Type"]])
            
            return List
        else:
            return None
    except:
        return None
    

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
    
def Get_Gig_Names(Gig_Name):
    try:
        List = []
        Product_List = []
        Data_Obj = []
        Search_Value = Search(Value=str(Gig_Name).lower())
        if Search_Value is not None:
            All_Gigs = Initial_Data.objects.all().values("Title")
            for i in All_Gigs:
                List.append(i["Title"])
            
            for j in List:
                String = str(j).lower()
                Found = String.find(Search_Value)
                if Found>-1:
                    Product_List.append(j)
            
            for x in Product_List:
                Data = Initial_Data.objects.all().filter(Title = x).values("Title","Category_Service","Descriptions","Date_Created","User","id")
                Data_Obj.append(Data)
                    
            return Product_List, Data_Obj
        else:
            return None
    except:
        return None
        
        
def Get_Influencer():
    List_inf = []
    try:
        Ids = Acount_Influencer.objects.all().filter(Is_Influencer = True).values("User")
        for i in Ids:
            us = Account.objects.all().filter(id=i["User"]).values("username")[0]["username"]
            Slg = Influencer_Details.objects.all().filter(User = i["User"]).values("Slug_Name")[0]["Slug_Name"]
            Slg_id = i["User"]
            prof_url = "{}_{}".format(Slg_id, Slg)
            List_inf.append([us,prof_url])
        return List_inf[0:4]
    except:
        return None
    
def Get_Influencers_by_Search(Inf_Name):
    try:
        List = []
        Product_List = []
        Data_Obj = []
        Search_Value = Search(Value=str(Inf_Name).lower())
        if Search_Value is not None:
            All_Inf = Influencer_Details.objects.all().values("Slug_Name")
            for i in All_Inf:
                List.append(i["Slug_Name"])
            
            for j in List:
                String = str(j).lower()
                Found = String.find(Search_Value)
                if Found>-1:
                    Product_List.append(j)
            
            for x in Product_List:
                Data = Influencer_Details.objects.all().filter(Slug_Name = x).values("Profile_Picture","Descriptions","Country","User")
                Data_Obj.append(Data)
                    
            return Product_List, Data_Obj
        else:
            return None
    except:
        return None
    
    
def Get_Advertisements():
    try:
        List_Ads = []
        All_Gigs = Advertisement_Create.objects.all().values("Product_Name")
        for i in All_Gigs:
            List_Ads.append(i["Product_Name"])
        return List_Ads[0:4]
    except:
        return None
        
def Get_Gigs():
    try:
        Gigs_Data = Initial_Data.objects.all().values("Title","User","id")
        Attachment_Url = "../../media/Thunbnail/glass_Full.png"
        for i in Gigs_Data:
            try:
                Urls = Influencer_Details.objects.all().filter(User = i["User"]).values("Profile_Picture")[0]["Profile_Picture"]
            except:
                Urls =None
            if Urls is not None:
                Profile_Url = "../../media/{}".format(Urls)
                i["image"] = Profile_Url
            else:
                i["image"] = Attachment_Url
        return Gigs_Data[0:4]
    except:
        return None

def Searching_Result(Country = "Select", Category = "Select"):
    if Category != "Select" and Country!="Select":
        try:
            List_Users_Cat = []
            List_User_Unique = []
            List_Users= []
            Data = Initial_Data.objects.all().filter(Category_Service = Category).values("User")
            for i in Data:
                List_Users.append(i["User"])
            for x in List_Users:
                if x not in List_User_Unique:
                    List_User_Unique.append(x)
            for j in List_User_Unique:
                Country_User = Influencer_Details.objects.all().filter(User = j).values("Country")[0]["Country"]
                if Country_User == Country:
                    UserCnt = j
                    print(UserCnt)
                    Gig_Data_Cat = Initial_Data.objects.all().filter(User = UserCnt).filter(Category_Service = Category).values("Title","Category_Service","Descriptions","Date_Created","User","id")
                    print(Gig_Data_Cat)
                    List_Users_Cat.append(Gig_Data_Cat)
            return List_Users_Cat
        except:
            return None
    elif Category == "Select" and Country != "Select":
        try:
            List_Users_Cnt = []
            Cnt_User_Data = Influencer_Details.objects.all().filter(Country = Country).values("User")
            for i in Cnt_User_Data:
                Gigs_Data_Cnt = Initial_Data.objects.all().filter(User = i["User"]).values("Title","Category_Service","Descriptions","Date_Created","User","id")
                List_Users_Cnt.append(Gigs_Data_Cnt)
            return List_Users_Cnt
        except:
            return None
    else:
        return None
    


def Chat_Rooms_Inf(User_Id):
    if User_Id is not None:
        Contact_Inf ={}
        Rooms_inf = []
        try:
            Chat_Rooms = Project_Creation.objects.all().filter(Created_For = User_Id).values("Chat_Room_Name","Created_By")
            for i in range(len(Chat_Rooms)):
                Username = Account.objects.all().filter(id = Chat_Rooms[i]["Created_By"]).values("username")[0]["username"]
                Active = Account.objects.all().filter(id = Chat_Rooms[i]["Created_By"]).values("is_active")[0]["is_active"]
                Prof_Pic = Details_Advertiser.objects.all().filter(User = Chat_Rooms[i]["Created_By"]).values("Profile_Picture")[0]["Profile_Picture"]
                Profile_Url = "../../media/{}".format(Prof_Pic)
                Contact_Inf["Contact"] = Username
                Contact_Inf["Room"] = Chat_Rooms[i]["Chat_Room_Name"]
                Contact_Inf["Status"] = Active
                Contact_Inf["Image"] = Profile_Url
                Rooms_inf.append(Contact_Inf)
            return Rooms_inf
        except:
            return None
    else:
        return None
    
def Chat_Room_Adv(User_id):
    if User_id is not None:
        Contact_Adv = {}
        Rooms_Adv = []
        try:
            Chat_Rooms = Project_Creation.objects.all().filter(Created_By = User_id).values("Chat_Room_Name","Created_For")
            for i in range(len(Chat_Rooms)):
                Username = Account.objects.all().filter(id = Chat_Rooms[i]["Created_For"]).values("username")[0]["username"]
                Active = Account.objects.all().filter(id = Chat_Rooms[i]["Created_For"]).values("is_active")[0]["is_active"]
                Prof_Pic = Influencer_Details.objects.all().filter(User = Chat_Rooms[i]["Created_For"]).values("Profile_Picture")[0]["Profile_Picture"]
                Profile_Url = "../../media/{}".format(Prof_Pic)
                Contact_Adv["Contact"] = Username
                Contact_Adv["Room"] = Chat_Rooms[i]["Chat_Room_Name"]
                Contact_Adv["Status"] = Active
                Contact_Adv["Image"] = Profile_Url
                Rooms_Adv.append(Contact_Adv)
            return Rooms_Adv
        except:
            return None
    else:
        return None
            
        
                    
            
        