from django.urls import path

from .views import RequerimentoCreateView, RequerimentoListView, RequerimentoDetailView

urlpatterns = [
    path("", RequerimentoListView.as_view(), name="requerimento_lista"),
    path('novo', RequerimentoCreateView.as_view(), name='requerimento_create'),
    path('detalhe/<int:pk>', RequerimentoDetailView.as_view(), name='requerimento_detail'),
]
