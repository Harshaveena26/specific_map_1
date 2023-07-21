from django.urls import path,include
import app
urlpatterns =[
    path('app/',include('app.urls')),
]