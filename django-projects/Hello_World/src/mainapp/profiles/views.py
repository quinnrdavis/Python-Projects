from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Profile
from .forms import ProfileForm


def profiles_page(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/profiles_page.html', {'profiles': profiles})


def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Profile, pk=pk)
    form = ProfileForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('profiles_page')
        else:
            print(form.errors)
    else:
        return render(request, 'profiles/present_profile.html', {'form': form})


def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('profiles_page')
    context = {"item": item,}
    return render(request, 'profiles/confirmDelete.html', context)


def confirm(request):
    if request.method == 'POST':
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('profiles_page')
    else:
        return redirect('profiles_page')


def createRecord(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profiles_page')
    else:
        print(form.errors)
        form = ProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'profiles/createRecord.html', context)
