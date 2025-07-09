from rest_framework import routers
from .api import ProductViewSet

router = routers.DefaultRouter()

router.register('api/productos', ProductViewSet, 'productos')

urlpatterns = router.urls