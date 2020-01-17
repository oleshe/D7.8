"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include, reverse_lazy
from p_library import views
#from .views import AuthorEdit, AuthorList 
from p_library.views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from allauth.account.views import login, logout

app_name = 'p_library' 
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.books_list),
    path('', views.index),
    path('index/', views.index),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('redactions/', views.redactions),
    path('author/create', AuthorEdit.as_view(), name='author_create'),  
    path('authors', AuthorList.as_view(), name='author_list'),  
    path('author/create_many', author_create_many, name='author_create_many'),  
    path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),  
    path('renters/', views.books_rent),
    path('books/', views.books),
    path('accounts/profile/', views.profile,  name='profile'),
    path('login/', login, name='login'),  
    path('logout/', logout, name='logout'),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)