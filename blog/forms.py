from django import forms

class GetArticleQueryForm(forms.Form):
    search = forms.CharField(max_length=60, min_length=3)
    limit  = forms.IntegerField(max_value=200, min_value=1, required=False)
    offset = forms.IntegerField(min_value=0, required=False)