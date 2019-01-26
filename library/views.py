from django.shortcuts import render
from .models import Books
from users.models import CustomUser
import json
from django.http import HttpResponse,HttpResponseRedirect
from .forms import BookForm
# Create your views here.

def assign_book(request):
    if request.method=="POST":
        json_str = request.body.decode(encoding = 'UTF-8')
        data = json.loads(json_str)
        book_id = data['id']
        username = data['username']
        book = Books.objects.get(id=book_id)
        user = None
        try:
            user = CustomUser.objects.get(username = username)
            if user is not None:
                book.assigned_to = user
                book.is_assigned = True
                book.save()
                return HttpResponse("Book assigned to the user.")
        except:
            return HttpResponse("bad username")




def mark_returned(request):
    if request.method=="POST":
        json_str = request.body.decode(encoding = 'UTF-8')
        data = json.loads(json_str)
        book_id = data['id']
        book = Books.objects.get(id=book_id)
        book.assigned_to = None
        book.is_assigned = False
        book.save()
        return HttpResponse("Book marked as returned")


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
            temp_json['assigned_to'] = str(x.assigned_to)
            response_json['book'].append(temp_json)
            response_json['size'] = response_json['size'] + 1 
        print(response_json)
        return HttpResponse(json.dumps(response_json),content_type = 'application/json')

def book_info(request,b_id):
    response_json = {}
    bookss = Books.objects.all().filter(id = b_id)
    for book in bookss:
        response_json['book_name'] = book.name
        response_json['author'] = book.author
        response_json['is_assigned']= (book.is_assigned)
        response_json['id']=(int(book.id))
    if (book.is_assigned):
        response_json['username'] = str(book.assigned_to.username)
    return render (request,'library/book_profile.html',response_json)