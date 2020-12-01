from django.shortcuts import render, redirect
from .models import Pizza, Topping, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    return render(request, 'pizza_app/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas':pizzas}
    return render(request, 'pizza_app/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-name')
    comments = pizza.comment_set.order_by('-date_posted')
    context = {'pizza':pizza, 'comments':comments, 'toppings':toppings}
    return render(request, 'pizza_app/pizza.html', context)

@login_required
def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.username = request.user.username
            new_comment.author = request.user
            new_comment.save()
            form.save()
            return redirect('pizza_app:pizza', pizza_id=pizza_id)
    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizza_app/new_comment.html', context)

@login_required
def edit_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    pizza = comment.pizza
    if comment.author != request.user:
        raise Http404
    if request.method != 'POST':
        form = CommentForm(instance=comment)
    else:
        form = CommentForm(data=request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('pizza_app:pizza', pizza_id = pizza.id) 
    context = {'form':form, 'pizza':pizza, 'comment':comment}
    return render(request, 'pizza_app/edit_comment.html', context)