from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('create',views.create),
    path('authors',views.authors),
    path('books/<_id>',views.showBook),
    path('authors/<_id>',views.showAuthor),

]