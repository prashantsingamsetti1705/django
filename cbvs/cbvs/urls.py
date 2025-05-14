"""
URL configuration for cbvs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('bookview/',views.BookListView.as_view()),
    # path('bookview2/',views.BookListView2.as_view()),
    # path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    # path('create/',views.CreateView.as_view()),
    # path('update/<int:pk>/',views.UpdateView.as_view()),
    # path('delete/<int:pk>/',views.DeleteView.as_view()),
        path('admin/', admin.site.urls),
    path('bookview/', views.BookListView.as_view(), name='book_list'),
    path('bookview2/', views.BookListView2.as_view(), name='book_list2'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create_book'),
    path('update/<int:pk>/', views.UpdateView.as_view(), name='update_book'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete_book'),

]
