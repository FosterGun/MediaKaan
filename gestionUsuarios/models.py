from djongo import models
from django.utils import timezone
from django.contrib.auth.models import User
from gestionArticulos.models import Media


# Create your models here.
# Los modelos serán las tablas de datos que tendrá nuestra base de datos

class UsuarioUbicacion(models.Model):
    """
    Modelo de datos para la ubicación del usuario.

    Se compone de:
    - Un modelo User que hace de clave extranjera primaria (con username, email, password, fecha de unión, etc...)
    - La latitud de la ubicación del usuario
    - La longitud de la ubicación del usuario
    """

    usuario=models.OneToOneField(User, on_delete=models.CASCADE)
    latUb=models.FloatField(verbose_name='Latitud de la ubicación')
    lngUb=models.FloatField(verbose_name='Longitud de la ubicación')
    dirUb=models.CharField(max_length=150, null=True)

    def __str__(self):
        return "Usuario: %s con ubicación con latitud %s y longitud %s y dirección %s" % (self.usuario.username, self.latUb, self.lngUb, self.dirUb)

class UsuarioInfo(models.Model):
    """
        Modelo de datos para la información adicional de los usuarios.

        Se compone de:
        - Un modelo User que hace de clave extranjera primaria (con username, email, password, fecha de unión, etc...)
        - Un avatar para el perfil
        - Una pequeña descripción
        - La valoración de su perfil en la aplicación y su número de valoraciones
        - Su fecha de nacimiento
    """

    usuario=models.OneToOneField(User, on_delete=models.CASCADE)
    avatar=models.ImageField(upload_to='avatars')
    bio=models.CharField(max_length=150)
    valoracion=models.IntegerField(default=0)
    n_valoraciones=models.IntegerField(default=0)
    fechaNacimiento=models.DateField(default=timezone.now, verbose_name='Fecha de nacimiento')
    ubicacion=models.EmbeddedField(model_container=UsuarioUbicacion)
    articulos=models.ArrayReferenceField(to=Media, related_name='mis_articulos', null=True)
    articulos_rec=models.ArrayReferenceField(to=Media, related_name='rec_articulos', null=True)

    def __str__(self):
        return "Usuario: %s con email %s y fecha de creación %s" % (self.usuario.username, self.usuario.email, self.usuario.date_joined)