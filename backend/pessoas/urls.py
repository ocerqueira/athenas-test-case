from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pessoas.views import PessoaModelViewSet


router = DefaultRouter()
router.register('pessoas', PessoaModelViewSet, basename='pessoas')
urlpatterns = [
    path('', include(router.urls)),
]
