from django.db import models
import uuid

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, null=False, help_text='Enter product name')
    description = models.CharField(max_length=300, help_text='Enter description')
    type = models.ForeignKey(Type, null=True, on_delete=models.SET_NULL)
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ['name', '-update_date']

    def __str__(self):
        return f'{self.name} {self.description} {self.type} {self.update_date}'




