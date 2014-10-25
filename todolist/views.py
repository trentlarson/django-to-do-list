from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from todolist.models import Item

# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    my_item_list = Item.objects.order_by('id')[:5]
    template = loader.get_template('todolist/index.html')
    context = RequestContext(request, {
        'my_item_list': my_item_list,
    })
    return HttpResponse(template.render(context))

def create(request):
    new_text = request.POST['new_text']
    new_item = Item(item_text=request.POST['new_text'])
    new_item.save()
    print "Created new item " + str(new_item.id)
    return HttpResponseRedirect('/todolist/')

def delete(request, item_id):
    Item.objects.filter(id=item_id).delete()
    print "Deleting item"
    return HttpResponseRedirect('/todolist')

def detail(request, item_id):
    return HttpResponse("You're looking at item %s." % item_id)


