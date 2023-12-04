from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.home_page, name='home_page'),
    path('login/',views.login_page, name='login_page'),
    path('signup/', views.signup_page, name='signup_page'),
    path('s/',views.index_page, name='index_page'),
     
    ]
     
     
     
     
     
    
   
    # path('logout/',views.logout, name='logout'),
    
    # path('home/',views.home, name='home'),



# from django.contrib import admin
# from django.urls import path
# from your_app import views  # Make sure to replace 'your_app' with the actual name of your Django app

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.signup, name='signup'),
#     path('login/', views.login_view, name='login_view'),  # Updated the name here
#     path('logout/', views.logout, name='logout'),
#     path('signup/', views.signup, name='signup'),
#     path('home/', views.home, name='home'),
# ]
