from django import forms

class ReleaseReqForm(forms.Form):
    Completion_Url = forms.URLField(widget=forms.URLInput(attrs={"placeholder":"Paste Url to Prove completion of the Project","class":"form-control" ,"label":"Url"}))
    Completion_Url_Sc = forms.URLField(required=False, widget=forms.URLInput(attrs={"placeholder":"Any other Url","class":"form-control" ,"label":"Url(Optional)"}))
    Completion_Url_Thr = forms.URLField(required=False, widget=forms.URLInput(attrs={"placeholder":"Any other Url","class":"form-control" ,"label":"Url(Optional)"}))
    Messege = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"Any Additional messege you want to send","class":"form-control"  ,"cols":"30" ,"rows":"7","label":"Messege(Optional)"}) )