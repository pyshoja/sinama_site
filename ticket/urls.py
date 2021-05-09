
from django.urls import path

from ticket.views import firstpageview
from ticket.views import filmlistview
from ticket.views import Tozihfilm
from ticket.views import Sinama
from ticket.views import Sanslist
from ticket.views import aboutview
from ticket.views import SignUpView
from ticket.views import Profileview

urlpatterns = [

    path('first/',firstpageview.as_view(), name='firstpage'),
    path('film/<int:janer_id>/',filmlistview.as_view()),
    path('tozih/<slug:slug>/', Tozihfilm.as_view()),
    path('sinama/', Sinama.as_view(), name='sinama'),
    path('sanslist/', Sanslist.as_view(), name='sans'),
    path('about/',aboutview.as_view(), name='about'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/profile/', Profileview.as_view(), name='profile'),
]


# from . import views
#     path('first/janer/film/account/', views.Newuser , name='register'),