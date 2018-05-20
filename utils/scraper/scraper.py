#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

nombres = {
    u"educación infantil": "inf",
    u"educación secundaria obrigatoria": "eso",
    u"educación primaria": "prim",
    u"ciclos formativos": "fp",
    u"bacharelato": "bac",
    u"ciclos formativos de grao medio": "medio",
    u"formación profesional básica": "basica",
    u"ciclos formativos de grao superior": "superior",
    u"educación secundaria para persoas adultas": "esa",
    u"educación especial": "esp",
    u"ensinanzas superiores de música": "mus-sup",
    u"grao superior música": "mus-sup",
    u"grao medio música": "mus-med",
    u"ensinanzas de música": "mus",
    u"ciencias": "ciencias",
    u"artes": "artes",
    u"humanidades e ciencias sociais": "humanidades",
    u"ensinanzas básicas iniciais":"ebi",
    u"ensinanzas de idiomas": "idiomas",
    u"ensinanzas superiores de deseño": "sup-desenho",
    u"ensinanzas profesionais de artes plásticas e deseño": "prof-art-des",
    u"ciclos formativos de grao superior de artes plásticas e deseño": "sup",
    u"ciclos formativos de grao medio de artes plásticas e deseño": "med",
    u"ensinanzas superiores de arte dramática": "sup-drama"
}

def get_todos_datos_centro (cod):
    session = requests.Session()
    session.get("https://www.edu.xunta.es/centroseducativos")
    datos = get_datos_centro(cod, session)
    oferta_educativa = get_oferta_educativa_centro(cod, session)
    outros = get_outrosdatos_centro (cod, session)
    datos["oferta"] = oferta_educativa
    datos["servizos"] = outros["servizos"]
    datos["xornada"] = outros["xornada"]
    return datos


def get_datos_centro (cod, session):
    ret = {}
    r = session.get("https://www.edu.xunta.es/centroseducativos/CargarDetalleCentro.do?codigo=" + cod)
    soup = BeautifulSoup(r.text, "html.parser")
    ret["nombre"] = soup.find("input", attrs={"name": "nome"})["value"]
    ret["enderezo"] = soup.find("input", attrs={"name": "enderezo.enderezo"})["value"]
    ret["localidade"] = soup.find("input", attrs={"name": "enderezo.localidade.nome"})["value"]
    ret["concello"] =soup.find("input", attrs={"name": "enderezo.concello.nome"})["value"]
    ret["cp"] = int(soup.find("input", attrs={"name": "enderezo.CP"})["value"])
    ret["provincia"] = soup.find("input", attrs={"name": "enderezo.provincia.nome"})["value"]
    ret["telefono"] = soup.find("input", attrs={"name": "contacto.telefono"})["value"]
    ret["fax"] = soup.find("input", attrs={"name": "contacto.fax"})["value"]
    #Obtenemos todas las imagenes y buscamos aquella que tenga de textoAimaxe como direccion.
    #try:
    #    email_image_src = filter(lambda t: "textoAimaxe" in t["src"], soup.find_all("img"))[0]["src"]
    #    get_imagen(cod, email_image_src, session)
    #except:
    #    return
    #return
    ret["web"] = soup.find("input", attrs={"name": "contacto.www"})["value"]
    return ret

def get_oferta_educativa_centro (cod, session):
    ret = {}
    r = session.get("https://www.edu.xunta.es/centroseducativos/CargarOfertaCentro.do?codigo=" + cod)
    soup = BeautifulSoup(r.text, "html.parser")
    lista = soup.find_all("tr")[1:]
    item = lista.pop(0)
    while True:
        nombretop = item.find("td").text.lower()
        if nombretop in nombres:
            nombretop = nombres[nombretop]
        if not nombretop in ret:
            ret[nombretop] = {}
        if not lista:
            return ret
        item = lista.pop(0)
        while item["class"][1] == "arbolNivel1":
            nombremid = item.find("td").text
            if nombremid.lower() in nombres:
                nombremid = nombres[nombremid.lower()]
            if not nombremid in ret[nombretop]:
                ret[nombretop][nombremid] = []
            if not lista:
                return ret
            item = lista.pop(0)
            while item["class"][1] == "arbolNivel2":
                nombrebot = item.find("td").text
                if nombrebot not in ret[nombretop][nombremid]:
                    ret[nombretop][nombremid].append(nombrebot)
                if not lista:
                    return ret
                item = lista.pop(0)


def get_outrosdatos_centro (cod, session):
    ret = {}
    r = session.get("https://www.edu.xunta.es/centroseducativos/CargarServizosComplementarios.do?codigo=" + cod)
    soup = BeautifulSoup(r.text, "html.parser")
    servicios_inputs = soup.find_all("input")
    ret["servizos"] = []
    for s in servicios_inputs:
        try:
            if ( s["checked"] != "checked"):
                continue
            ret["servizos"].append(s["name"][9:])
        except KeyError:
            continue
    xornada_tr = soup.find_all("tr")[1:]
    ret["xornada"] = {}
    for xor in xornada_tr:
        if xor["class"][0] == "empty":
            break
        campos = xor.find_all("td")
        edu = campos[0].getText().lower()
        if edu in nombres:
            edu = nombres[edu]
        ret["xornada"][edu] = campos[1].getText().lower()
    return ret


def get_imagen (cod, img_url, session):
    from subprocess import call
    r = session.get('https://www.edu.xunta.es' + img_url)
    with open("./center_email/" + cod + ".png", "wb") as f:
        f.write(r.content)


import json
import codecs
with codecs.open('centros.json', "r",'utf-8') as f:
    content = f.read()

result = []
centros = json.loads(content, "utf-8")

index = 0
step=10

while index < len(centros):
    index_end = index + step
    if (index_end > len(centros)):
        index_end = len(centros)
        print "FILE START - %i - %i" % (index, index_end)
    for c in centros[index:index_end]:
        print c[u"Nome"]
        datos = get_todos_datos_centro (unicode(c[u"Código"]))
        result.append({
            "cod": c[u"Código"],
            "nome": c[u"Nome"],
            "enderezo": c[u"Enderezo"],
            "concello": c[u"Concello"],
            "provincia": c[u"Provincia"],
            "cp": c[u"Cód. postal"],
            "tlf": c[u"Teléfono"],
            "web": datos["web"],
            "coordenadas": {
                "lat": c[u"COORDENADA_X"],
                "lon": c[u"COORDENADA_Y"]
            },
            "ensinanzas": datos["oferta"],
            "servizos": datos["servizos"],
            "xornada": datos["xornada"]
        })

    result_json = json.dumps(result, ensure_ascii=False)

    with codecs.open("centros-final-" + str(index / step) + ".json", "w", "utf-8") as f:
        f.write(result_json)
    print "FILE END!\n\n"
    index = index_end
