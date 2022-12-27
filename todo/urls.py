from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [                                                 
    path('admin/', admin.site.urls),
    path("",views.index,name="Home"),
    path('del/<int:item_id>',views.remove,name="del"),
]