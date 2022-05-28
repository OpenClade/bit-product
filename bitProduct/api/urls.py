 
from api.views import ProductList
# import path
from django.urls import path
urlpatterns = [
    path('products/', ProductList.as_view()),
]