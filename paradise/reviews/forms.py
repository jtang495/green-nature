from django.forms import ModelForm, Textarea
from reviews.models import Review, Wine, Announcement

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }


class ProductForm(ModelForm):
    class Meta:
        model = Wine
        fields = ["image"]
        
#class AnnouncementForm(ModelForm):
#    class Meta:
#        model = Announcement
#        fields = ["image1"]
# 
        
    