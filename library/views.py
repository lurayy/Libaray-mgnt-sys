from django.shortcuts import render
from .models import Books
import json
from django.http import HttpResponse,HttpResponseRedirect
from .forms import BookForm
# Create your views here.

def assign_book(request):
    pass

def mark_returned(request):
    pass


def add_book(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Some errors occured in the form please try again.')
    else:
        book_form = BookForm()
        print(book_form)
        return render(request, 'library/register_book.html', { 'book_form':book_form})

def search(request):
    if request.method=="POST":
        json_str = request.body.decode(encoding = 'UTF-8')
        data = json.loads(json_str)
        book_name = data['name']
        book = Books.objects.filter(name = book_name)
        response_json = {'book':[],'size':0}
        for x in book:
            temp_json = {}
            temp_json['id'] = x.id
            temp_json['name'] = x.name
            temp_json['author']= x.author
            temp_json['is_assigned'] = x.is_assigned
            temp_json['assigned_to'] = x.assigned_to
            response_json['book'].append(temp_json)
            response_json['size'] = response_json['size'] + 1 
        print(response_json)
        return HttpResponse(json.dumps(response_json),content_type = 'application/json')

