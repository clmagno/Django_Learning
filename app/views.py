from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Member
from django.template import loader
from django.urls import reverse
from .forms import ProductForm, UploadCSVForm
import csv
from io import TextIOWrapper
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return HttpResponse(loader.get_template('misc/index.html').render({},request))

@login_required
def home(request):
    members = Member.objects.all().values()
    template = loader.get_template('members/home.html')
    context={
        'members':members
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template  = loader.get_template('members/add.html')
    return HttpResponse(template.render({},request)) 

def addrecord(request): 
    fn = request.POST['first']
    ln = request.POST['last']
    
    member = Member(fname=fn, lname=ln)
    member.save()
    return HttpResponseRedirect(reverse('members'))

def update(request,id):
    member = Member.objects.get(id=id) #Select * from Member where id= 3
    
    template = loader.get_template("members/update.html")
    context={
        'member':member
    }
    return HttpResponse(template.render(context,request))

def updaterecord(request,id):
    fn = request.POST['first']
    ln = request.POST['last']
    member = Member.objects.get(id=id)
    member.fname = fn
    member.lname = ln
    member.save()
    return HttpResponseRedirect(reverse('members'))

def confirm_delete(request,id):
    member = Member.objects.get(id=id)
    template = loader.get_template("members/delete.html")
    context ={
        "member":member
    }
    return HttpResponse(template.render(context,request))
    
def delete(request,id):
    member = Member.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('members'))


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to a list of products
    else:
        form = ProductForm()
    return render(request, 'products/add.html', {'form': form})
@login_required
def upload_csv(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            # Check if it's a valid CSV file
            if csv_file.name.endswith('.csv'):
                # Open the CSV file in text mode
                csv_text = TextIOWrapper(csv_file.file, encoding='utf-8')
                # Parse CSV data and create Member objects
                csv_data = csv.reader(csv_text)
                # next(csv_data) # if there is no header remain commented
                for row in csv_data:
                    fname, lname = row
                    Member.objects.create(fname=fname, lname=lname)
                return HttpResponseRedirect(reverse('members'))  # Render the success page
            else:
                # Handle invalid file format
                return render(request, 'members/upload.html', {'form': form, 'error_message': 'Invalid file format.'})
    else:
        form = UploadCSVForm()
    return render(request, 'members/upload.html', {'form': form})