from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import blog.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.main, name="main"),
    path('home/', blog.views.home, name="home"),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

