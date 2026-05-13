from django.db import models
import os

# Función para organizar imágenes en subcarpetas por año/mes
def ruta_imagen_portfolio(instance, filename):
    ext = filename.split('.')[-1].lower()
    nombre = f"{instance.title}_{filename}"
    return os.path.join('portfolio', nombre)

class portfolio(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripcion')
    image = models.ImageField(
        verbose_name='Imagen',
        upload_to=ruta_imagen_portfolio,  # ← ahora usa la función personalizada
        null=True,
        blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Portafolio'
        verbose_name_plural = 'Portafolios'
        ordering = ['-created']
        db_table = 'portfolio'