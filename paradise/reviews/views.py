from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Review, Product, Announcement
from .forms import ReviewForm
import datetime

def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def product_list(request):
    product_list = Product.objects.order_by('-name')
    context = {'product_list':product_list}
    return render(request, 'reviews/product_list.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm()
    return render(request, 'reviews/product_detail.html', {'product': product})

def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        review = Review()
        review.product = product
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('reviews:product_detail', args=(product.id,)))

    return render(request, 'reviews/product_detail.html', {'product': product, 'form': form})
    
def about_detail(request):
    context = {'about_detail':about_detail}
    return render(request, 'reviews/about_detail.html', context)

def faq_detail(request):
    context = {'faq_detail':faq_detail}
    return render(request, 'reviews/faq_detail.html', context)

def why_detail(request):
    context = {'why_detail':why_detail}
    return render(request, 'reviews/why_detail.html', context)

def home(request):
    announcement_list = Announcement.objects.order_by('-pub_date')[:9]
    context = {'announcement_list':announcement_list}
    return render(request, 'reviews/home.html', context)

