from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class User(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.CharField(max_length=255, null=True, blank=True)
    senha = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.senha:
            self.senha = make_password(self.senha)  # Hash a senha antes de salvar
        super().save(*args, **kwargs)
