
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',recipes,name="recipes"),
    path('recipe_info',recipe_info,name="recipe_info"),
    path('del_recipe/<int:pk>',del_recipe,name="del_recipe"),
    path('update_recipe/<int:pk>',update_recipe,name="update_recipe")
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns() 