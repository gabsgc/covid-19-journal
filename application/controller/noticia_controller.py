from flask import render_template, request
from application import app
from application.model.entity.noticia import Noticia
from application.model.dao.estado_dao import EstadoDAO

@app.route("/noticia/<int:id>")
def noticia(id: int):
    noticia = EstadoDAO().findNoticiaById(id)
    return render_template("noticia.html", noticia = noticia)