""" about/views.py """

from django.shortcuts import redirect
from django.contrib import messages
from .models import Review
from .forms import ReviewForm
from django.views.generic import TemplateView


class AboutView(TemplateView):
    """ View for the About page with review form submission """

    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        """ Pass context data to the template, including reviews
        and the form """
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        context['form'] = ReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        """ Handle review form submission and validation """
        if not request.user.is_authenticated:
            messages.error(request, 'Please log in to submit a review.')
            return redirect('account_login')

        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, 'Your comment has been submitted!')
            return redirect('about')
        else:
            messages.error(request, 'Please fill out all fields.')

        return self.render_to_response(self.get_context_data(form=form))
