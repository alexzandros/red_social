# -*- coding: utf-8 -*-

def encuentra_mis_amigos(mi_id):
    amigos = list()
    lista_amigos = db(db.amistad.amigo2 == mi_id)
    for amigo in lista_amigos.select():
        otro_nombre = db.auth_user(amigo.amigo1).first_name
        amigos.append((otro_nombre,amigo.amigo1))

    lista_amigos = db(db.amistad.amigo1 == mi_id)
    for amigo in lista_amigos.select():
        otro_nombre = db.auth_user(amigo.amigo2).first_name
        amigos.append((otro_nombre,amigo.amigo2))
        
    return amigos
