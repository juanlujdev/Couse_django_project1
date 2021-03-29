"""empleado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings  # importo el archivo de configuracion actual de django
from django.conf.urls.static import static  # paquete para generar url estaticas de archivos multimedia

urlpatterns = [
                  path('admin/', admin.site.urls),
                  # incluimos las urls de la app departamemto y persona
                  re_path('', include('applications.departamento.urls')),
                  re_path('', include('applications.persona.urls')),
                  re_path('', include('applications.home.urls')),

              ] + static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)  # se genera a traves del paquete de static, queremos
# que traiga por defecto de nuestro archivo de configuracion (settings) que traiga por defecto los archivos multimedia
# (Seria MEDIA_URL por que es donde queremos guardar las imagenes, esta configurado en settings, local) que nos genere
# para la ruta de un documento que este guardado en nuestro proyecto (document_root =settings.MEDIA_ROOT)
