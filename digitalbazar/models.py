from django.db import models

class Product(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # Setter personalizado
    def set_preco(self, novo_preco):
        if novo_preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        self.preco = novo_preco  
        self.save()
