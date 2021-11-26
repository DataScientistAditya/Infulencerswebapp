from django import forms

class Amountchangeform(forms.Form):
    Amount = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Enter Revised Amount in $","class":"form-control" ,"label":"Amount"}))
    Messege = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"Any Additional messege you want to send","class":"form-control"  ,"cols":"30" ,"rows":"7","label":"Messege(Optional)"}) )