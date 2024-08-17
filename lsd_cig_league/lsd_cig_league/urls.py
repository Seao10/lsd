from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scoreboard/', include('scoreboard.urls')),  # Include app URLs
    path('', RedirectView.as_view(url='/scoreboard/', permanent=False)),  # Redirect root to scoreboard
]
