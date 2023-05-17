from django.urls import path,include
from django.contrib import admin, auth
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import CategoryAPIView, ProduitAPIView, ProductViewset
from rest_framework import routers

router = routers.SimpleRouter()
router.register('produit', ProductViewset, basename='produit')

urlpatterns = [ 
 path('', views.index, name='index'),
 path('mag', views.mag, name='mag'),
 path('vitrine', views.vitrine, name='vitrine'),
 path('acceuil', views.acceuil, name='acceuil'),
 path('order', views.order, name='order'), 
 path('nouveauFournisseur', views.nouveauFournisseur, name='nouveauFournisseur'),
 path('accounts/', include('django.contrib.auth.urls')),
 path('api-auth/', include('rest_framework.urls')),
 path('api/category/', CategoryAPIView.as_view()),
 path('api/produit/', ProduitAPIView.as_view()),
 path('register/',views.register, name = 'register'),
 path('api/', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
