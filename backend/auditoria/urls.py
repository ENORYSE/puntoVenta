from rest_framework import routers
from .api import TipoTurnoViewSet, TurnoAsignadoViewSet

router = routers.DefaultRouter()

router.register('turnos-tipos', TipoTurnoViewSet)
router.register('turnos-asignados', TurnoAsignadoViewSet)

urlpatterns = router.urls