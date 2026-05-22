from . import views
from django.urls import path

urlpatterns = [
    path("", views.home,name='homepage'),
    path("add/", views.add_expense,name='add_expense'),
    path('update/<int:id>/', views.update_view, name='update'),
    path('delete/<int:id>/', views.delete_view, name='delete'),
]