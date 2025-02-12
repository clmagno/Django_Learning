from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns=[
    path('',views.index, name='index'),
    path('members/',views.home, name='members'),
    path('members/add/', views.add, name='add'),
    path('members/add/addrecord/', views.addrecord, name='addrecord'),
    path('members/update/<int:id>', views.update, name='update'),
    path('members/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('members/confirm_delete/<int:id>', views.confirm_delete, name='confirm_delete'),
    path('members/confirm_delete/delete/<int:id>', views.delete, name='delete'),
    path('add_product/', views.add_product, name='add_product'),
    path('members/upload_csv/', views.upload_csv, name='upload_csv'),
    path('login/', LoginView.as_view(template_name='misc/login.html'),name='login'),
    path('logout/', LogoutView.as_view(next_page='/members/'), name='logout'),
]