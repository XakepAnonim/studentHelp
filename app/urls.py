from django.urls import path

from .views import IndexView, ReviewsView, ContactsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('reviews', ReviewsView.as_view(), name='reviews'),
    path('contacts', ContactsView.as_view(), name='contacts'),
]
