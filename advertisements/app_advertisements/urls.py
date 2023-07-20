from django.urls import path
from .views import index,top_sellers,advertisement_post,advertisement,register,login,profile

urlpatterns = [
    path('',index, name = "main-page"),
    path('top-sellers',top_sellers,name = "top-sellers"),
    path('ad_post',advertisement_post,name = "ad_post"),
    path('adv',advertisement,name = "adv"),
    path('register',register,name = "reg"),
    path('login', login, name="log"),
    path('profile', profile, name="prf"),
]