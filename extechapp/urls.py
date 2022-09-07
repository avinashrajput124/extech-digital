from django.urls import path

from extechapp import views

urlpatterns=[

    path('',views.login_user,name='login'),

    path('signup',views.signup,name='signup'),
    path('main',views.main,name='main'),
    path('dashbord',views.dashbord,name="dashbord"),
    path('delete_data/<int:id>/',views.delete_data,name="delete_data"),
    path('update/<int:id>',views.update,name='update'),
    path('<int:id>',views.edit_data,name='edit_data'),
    path('logout_user',views.logout_user,name="logout_user"),
]