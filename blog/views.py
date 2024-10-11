# myapp/views.py
from django.shortcuts import render, redirect,HttpResponse
from .forms import MyModelForm

def  my_form_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogPost')  # Replace 'success' with the name of your success page or URL
    else:
        form = MyModelForm()

    return render(request, 'myapp/my_form.html', {'form': form})



def blogHome(request):
    return HttpResponse(f'"ON The Home:"')
def blogPost(request):
    return HttpResponse(f'"ON The blog:"')

# Create your views here.
def add(request):
    if (request.method=='POST'):
        num=int(request.POST.get('num'))
        sum = num +1

        print(sum)

    return render(request,'add.html')