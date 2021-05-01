from application import app
from flask import render_template
from application.model.entity.estado import Estado
from application.model.dao.estado_dao import EstadoDAO

@app.route("/")
def index():
    estado_list = EstadoDAO().findAll()

    return render_template('index.html', estado_list = estado_list)