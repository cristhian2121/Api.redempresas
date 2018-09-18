from rest_framework import routers
from Api.viewsets import EmpresaViewSet, CiudadViewSet, TipoViewSet, Empresas_viewViewSet

router = routers.DefaultRouter()
router.register(r'empresa', EmpresaViewSet, base_name='empresa')
router.register(r'ciudad', CiudadViewSet, base_name='ciudad')
router.register(r'tipo', TipoViewSet, base_name='tipo')
router.register(r'detalle', Empresas_viewViewSet, base_name='detalle')
