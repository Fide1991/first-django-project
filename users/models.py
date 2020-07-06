from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE) #User es la tabla de donde va a jalar el id. related_name es el nombre(alias) que le damos 
    #para poder acceder desde la tabla usuario(que no tiene definida la relacion) al perfil
    gender = models.CharField(max_length=140)
    phone = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/profile_images/',blank=True, null=True)#carpeta donde se van a guardar las imagenes, 
    #es necesario intalar la libreria Pillow (libreria para manejar imagenes)

    def __str__(self):#para que se muestre en la pagina de admin lo que deseamos en lugar de "Profile object"
        return f'Perfil del usuario {self.user.first_name} {self.user.last_name}'#accedemos a la informacion de la tabla User a traves de la relacion (self.user.first_name)
    