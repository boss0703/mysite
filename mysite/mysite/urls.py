from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # 追加
    path('discrimination/', include('discrimination.urls')),
    path('admin/', admin.site.urls),
]
