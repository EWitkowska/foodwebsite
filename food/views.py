from django.shortcuts import render, redirect
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/details.html'
 
class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

    def dispatch(self, request):
        in_group =  self.request.user.groups.filter(name='Staff').exists()
        return in_group

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['in_group'] =  self.request.user.groups.filter(name='Staff').exists()
        return context

def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'form':form,'item':item})

def delete_item(request,id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request,'food/item-delete.html',{'item':item})