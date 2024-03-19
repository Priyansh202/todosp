from app import views
from django.urls import path

urlpatterns = [
    
    
    path('', views.home),
    path('signup/', views.signup),
    path('loginn/', views.loginn),
    path('todopage', views.todo),
    path('delete_todo/<int:srno>', views.delete_todo),
    path('edit_todo/<int:srno>', views.edit_todo, name='edit_todo'),
    path('mark_completed/<int:srno>/', views.mark_completed, name='mark_completed'),
    path('signout/', views.signout, name='signout'),
    

]
