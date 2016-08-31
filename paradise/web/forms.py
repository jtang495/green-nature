#from django import forms
from django.forms import ModelForm, Textarea
from web.models import Review
#from tinymce.widgets import TinyMCE

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }


#class ProductForm(ModelForm):
#    class Meta:
#        model = Wine
#        fields = ["image"]
        
#class AnnouncementForm(ModelForm):
#    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
#    class Meta:
#        model = Announcement
#        
 
        
    