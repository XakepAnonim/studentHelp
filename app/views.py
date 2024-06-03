from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class ReviewsView(TemplateView):
    template_name = "reviews.html"


class ContactsView(TemplateView):
    template_name = "contacts.html"
