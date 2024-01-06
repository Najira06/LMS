from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('readers/',views.readers,name='readers'),
    path('books/',views.books,name='books'),
    path('mybag/',views.mybag,name='mybag'),
    path('returns/',views.returns,name='returns'),

]

