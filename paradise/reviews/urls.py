from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
#    url(r'^$', views.review_list, name='review_list'),
    url(r'^$', views.home, name='home'),
    # ex: /review/5/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /wine/
    url(r'^product$', views.wine_list, name='wine_list'),
    # ex: /wine/5/
    url(r'^product/(?P<wine_id>[0-9]+)/$', views.wine_detail, name='wine_detail'),
    url(r'^product/(?P<wine_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
    # ex: /about/
    url(r'^about$', views.about_detail, name='about_detail'),
    url(r'^why$', views.why_detail, name='why_detail'),
    url(r'^faq$', views.faq_detail, name='faq_detail'),

    
]
