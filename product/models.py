from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=100, verbose_name='Nombre Producto')
    content=models.TextField(verbose_name='Contenido')
    image=models.ImageField(upload_to='product', verbose_name='Imagen')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering=['-created']

    def __str__(self):
        return self.title
