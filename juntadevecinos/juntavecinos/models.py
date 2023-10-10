from django.db import models

# Create your models here.
class Vecinos(models.Model):
    rut = models.CharField(primary_key=True,max_length=15,verbose_name="Rut")
    nombre = models.CharField(max_length=100,verbose_name="Nombre")
    apellido = models.CharField(max_length=100,verbose_name="Apellido")
    direccion = models.CharField(max_length=100,verbose_name="Dirección")
    correo = models.EmailField(max_length=100,verbose_name="Correo")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    certificado = models.ImageField(upload_to='images/',verbose_name="Certificado de residencia")
    
    
    def __str__(self):
        fila = "Rut: " + self.rut + '-' +"Nombre: " + self.nombre + '-' +"Apellido: " + self.apellido + '-' +"Dirección: " + self.direccion + '-' +"Correo: " + self.correo
        return fila
    def delete(self, using=None,keep_parents=False):
        self.certificado.storage.delete(self.certificado.name)
        super().delete();


##Formato de base de datos para las noticias
class Noticias(models.Model):
    id = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=100,verbose_name="Titulo")
    Descripcion = models.TextField(verbose_name="Descripcion")
    Imagen = models.ImageField(upload_to='images/noticias/', verbose_name="Imagen")

    def __str__(self):
        fila = "Titulo: " + self.Titulo + '-' +"Descripcion : " + self.Descripcion
        return fila
    def delete(self, using=None,keep_parents=False):
        self.Imagen.storage.delete(self.certificado.name)
        super().delete();


##Formato de base de datos para las proyectos
class Proyectos(models.Model):
    id = models.AutoField(primary_key=True)
    TipoProyecto = models.CharField(max_length=100,verbose_name="Tipo de proyecto")
    Descripcion = models.TextField(verbose_name="Descripcion")
    Imagen = models.ImageField(upload_to='images/proyectos/', verbose_name="Imagen")

    def __str__(self):
        fila = "Tipo de proyecto: " + self.TipoProyecto + '-' +"Descripcion : " + self.Descripcion
        return fila
    def delete(self, using=None,keep_parents=False):
        self.Imagen.storage.delete(self.certificado.name)
        super().delete()

##Formato de base de datos para las actividades
class Actividades(models.Model):
    id = models.AutoField(primary_key=True)
    TipoSolicitud = models.CharField(max_length=100,verbose_name="Tipo de solicitud")
    Descripcion = models.TextField(verbose_name="Descripcion")
    Imagen = models.ImageField(upload_to='images/actividades/', verbose_name="Imagen")
    fecha_actividad = models.DateField(verbose_name="Fecha de actividad")
    def __str__(self):
        fila = "Tipo de solicitud: " + self.TipoSolicitud + '-' +"Descripcion : " + self.Descripcion
        return fila
    def delete(self, using=None,keep_parents=False):
        self.Imagen.storage.delete(self.certificado.name)
        super().delete()


##Formato de base de datos para las propuestas
class Propuesta(models.Model):
    id = models.AutoField(primary_key=True)
    TipoSolicitud = models.CharField(max_length=100,verbose_name="Tipo de solicitud")
    Descripcion = models.TextField(verbose_name="Descripcion")
    def __str__(self):
        fila = "Tipo de solicitud: " + self.TipoSolicitud + '-' +"Descripcion : " + self.Descripcion
        return fila
    def delete(self, using=None,keep_parents=False):
        super().delete()



