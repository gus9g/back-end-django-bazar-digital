from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import csv
from .models import Product

@csrf_exempt
def adicionar_produto(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        produto = Product.objects.create(
            nome=data['nome'],
            preco=data['preco'],
            quantidade=data['quantidade']
        )
        return JsonResponse({'id': produto.id, 'nome': produto.nome, 'preco': str(produto.preco)})
    return JsonResponse({'error': 'Método não permitido'}, status=405)

@csrf_exempt
def listar_todos_produtos(request):
    if request.method == 'GET':
        produtos = list(Product.objects.values())
        return JsonResponse(produtos, safe=False)
    return JsonResponse({'error': 'Método não permitido'}, status=405)

@csrf_exempt
def listar_produto_por_nome(request, nome):
    if request.method == 'GET':
        produtos = list(Product.objects.filter(nome__icontains=nome).values())
        return JsonResponse(produtos, safe=False)
    return JsonResponse({'error': 'Método não permitido'}, status=405)

@csrf_exempt
def alterar_produto(request, id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        try:
            produto = Product.objects.get(id=id)
            produto.nome = data.get('nome', produto.nome)
            produto.set_preco(data.get('preco', produto.preco))  # Usando o setter personalizado
            produto.quantidade = data.get('quantidade', produto.quantidade)
            produto.save()
            return JsonResponse({'id': produto.id, 'nome': produto.nome, 'preco': str(produto.preco)})
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Produto não encontrado'}, status=404)
    return JsonResponse({'error': 'Método não permitido'}, status=405)

@csrf_exempt
def excluir_produto(request, id):
    if request.method == 'DELETE':
        try:
            produto = Product.objects.get(id=id)
            produto.delete()
            return JsonResponse({'message': 'Produto excluído com sucesso'})
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Produto não encontrado'}, status=404)
    return JsonResponse({'error': 'Método não permitido'}, status=405)

@csrf_exempt
def incluir_por_planilha(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['file']
        if file.name.endswith('.csv'):
            reader = csv.DictReader(file.read().decode('utf-8').splitlines())
            for row in reader:
                Product.objects.create(
                    nome=row['nome'],
                    preco=row['preco'],
                    quantidade=row['quantidade']
                )
            return JsonResponse({'message': 'Produtos incluídos com sucesso'})
    return JsonResponse({'error': 'Método não permitido ou arquivo inválido'}, status=405)

@csrf_exempt
def incluir_por_txt(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['file']
        if file.name.endswith('.txt'):
            for line in file.read().decode('utf-8').splitlines():
                nome, preco, quantidade = line.split(',')
                produto = Product(nome=nome, preco=float(preco), quantidade=int(quantidade))
                produto.save()  # Salva o produto no banco de dados
            return JsonResponse({'message': 'Produtos incluídos com sucesso'})
    return JsonResponse({'error': 'Método não permitido ou arquivo inválido'}, status=405)