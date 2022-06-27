from django.shortcuts import render , redirect
from .models import *

def index(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
    return render(request,'index.html',context)


def authors(request):
    _authors = Author.objects.all()
    context = {
        'authors':_authors
    }
    return render(request,'authors.html',context)


def create(request):
    if request.method == 'POST':
        if request.POST['form'] == 'book':
            book = Book.objects.create(
                title = request.POST['title'],
                description = request.POST['description']
            )
            book.save()
        elif request.POST['form'] == 'author':
            author = Author.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                notes = request.POST['notes'],
            )
            author.save()
            return redirect('/authors')

        elif request.POST['form'] == 'addAuthor' or request.POST['form'] == 'addBook':
            author_id = request.POST['author_id']
            book_id = request.POST['book_id']

            author = Author.objects.get(id=author_id)
            book = Book.objects.get(id=book_id)

            author.books.add(book)
            book.authors.add(author)

            if request.POST['form'] == 'addAuthor':
                return redirect(f"books/{book_id}")
            else: 
                return redirect(f"authors/{author_id}")
    
    return redirect('/')

def showBook(request,_id):
    book = Book.objects.get(id=_id)
    authors = Author.objects.exclude(books=book)
    context = {
        'book':book,
        'authors':authors,

    }
    return render(request,'show_book.html',context)


def showAuthor(request,_id):
    author = Author.objects.get(id=_id)
    books = Book.objects.exclude(authors=author)
    context = {
        'author':author,
        'books':books,
    }
    return render(request,'show_author.html',context)