from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse, reverse_lazy
from django.utils.timezone import now
from django.http import HttpResponse, JsonResponse

from .models import Type, Product
from .forms import ProductCreateForm, ProductUpdateForm

# Create your views here.
# View = for normal view page = controller


def index(request):
    num_product = Product.objects.all().count()
    context = {
        'name': 0
    }
    return render(request, 'index.html', context=context)


#################################
#just view
class ProductList(ListView):
    model = Product
    context_object_name = 'product_list'    # default object_list
    template_name = 'products/product_all_list_template.html'   # using template
    queryset = Product.objects.all()
    
    def get_queryset(self):
        query = self.request.GET.get('name')
        if query:
            qs = self.model.objects.filter(name__icontains=query)
            return qs
        else:
            return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('name')
        if query:
            context["title"] = "Search: " + query
        else:
            context["title"] = "All Product"
        return context
    
    

# DetailView will auto select by XX, XX = set by urls.py
#https://zhuanlan.zhihu.com/p/36989981
class ProductDetail(DetailView):
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    queryset = Product.objects.all().prefetch_related('type')

    def get_object(self, queryset=None):
        context = super(ProductDetail, self).get_object(queryset=queryset)
        # if obj.user != obj.photoextended.user:
        #     raise Http404()
        return context

##############################
#Form

class ProductCreate(CreateView):
    model = Product
    template_name = 'products/product_create.html'
    form_class = ProductCreateForm
    #success_url = reverse_lazy('shop:product-detail/{pk}')

    def form_valid(self, form):
        # for the form post is success, then do below action
        form.cleaned_data   #clean all input data
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('shop:product-detail', args=(self.object.pk,))  #args need ','  otherwise error


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'products/product_update.html'
    form_class = ProductUpdateForm

    def form_valid(self, form):
        # for the form post is success, then do below action
        form.cleaned_data   #clean all input data
        form.instance.update_date = now()   #update product update_date in here
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('shop:product-detail', args=(self.object.pk,))  #args need ','  otherwise error


################################
#Ajax


#for the js ajax delete
def ProductDeleteAjax(request):
    id = request.POST.get('id', None)
    Product.objects.all().filter(id=id).delete()
    payload = {'delete': 'ok'}
    return JsonResponse(payload)

