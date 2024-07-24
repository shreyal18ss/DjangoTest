from django.urls import path
from .views import FileUploadView, data_grid


urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('data-grid/', data_grid, name='data-grid'),

]