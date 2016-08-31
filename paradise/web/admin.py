from django.contrib import admin

from .models import Product, Review, Announcement

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('product', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']

class AnnouncementAdmin(admin.ModelAdmin):
    model = Announcement
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']

admin.site.register(Product)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Review, ReviewAdmin)
