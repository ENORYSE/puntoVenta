from rest_framework import routers
from .api import ProductViewSet
from ventas.api import RemitoViewSet
from turnos.api import TurnoAsignadoViewSet

router = routers.DefaultRouter()

router.register('api/productos', ProductViewSet, 'productos')
router.register('api/remito', RemitoViewSet, 'deliveryNotes')
router.register('turnos-asignados', TurnoAsignadoViewSet)

urlpatterns = router.urls