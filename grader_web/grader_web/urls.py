"""grader_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
  https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
  1. Add an import:  from my_app import views
  2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
  1. Add an import:  from other_app.views import Home
  2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
  1. Import the include() function: from django.urls import include, path
  2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static


# WARNING! Make sure to restrict api access for internal uses

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^users/', include('users.urls')),
  # make sure this two path doesn't overlap
  # also should try to find a better way
  url(r'', include('core.urls')),
  # --- Shouldn't be accessible elsewhere but api ---
  url(r'', include('api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
