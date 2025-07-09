from rest_framework import routers
from .api import ProductViewSet, DeliveryNoteViewSet

router = routers.DefaultRouter()

router.register('api/productos', ProductViewSet, 'productos')
router.register('api/deliveryNotes', DeliveryNoteViewSet, 'deliveryNotes')

urlpatterns = router.urls