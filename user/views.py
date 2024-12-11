# myapp/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('usuario')
            password = data.get('senha')

            # Verifica se os campos estão preenchidos
            if not username or not password:
                return JsonResponse({'error': 'Nome de usuário e senha são obrigatórios.'}, status=400)

            # Verifica se o usuário já existe
            if User.objects.filter(usuario=username).exists():
                return JsonResponse({'error': 'Usuário já existe.'}, status=400)

            # Cria e salva o novo usuário
            new_user = User(usuario=username, senha=make_password(password))  # Armazena a senha hashada
            new_user.save()

            return JsonResponse({'message': 'Usuário criado com sucesso!', 'usuario': new_user.usuario}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON inválido'}, status=400)

    return JsonResponse({'error': 'Método não permitido'}, status=405)

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('usuario')
            password = data.get('senha')
            senhaMock = make_password("123")

            # Verifica se os campos estão preenchidos
            if not username or not password:
                return JsonResponse({'error': 'Nome de usuário e senha são obrigatórios.'}, status=400)

            # Tenta encontrar o usuário
            user = User.objects.filter(usuario=username).first()

            if user:  # Se o usuário foi encontrado
                if check_password(password, senhaMock): 
                    return JsonResponse({'message': 'Login bem-sucedido!', 'usuario': user.usuario})
                else:
                    return JsonResponse({'error': 'Credenciais inválidas'}, status=401)
            else:
                return JsonResponse({'error': 'Credenciais inválidas'}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON inválido'}, status=400)

    return JsonResponse({'error': 'Método não permitido'}, status=405)