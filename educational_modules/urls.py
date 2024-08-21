from django.urls import path

from .apps import EducationalModulesConfig
from .views import (EduModelAPIView, EduModelDetailAPIView, EduModelCreateAPIView, EduModelUpdateAPIView,
                    EduModelDestroyAPIView)

app_name = EducationalModulesConfig.name

urlpatterns = [
    path('models/', EduModelAPIView.as_view(), name='models'),
    path('models/<int:pk>/', EduModelDetailAPIView.as_view(), name='model'),
    path('models/create/', EduModelCreateAPIView.as_view(), name='create'),
    path('models/delete/<int:pk>/', EduModelDestroyAPIView.as_view(), name='delete'),
    path('models/update/<int:pk>/', EduModelUpdateAPIView.as_view(), name='update'),
]
