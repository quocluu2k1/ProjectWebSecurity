from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('user_order/', views.user_order, name='user_order'),
    path('user_update/', views.user_update, name='user_update'),
    path('comment/', views.comment, name='comment'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('reset_password_validate/<uidb64>/<token>', views.reset_password_validate, name='reset_password_validate'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('shipper/', views.shipper, name='shipper'),
]
