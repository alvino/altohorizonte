from django.urls import path

from .views import RequerimentoCreateView

urlpatterns = [
    path('novo', RequerimentoCreateView.as_view(), name='requerimento_new'),
]
