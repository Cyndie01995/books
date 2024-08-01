from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    # path('all/', views.book_list, name='book_list'), for function base views
    path('', views.BookList.as_view(), name='book_list'), #for classbase views
    # path('', views.BookListGeneric.as_view(), name='book_list'), #for classbase views using generics

]
