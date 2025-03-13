from django.urls import path

from . import views

app_name = 'weathers'

urlpatterns = [
    path("", views.index, name="cities"),
    path('<int:pk>', views.detail, name = 'city'),
    path('add', views.add_city, name = 'city_add'),

    path('delete/<int:pk>/', views.delete_city, name = 'city_delete'),
    path('update/<int:pk>/', views.update_city, name = 'city_update'),
    # path('weathers/<int:pk>', views.detail, name = 'weathers'),
    path('weathers/', views.weathers_view, name = 'weathers'),
]