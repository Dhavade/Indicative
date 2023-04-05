from django.urls import path,include
from members import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    #path("show/",views.show,name='show'),
    path('index/', views.index), 
    #path('upload', views.upload_file_view, name = 'upload-view'),
    #path('simple/', views.simple_upload,name=""), 
    path('', views.simple_upload,name=""),
    path('calculation', views.calculation,name="claculation"), 
    #path('simple/', views.simple,name="simple"),
    #path('Upload',views.Upload,name='Upload')
    path('user_ip/',views.show_ip_address),
    path('pegination',views.my_view)

    #path('file/', views.file,name="file"), 



]
'''path("",LoginView.as_view(template_name='uplode.html'))
    from django.contrib.auth.views import LoginView'''
