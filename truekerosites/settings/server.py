#!usr/local/bin
# coding: latin-1

"""
Se importa la configuración de la aplicacipón para obtener
la instancia de la base de datos que está utilizando la aplicación.
"""
from django.conf import settings

"""
dj_database_url: Realiza una sincronización entre la base de datos
de la aplicación y la base de datos del servidor (Heroku)
"""
import dj_database_url

"""Se desactiva el modo debug de la aplicación, para que no muestre
información detallada en caso de que ocurra un error."""
DEBUG = False


DATABASES = settings.DATABASES

db_from_env = dj_database_url.config(conn_max_age=500)

DATABASES['default'].update(db_from_env)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

"""
Se especifica que la aplicación va almacenar los archivos estaticos mediante whitenoise.
"""
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
"""
Configuracion Variables de Entorno Heroku
"""
EMAIL_HOST_USER= os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']