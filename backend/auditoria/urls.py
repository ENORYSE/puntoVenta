from rest_framework import routers
from .api import TipoTurnoViewSet, TurnoAsignadoViewSet

router = routers.DefaultRouter()

router.register('api/turnos-tipos', TipoTurnoViewSet)
router.register('api/turnos-asignados', TurnoAsignadoViewSet)

urlpatterns = router.urls