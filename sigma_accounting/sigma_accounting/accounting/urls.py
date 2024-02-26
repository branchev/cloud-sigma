from django.urls import path

from sigma_accounting.accounting import views

app_name = "accounting"


urlpatterns = [
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('items/', views.ItemsView.as_view(), name='items'),
]
