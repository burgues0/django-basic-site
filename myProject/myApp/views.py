from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
        features = Feature.objects.all()
        return render(request, 'index.html', {'features' : features})

def register(request):
        #caso o metodo seja post, o formulario foi enviado
        if (request.method == 'POST'):
                #salva os valores do form em variaveis
                username = request.POST['username']
                email = request.POST['email']
                password = request.POST['password']
                passwordConf = request.POST['passwordConfirmation']
                #checa pra ver se a senha e a mesma da confirmação
                if(password == passwordConf):
                        #checa na base de dados caso o email recebido no form já existe, se sim redireciona de volta para a pagina
                        if(User.objects.filter(email=email).exists()):
                                messages.info(request, 'Email already utilized')
                                return redirect('register')
                        #mesma coisa pro username
                        elif(User.objects.filter(username=username).exists()):
                                messages.info(request, 'Username already utilized')
                                return redirect('register')
                        #caso o username e o email sejam novos, ele cria o usuario, salva no BD e redireciona pra pagina de login
                        else:
                                user = User.objects.create_user(username=username, email=email, password=password)
                                user.save()
                                return redirect('login')
                else:
                        messages.info(request, 'Passwords are not equal')
                        return redirect('register')
        else:
                return render(request, 'register.html')