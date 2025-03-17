from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import SalesEntryForm
from .forms import DailyPurchaseForm
from .models import StockRequisition
from .models import SalesEntry, DailyPurchase



# Create your views here.

def LoginPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        paswd = request.POST.get('pass')
        user = authenticate(username=uname, password=paswd)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username/Password is incorrect!")
    return render(request, 'login.html')

def HomePage(request):
    return render(request, 'home.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')  # Redirect to login after logout
 



def daily_purchase(request):
    if request.method == "POST":
        form = DailyPurchaseForm(request.POST)
        if form.is_valid():
            if request.POST.get("action") == "save":
                # Save the data to the database but don't mark it as submitted
                form.save()
                return redirect("success")  # Redirect to the same page
            elif request.POST.get("action") == "submit":
                # Save the data and handle "submission" logic if needed
                form.save()
                # Add additional logic here for submission if necessary
                return redirect("success")  # Redirect to the same page
    else:
        form = DailyPurchaseForm()

    return render(request, "daily_purchase.html", {"form": form})





def DailySales(request):
    if request.method == 'POST':
        form = SalesEntryForm(request.POST)
        print("Form data received:", request.POST)
        if form.is_valid():
            form.save()  # Save form data to the database
            print("Form saved successfully")
            return redirect('success')  # Redirect to a success page or another view
        else:
            print("Form errors:", form.errors)
    else:
        form = SalesEntryForm()
    return render(request, 'daily_sales.html', {'form': form})



def DailyStock(request):
    return render(request, 'daily_stock_requisition.html')



def SuccessView(request):
    return render(request, 'success.html')



def view_history(request):
    try:
        sales_history = DailySales.objects.all().order_by('-date')
        return render(request, 'view_history.html', {'sales_history': sales_history})
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})

