from flask import Flask, render_template, request, current_app
from pymongo import MongoClient
import datetime
import os 

#vamos a colocarlo a un siito web 
def crear_app(): 
  
    app = Flask(__name__)
    cliente = MongoClient(os.getenv("MONGODB_URL"))
    app.db = cliente.blog_personal

  

    @app.route("/", methods=["GET", "POST"]) 

    def home(): 
      if request.method == "POST": 
        titulo = request.form.get("tit")
        contenido = request.form.get("content")
        fecha_formato = datetime.datetime.today().strftime("%d-%m-%Y")
        json = {"titulo": titulo, "contenido":contenido, "fecha":fecha_formato}

        current_app.db.entradas.insert_one(json)
        
      entradas = list(current_app.db.entradas.find({}))

      return render_template("index.html", entradas = entradas)
    
    return app
   


