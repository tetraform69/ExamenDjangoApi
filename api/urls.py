from django.urls import path
from . import views

urlpatterns = [
    path('usuario', views.UsuarioList.as_view()),
    path('usuario/<int:pk>', views.UsuarioDetail.as_view()),
    path('programa', views.ProgramaList.as_view()),
    path('programa/<int:pk>', views.ProgramaDetail.as_view()),
]