from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

import json
from todolist.models import Item


# Some helpers first

#def set_cookie(response, key, value, days_expire = 7):
def user_cookie_value(request):
  if 'todos' in request.COOKIES:
      return json.loads(request.COOKIES['todos'])
  else:
      return []



# Now the views

def index(request):
    my_item_list = user_cookie_value(request)
    print "my_item_list"
    print my_item_list
    template = loader.get_template('todolist/index.html')
    context = RequestContext(request, {
        'my_item_list': my_item_list,
    })

    response = HttpResponse(template.render(context))
    todoStr = json.dumps(my_item_list)
    response.set_cookie('todos', todoStr)

    return response

def create(request):
    my_item_list = user_cookie_value(request)
    my_item_list.append(request.POST['new_text'])
    todoStr = json.dumps(my_item_list)

    response = HttpResponseRedirect('/todolist/')
    response.set_cookie('todos', todoStr)

    return response

    '''
    // server-side DB
    new_text = request.POST['new_text']
    new_item = Item(item_text=request.POST['new_text'])
    new_item.save()
    print "Created new item " + str(new_item.id)
    return HttpResponseRedirect('/todolist/')
    '''



def delete(request, item_id):
    my_item_list = user_cookie_value(request)
    my_item_list.pop(int(item_id))
    todoStr = json.dumps(my_item_list)

    response = HttpResponseRedirect('/todolist/')
    response.set_cookie('todos', todoStr)

    return response

    '''
    // server-side DB
    Item.objects.filter(id=item_id).delete()
    print "Deleting item"
    return HttpResponseRedirect('/todolist')
    '''




def detail(request, item_id):
    return HttpResponse("You're looking at item %s." % item_id)


