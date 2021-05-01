from application import app
from flask import render_template
from application.model.entity.estado import Estado
from application.model.dao.estado_dao import EstadoDAO
from application.model.entity.noticia import Noticia

@app.route("/")
def index():
    estado_list = EstadoDAO().findAll()

    noticia1 = EstadoDAO().findNoticiaById(3)
    noticia2 = EstadoDAO().findNoticiaById(2)
    noticia3 = EstadoDAO().findNoticiaById(1)

    noticia_list = [noticia1, noticia2, noticia3]

    return render_template('index.html', estado_list = estado_list, noticia_list = noticia_list)