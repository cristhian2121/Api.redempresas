from django.conf.urls import url, include
from Api.views import * 
from django.views.generic import TemplateView
#from * import views
#path('about/', TemplateView.as_view(template_name="about.html")),

urlpatterns = [
    url(r'^accounts/', include('registration.backends.hmac.urls')),         #ingreso usuarios
    url(r'^accounts/profile/', index.as_view(context_object_name="type"), name='index'),    #index
    url(r'^register', RegisterUser.as_view(), name='register'),     # formulario reg persona
    url(r'^reg_empresa/$', viewRegEmpresa.as_view(), name='reg_empresa'),     #formulario reg empresa
    # url(r'^empresa/(?P<pk>[0-9]+)/$', templateDetail, name='templateDetail'),
    # url(r'^empresas/', ViewEmpresa.as_view(), name='empresas')
    #url(r'^post/(?P<pk>[0-9]+)/$', templateDetail.as_view()),       #vista detallada empresa

    # url(r'home/', index.as_view(context_object_name="type"), name='index'),
    #url(r'^(?P<pk>[0-9]+)/$', templateDetail, name='templateDetail'),
    #url(r'^new/$', views.post_new, name='post_new')
    # url('home/', TemplateView.as_view(template_name='home.html')),
    #  url('ciudad/', views.CiudadList.as_view()),
    # # path('ciudad/', views.CitiesList.as_view()),
    # url('usuario/<int:pk>/', views.CiudadDetail.as_view()),    
    # # path('empresa/<int:pk>/', views.BusinessDetail.as_view())
    # url('tipo/', views.TipoList.as_view()),
    # url('empresas/', views.EmpresasList.as_view()),
    # url('vista2/', TemplateView.as_view(template_name='prueba.html'))

]