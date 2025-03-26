from django.urls import path
from . import views
from .views import filter_rents
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),


    path('login', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signUp', views.user_signUp, name='signUp'),
    path("profile", views.profile, name="profile"),


    path('aboutUs', views.aboutUs, name='about'),
    path('error', views.error, name='404'),

    path('services/rent', views.servicesPageRent, name='servicesPageRent'),
    path('services/movie', views.servicesPageMovie, name='servicesPageMovie'),

    path('location/street', views.locationPageStreet, name='locationPageStreet'),
    path('location/room', views.locationPageRoom, name='locationPageRoom'),
    path('location/studio', views.locationPageStudio, name='locationPageStudio'),
    path("filter_rents/", filter_rents, name="filter_rents"),



    path('service/rent/detail/<int:rent_id>/', views.rent_detail, name='servicesDetailPage'),
    # path('service/movie/detail/<int:rent_id>/', views.servicesDetailPage, name='servicesDetailPage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)