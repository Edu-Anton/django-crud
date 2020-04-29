from django.db import models

# Create your models here.
# Esta clase representa una tabla
class Project(models.Model):
  title = models.CharField(max_length=200, verbose_name="Título")
  description = models.TextField(verbose_name="Descripción")
  image = models.ImageField(verbose_name="Imagen")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
  updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización") # se adicionar{a con cada modificación

  class Meta:
    verbose_name = "proyecto"
    verbose_name_plural = "proyectos"
    ordering = ['-created_at']
  
  def __str__(self):
    return self.title