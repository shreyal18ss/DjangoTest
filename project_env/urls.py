from django.urls import include, path

urlpatterns = [
    path('uploadexcel/', include('uploadexcel.urls')),
]