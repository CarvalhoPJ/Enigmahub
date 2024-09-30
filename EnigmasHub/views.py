from django.shortcuts import render,redirect
from .forms import EnigmaForm
from EnigmasHub.models import Enigma

#Home Page
def home_page(request):
    return render(request, 'EnigmasHub/home.html')

def create_enigma(request):
    if request.method == 'POST':
        form = EnigmaForm(request.POST, request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EnigmaForm()
    return render(request, 'EnigmasHub/create_enigmas.html', {'form': form})

def enigmas_list(request):
    enigmas = Enigma.objects.all()
    if request.method == 'POST':
        enigma_id = request.POST.get('enigma_id')
        enigma = Enigma.objects.get(id=enigma_id)
        user_answer = request.POST.get('answer')
        correct_answer = enigma.correct_answer


        if user_answer == correct_answer:
            result = "Correct"
            enigma.resolved = True
        else:
            result = "Wrong"

        enigma.answers +=1
        enigma.save()

        return render(request,'EnigmasHub/enigmas_list.html',{
            'enigmas':enigmas,
            'result':result,
            'enigma_resolved':enigma
        })
    return render(request, 'EnigmasHub/enigmas_list.html', {'enigmas': enigmas})

