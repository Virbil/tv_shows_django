from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows),
    path('shows/new', views.add_show),
    path('shows/<int:show_id>', views.show_info, name="show_info"),
    path('shows/<int:show_id>/edit', views.edit_show, name="edit_show_info"),
    path('shows/<int:show_id>/delete', views.delete_show, name="delete_show"),
]