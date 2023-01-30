from django . urls import path
from .import views
app_name="app15"
urlpatterns=[
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('home/<int:id>',views.home,name='home'),
    path('show_users',views.show_users,name='show_users'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('changepassword/<int:id>',views.changepassword,name='changepassword'),
    path('registerimage/',views.registerimage,name='registerimage'),
    path('loginform/',views.loginform,name="loginform"),
    path('homeimage/<int:id>',views.homeimage,name='homeimage'),
    path('logout/',views.logout,name='logout'),
]