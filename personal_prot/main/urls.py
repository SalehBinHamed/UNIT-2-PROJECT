from . import views
from django.urls import path

urlpatterns =[
    path('',views.home_views , name='home_views'),
    path('about/', views.about_views, name='about_views'),
    path("create/",views.create_views,name="create_views"),
    path('update/<int:entry_id>/', views.update_views, name='update_views'),
    path('delete/<int:entry_id>/', views.delete_views, name='delete_views'),
    path('dashboard/', views.dashboard_views, name='dashboard_views'),
    path('detail/<int:user_id>/', views.detail_views, name='detail_views'),
    path("contact/",views.contact_views,name="contact_views"),
    path('massage/', views.contact_messages, name='contact_messages'),




]