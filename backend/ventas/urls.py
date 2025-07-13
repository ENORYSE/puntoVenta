from rest_framework import routers
from .api import RemitoViewSet

router = routers.DefaultRouter()

router.register('api/remitos', RemitoViewSet, 'remito')

urlpatterns = router.urls