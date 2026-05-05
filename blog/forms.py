from django import forms

class GetArticleQueryForm(forms.Form):
    search = forms.CharField(max_length=60, min_length=3)
    limit  = forms.IntegerField(max_value=200, min_value=1, required=False)
    offset = forms.IntegerField(min_value=0, required=False)


    def clean_search(self):
        data = self.cleaned_data
        return data['search'].lower()
    

class CreateArticleForm(forms.Form):
    title = forms.CharField(max_length=100, min_length=3)
    content = forms.CharField(max_length=5000, min_length=10)

    