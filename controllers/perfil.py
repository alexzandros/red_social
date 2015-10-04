# -*- coding: utf-8 -*-

@auth.requires_login() 
def index():
    return __organizar_datos_usuario(auth.user)

def downloads():
     return response.download(request, db)

@auth.requires_login()
def ver():
    id = request.args[0]
    usuario = db.auth_user(id)
    return __organizar_datos_usuario(usuario)

def __organizar_datos_usuario(usuario):
    nombre_completo = usuario.first_name + " " + usuario.last_name
    ruta_imagen =  URL('downloads',args = usuario.foto)
    return dict(nombre_completo = nombre_completo, 
                amigos = encuentra_mis_amigos(usuario.id),
                ruta_imagen = ruta_imagen)
