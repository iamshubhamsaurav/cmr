from django.urls import path
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    path('', views.home),
    path('products/', views.products),
    path('customers/', views.customer)
]
