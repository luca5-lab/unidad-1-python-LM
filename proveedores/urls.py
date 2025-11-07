from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('registrarse/', views.register_view, name='registrarse'),
    path('logout/', views.logout_view, name='logout'),
    path('proveedores/nuevo/', views.nuevo_proveedor, name='nuevo_proveedor'),
    path('proveedor/<int:id>/eliminar/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('detalle/<int:proveedor_id>/', views.detalle_proveedor, name='detalle_proveedor'),
    path('gestionar_desempeno/', views.gestionar_desempeno, name='gestionar_desempeno'),
    path('gestionar_desempeno/<int:proveedor_id>/', views.gestionar_desempeno_proveedor, name='gestionar_desempeno_proveedor'),
    path('solo_vista/', views.solo_vista, name='solo_vista'),
    path('dashboard_editor/', views.editor_view, name='dashboard_editor'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('proveedor/<int:proveedor_id>/agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('producto/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('recordar-contrasena/', views.recordar_contrasena, name='recordar_contrasena'),
    path('verificar_codigo/', views.verificar_codigo, name='verificar_codigo'),
    path('cambiar_contrasena/', views.cambiar_contrasena, name='cambiar_contrasena'),
    path('exportar_excel/', views.exportar_excel, name='exportar_excel'),

]
