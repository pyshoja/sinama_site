
from django.urls import path , include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
# from rest_api.views import testview
from . import views

router= routers.DefaultRouter()
router.register('',views.testrestview)
router.register('user/',views.userrestview)


urlpatterns = [

    # path('testview/',testview.as_view(), name='testview'),
    path('v1/', include(router.urls)),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]