from django.shortcuts import render

# Create your views here.


# from django.views.generic.base import TemplateView
# from .models import testrest
#
# class testview (TemplateView):
#     model = testrest
#     template_name = 'rest_api/test_template.html'



from rest_framework import viewsets , permissions
from django.contrib.auth.models import User
from .models import testrest
from .serializers import testrestserializers , userrestserializers


class testrestview (viewsets.ModelViewSet):
    queryset = testrest.objects.all()
    serializer_class = testrestserializers


class userrestview (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userrestserializers
    permission_classes = [permissions.IsAdminUser]