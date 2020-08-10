from django.urls import path,include
from .import views
urlpatterns = [
                path('',views.home,name='home'),
                path('login',views.login,name='login'),
                path('sinup',views.sinup,name='sinup'),
                path('logout',views.log_out,name='logout'),
                path('detail',views.detail,name='detail'),
                path('occupation',views.occupation,name='occupation'),
                path('update',views.update,name='update'),
                path('vdetail',views.vdetail,name='view detail'),
]
