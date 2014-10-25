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
    '''
    output = "<li><a href='/todolist/1/delete/'>"
    output += '</a></li><li>'.join([p.item_text for p in my_item_list])
    output += "</li>"
    '''
    return HttpResponse(template.render(context))

def delete(request, item_id):
    Item.objects.filter(id=item_id).delete()
    print 'Deleting object ' + item_id
    return HttpResponseRedirect('/todolist')

def detail(request, item_id):
    return HttpResponse("You're looking at item %s." % item_id)

def results(request, item_id):
    response = "You're looking at the results of item %s."
    return HttpResponse(response % item_id)

