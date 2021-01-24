from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .models import Bookshop


def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def book(request):
    books_list = Bookshop.objects.all()
    return render(request, "books.html", {"books_list": books_list})

def second(request):
    return HttpResponse("Test 2 page")

def add_todo(request):
    form = request.POST
    text = form["todo_test"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite=True
    todo.save()
    return redirect(test)


def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite=False
    todo.save()
    return redirect(test)

def mark_book(request, id):
    books = Bookshop.objects.get(id=id)
    books.is_favorite=True
    books.save()
    return redirect(book)

def unmark_book(request, id):
    books = Bookshop.objects.get(id=id)
    books.is_favorite=False
    books.save()
    return redirect(book)

def delete_book(request, id):
    books = Bookshop.objects.get(id=id)
    books.delete()
    return redirect(book)

def BooksDetail(request, id):
    book_object = Bookshop.objects.get(id=id)
    return render(request, "books_detail.html", {"book_object": book_object})

def add_book(request):
    form = request.POST
    books1 = form["book_title"]
    books2 = form["book_subtitle"]
    books3 = form["book_description"]
    books4 = form["book_price"]
    books5 = form["book_genre"]
    books6 = form["book_author"]
    books7 = form["book_year"]
    bookshop = Bookshop(title=books1, subtitle=books2, description=books3, price=books4, genre=books5, author=books6, year=books7)
    bookshop.save()
    return redirect(book)

