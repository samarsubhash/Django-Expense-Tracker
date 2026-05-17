from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import expensedb
# Create your views here.
def home(request):

  expenses = expensedb.objects.all()
  context = {
    'expenses' : expenses
  }
  return render(request,'expense/home.html',context)

def add_expense(request):

  if request.method == 'POST':

    title = request.POST.get('title')
    amount = request.POST.get('amount')
    category = request.POST.get('category')

    expensedb.objects.create(
      title = title,
      amount = amount,
      category = category
    )

    return redirect('homepage')
  
  return render(request,'expense/add_expense.html')

def update_view(request,id):

  expense = expensedb.objects.get(id=id)
  if request.method == 'POST':

    expense.title = request.POST.get('title')
    expense.amount = request.POST.get('amount')
    expense.category = request.POST.get('category')

    expense.save()


    return redirect('homepage')
  context = {
    'expense' : expense
  }
  
  return render(request,'expense/update_expense.html',context)