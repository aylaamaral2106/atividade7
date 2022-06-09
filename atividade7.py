from flask import Flask

app = Flask(__name__)

@app.route("/notasmedias/<y>/<x>/<a>")
def notasmedias(y,x,a):
    soma=float(y)+float(x)+float(a)
    notasformatadas=soma/3
    if(notasformatadas>=60):
       return "Você foi aprovado."
    else(notasformatadas<60):
        return "Você foi reprovado."
