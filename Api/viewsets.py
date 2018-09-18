from rest_framework import generics, viewsets
from .serializers import *
from rest_framework.response import Response

class EmpresaViewSet (viewsets.ModelViewSet): 
    serializer_class = EmpresasSerializer
    def get_queryset(self):
        filtro_ciudad = self.request.query_params.get('id_ciudad', None)
        filtro_tipo = self.request.query_params.get('id_tipo',None)        
        queryset = Empresa.objects.all()

        if filtro_ciudad is not None:
            queryset_ciudad = queryset.filter(id_ciudad=filtro_ciudad)
        else:
            queryset_ciudad = queryset
        if filtro_tipo is not None:
            queryset = queryset_ciudad.filter(id_tipo=filtro_tipo)
        else:
            queryset = queryset_ciudad        
        return queryset
    # def perform_create(self, serializer):
    #     print(serializer)
    #     serializer.save(owner=self.request.EmpresasSerializer)

class CiudadViewSet (viewsets.ModelViewSet): 
    serializer_class = CiudadSerializer
    def get_queryset(self):
        filtro = self.request.query_params.get('id_ciudad', None)
        print(filtro)
        queryset = Ciudad.objects.all()
        print(queryset)
        if filtro is not None:
            print("------------- Entro por aqui ------------")
            queryset = queryset.filter(id_ciudad=filtro)
            print(queryset)
        return queryset

class TipoViewSet (viewsets.ModelViewSet): 
    queryset = Tipo.objects.all () 
    serializer_class = TipoSerializer

class Empresas_viewViewSet(viewsets.ModelViewSet):
    serializer_class = Empresas_viewSerializer
    def get_queryset(self):
        filtro_empresa_view = self.request.query_params.get('nombre', None)
        filtro_usuario_view = self.request.query_params.get('email_user', None)
        queryset = Empresas_view.objects.all()

        if filtro_empresa_view is not None:
            queryset = queryset.filter(nombre=filtro_empresa_view)
        if filtro_usuario_view is not None:
            print("entra al filtro")
            queryset = queryset.filter(email_user='hrpalma@gmail.com')
            print(queryset)
        return queryset
    