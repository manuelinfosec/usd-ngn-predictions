from django.urls import path
from .views import Predict

urlpatterns = [
    path("", Predict.as_view(), name="predict")
]