from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.template.context_processors import media

from .forms import EnigmaForm
from EnigmasHub.models import Enigma,Tentativa
from django.contrib.auth.decorators import login_required

#Home Page
def home_page(request):
    return render(request, 'EnigmasHub/home.html')

def create_enigma(request):
    if request.method == 'POST':
        form = EnigmaForm(request.POST, request.POST)
        if form.is_valid():
            enigma = form.save(commit=False)
            enigma.usuario = request.user
            enigma.save()
            return redirect('home')
    else:
        form = EnigmaForm()
    return render(request, 'EnigmasHub/create_enigmas.html', {'form': form})

@login_required
def enigmas_list(request):
    enigmas = Enigma.objects.exclude(usuario=request.user)
    enigmas_com_tentativas = []

    for enigma in enigmas:
        tentativa = Tentativa.objects.filter(enigma=enigma, usuario=request.user).first()
        enigmas_com_tentativas.append({
            'enigma': enigma,
            'tentativa': tentativa
        })

    if request.method == 'POST':
        enigma_id = request.POST.get('enigma_id')
        enigma = Enigma.objects.get(id=enigma_id)
        usuario = request.user

        user_answer = request.POST.get('answer')
        correct_answer = enigma.correct_answer

        esta_correto = user_answer == correct_answer

        tentativa= Tentativa.objects.filter(enigma=enigma,usuario=usuario).first()

        if tentativa:
            tentativa.numero_tentativas += 1
        else:
            tentativa= Tentativa(enigma=enigma,usuario=usuario,numero_tentativas=1)

        tentativa.esta_correto = esta_correto

        if esta_correto:
            tentativa.resultado = 'Correto!'
        else:
            tentativa.resultado = 'Errado! Tente novamente.'

        tentativa.save()
        # Atualiza a lista de tentativas para o template após a nova tentativa
        for enigma_obj in enigmas_com_tentativas:
            if enigma_obj['enigma'].id == enigma.id:
                enigma_obj['tentativa'] = tentativa


    return render(request,'EnigmasHub/enigmas_list.html',{
        'enigmas_com_tentativas': enigmas_com_tentativas,
    })
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('enigmas')  # Redireciona para a página de enigmas
        else:
            return render(request, 'EnigmasHub/login.html', {'error': 'Usuário ou senha inválidos.'})
    return render(request, 'EnigmasHub/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password == password_confirm:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('enigmas')
        else:
            return render(request, 'EnigmasHub/register.html', {'error': 'As senhas não coincidem.'})

    return render(request, 'EnigmasHub/register.html')


def logout_view(request):
    logout(request)
    return redirect('login')