from django.urls import path
from phone import views

app_name = "phone"
urlpatterns = [
    path("", views.index, name="index"),
    path('phones/', views.PhoneListView.as_view(), name='phone-list'),
    path('add-phone/', views.add_phone, name='add-phone'),
    path('get-report/', views.get_report, name='get-report')
]
