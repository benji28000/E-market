from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=['title','category','quantité','prix','description','image']
        labels={'title':'Titre', 'category':'Catégorie','quantité':'quantité','description':'Description','prix':'prix'}
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'quantité':forms.NumberInput(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','rows':5}),
            'prix':forms.NumberInput(attrs={'class': 'form-control'})
        }

