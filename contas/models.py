from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    is_aluno = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)

    def __str__(self):
        return self.username