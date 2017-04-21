from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission

"""
Se crean los permisos y la instancia del almacenamiento de Google Drive
para guardar las imagenes de los posts.
"""
permission =  GoogleDriveFilePermission(
   GoogleDrivePermissionRole.READER,
   GoogleDrivePermissionType.ANYONE,
 )

gd_storage = GoogleDriveStorage(permissions=(permission, ))


# Create your models here.
class Entrada(models.Model):
	"""docstring for Entrada"""
	titulo =  models.CharField(max_length=200)
	contenido = models.TextField()
	imagen = models.ImageField(upload_to="/truekeros/",
        storage=gd_storage,
        null=True,
        blank=True,
)
	email = models.EmailField(null=False)
	number = models.IntegerField(null=None)
	slug = models.SlugField(editable=False )

	def __unicode__(self):
		return self.titulo

	#Guarda el slug automaticamente con el nombre del titulo
	def save(self, *arg, **kwargs):
		if not self.id:
			self.slug = slugify(self.titulo)
		super(Entrada, self).save(*arg, **kwargs)



