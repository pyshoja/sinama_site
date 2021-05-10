# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Janer
from .models import Film
from .models import Location
from .models import sans
from .models import Profile


from django.views.generic import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


class firstpageview(LoginRequiredMixin,TemplateView):
    template_name = 'ticket/firstpage.html'

    def get_context_data(self, *args, **kwargs):
        context = super(firstpageview, self).get_context_data(*args, **kwargs)
        context['filmi'] = Film.objects.all()
        return context


class filmlistview(LoginRequiredMixin,ListView):
    template_name = 'ticket/filmlist.html'
    model = Film

    def get_queryset(self, **kwargs):
        query = super().get_queryset(**kwargs)
        film_id = self.kwargs.get('janer_id')
        query = query.filter(name_janer__id=film_id)
        return query


class Tozihfilm(LoginRequiredMixin,DetailView):
    model = Film
    template_name = 'ticket/tozihfilm.html'
    slug_field = 'namber_film'


class Sinama (LoginRequiredMixin,TemplateView):
    template_name = 'ticket/locationlist.html'

    def get_context_data(self, **kwargs):
        context = super(Sinama, self).get_context_data(**kwargs)
        context['local'] = Location.objects.all()
        return context



class Sanslist(LoginRequiredMixin,ListView):
    model = sans
    template_name = 'ticket/sanslist.html'



class aboutview(TemplateView):
    template_name = 'ticket/about.html'

    def get_context_data(self, *args, **kwargs):
        context = super(aboutview, self).get_context_data(*args, **kwargs)
        # context['users'] = YourModel.objects.all()
        return context




from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'ticket/signup.html'


class Profileview(TemplateView):
    template_name = 'ticket/profile.html'

    def get_context_data(self, **kwargs):
        context = super(Profileview, self).get_context_data(**kwargs)
        context['pro'] = Profile.objects.all()
        return context


