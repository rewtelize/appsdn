from django.conf.urls import url

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.login, name='login'),
    #url(r'^$', views.index, name='index'),
    url(r'^Conmutadores', views.conmutadores, name='conmutadores'),
    url(r'^Administracion', views.index, name='index'),
    url(r'^Aplicaciones', views.aplicaciones, name='aplicaciones'),
    url(r'^Usuarios', views.usuarios, name='usuarios'),
    url(r'^Estadisticas', views.graficos, name='graficos'),
    url(r'^Topologia', views.topologia, name='graficos'),
    url(r'^Politicas', views.politicas, name='politicas'),
    url(r'^Configuraciones', views.configuraciones, name='configuraciones'),

    url(r'^Login', views.login, name='login'),
    url(r'^Registro', views.registro, name='registro'),

    url(r'^NuevosConmutadores', views.nuevos_conmutadores, name='nuevos_conmutadores'),
    url(r'^BorrarConmutador/(?P<pk>[0-9a-f-]+)/$', views.borrar_conmutador, name='borrar_conmutador'),
    url(r'^NuevasConfiguraciones', views.nuevas_configuraciones, name='nuevas_configuraciones'),
    url(r'^BorrarConfiguracion/(?P<pk>[0-9a-f-]+)/$', views.borrar_configuracion, name='borrar_configuracion'),
    url(r'^NuevasAplicaciones', views.nuevas_aplicaciones, name='nuevas_aplicaciones'),
    url(r'^BorrarAplicacion/(?P<pk>[0-9a-f-]+)/$', views.borrar_aplicacion, name='borrar_aplicacion'),
    url(r'^NuevosUsuarios', views.nuevos_usuarios, name='nuevos_usuarios'),
    url(r'^AdminUsuario/(?P<pk>[0-9a-f-]+)/$', views.admin_usuario, name='admin_usuario'),
    url(r'^BorrarUsuario/(?P<pk>[0-9a-f-]+)/$', views.borrar_usuario, name='borrar_usuario'),
    url(r'^NuevasRelaciones', views.nuevas_relaciones, name='nuevas_relaciones'),
    url(r'^BorrarRelacion/(?P<pk>[0-9a-f-]+)/$', views.borrar_relacion, name='borrar_relacion'),
    url(r'^NuevasPoliticas', views.nuevas_politicas, name='nuevas_politicas'),
    url(r'^BorrarPolitica/(?P<pk>[0-9a-f-]+)/$', views.borrar_politica, name='borrar_politica'),

    url(r'^MandarMensaje', views.mandar_mensaje, name='mandar_mensaje'),
    url(r'^RutasRespaldo', views.rutas_respaldo, name='rutas_respaldo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
