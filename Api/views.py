# Create your views here.
from django.shortcuts import render, get_object_or_404, render_to_response


from django.views import generic
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from Api.models import Ciudad, Tipo, Empresa
from Api.forms import RegEmpForm, RegisterUserForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import permission_required
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from Api.serializers import EmpresasSerializer
#admin.site.register()
# from Api.serializers import *

class index(ListView):     
    model = Empresa

    def get_context_data(self, **kwargs):
        context = super(index, self).get_context_data(**kwargs)
        context['city'] = Ciudad.objects.all()
        context['type'] = Tipo.objects.all()
        return context


# class ViewEmpresaPk(ListView):
#     model = Empresa
#     empresa = Empresa.objects.all()



# class ViewEmpresaPk()






class RegisterUser(CreateView):
    model = User
    template_name = "registration/register.html"
    form_class = RegisterUserForm
    #success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            #post.author = request.user
            user.published_date = timezone.now()
            user.save()
            return redirect('reg_empresa')#, pk=post.pk)
        else:
            form = RegisterUserForm()
        return render(request, 'registration/register.html')


class viewRegEmpresa(CreateView):
    model = Empresa
    template_name = 'registration/reg_empresa.html'
    form_class = RegEmpForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            empresa = form.save(commit=False)
            #post.author = request.user
            empresa.published_date = timezone.now()
            empresa.save()
            return redirect('templateDetail', pk=empresa.pk)
        else:
            form = RegEmpForm()
        return render(request, 'registration/reg_empresa.html')

# class templateDetail(ListView):#, pk):
#     model = Empresa#   get_object_or_404(Empresa, pk=pk)
#     template_name= 'Api/template_detail.html'

def templateDetail(request, pk):
    post = get_object_or_404(Empresa, pk=pk)
    return render(request, 'api/template_detail.html', {'post': post})


#lista empresas
# class EmpresasListApiView(ListAPIView):
#     model = Empresa
#     queryset = Empresa.objects.all()
#     permissions_classes = AllowAny
#     #renderer_classes = EmpresaJSONRenderer
#     serializer_class = EmpresaSerializer

# #Empresa detalle
# class EmpresaApiView(viewsets.ViewSet):
#     serializer_class = EmpresaListSerializer

#     def retrieve(self, request, pk):
#         queryset = Empresa.objects.all()
#         empresa = get_object_or_404(queryset, pk=pk)
#         serializer = self.serializer_class(empresa)
#         return Response(serializer.data)

