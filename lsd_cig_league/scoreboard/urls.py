from django.urls import path
from . import views

urlpatterns = [
    path('', views.scoreboard_view, name='scoreboard'),
    # path('admin/', views.admin_view, name='admin_scoreboard'),  # Add this line
]
