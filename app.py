from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>list quelques artist id/jingles maker que tu connais : . list quelques artists/radio stations dans ta region.</p><p>creer ton simple profile, avec les simple info : nom, age, nationalite</p><p>maintenant cree ton AI digital ID comme pour voyager et crée ton identite d'artiste digital, ajouter un job, un artist name, un artist ID, un artist ID/jingle maker, number of points(face id), gender, ethcnicity</p>"
