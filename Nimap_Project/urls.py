from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home, name='home_page'),
    path('users/', views.users_page, name='users_page'),
    path('clients/', views.clients_page, name='clients_page'),
    path('clients/get_all_clients',views.get_all_clients, name='get_all_clients'),
    path('clients/create_new_client',views.create_new_client, name='create_new_client'),
    path('clients/update_client', views.update_client, name='update_client'),
    path('clients/get_clientby_id', views.get_clientby_id, name='get_clientby_id'),
    path('clients/delete_client', views.delete_client, name='delete_client'),
    path('projects/', views.projects_page, name='projects_page'),
    path('projects/create_new_project', views.create_new_project, name='create_new_project'),
    path('projects/get_all_projects', views.get_all_projects, name='get_all_projects'),
    path('users/get_all_user', views.get_all_user, name='get_all_users'),
    path('users/create_new_user',views.create_new_user, name='create_new_user'),
]