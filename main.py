from flask import Flask
import random
import string

app = Flask(__name__)

curiosita = [
"La maggior parte delle persone che soffrono di dipendenza tecnologica sperimentano un forte stress quando si trovano al di fuori dell'area di copertura della rete o non possono utilizzare i loro dispositivi",
"Secondo uno studio condotto nel 2018, più del 50% delle persone di età compresa tra i 18 e i 34 anni si considera dipendente dal proprio smartphone",
"Lo studio della dipendenza tecnologica è una delle aree più rilevanti della ricerca scientifica moderna",
"Secondo uno studio del 2019, oltre il 60% delle persone risponde ai messaggi di lavoro sul proprio smartphone entro 15 minuti dall'uscita dal lavoro.",
"I social network hanno aspetti positivi e negativi e dobbiamo essere consapevoli di entrambi quando usiamo queste piattaforme.",
"Elon Musk sostiene che i social network sono progettati per tenerci all'interno della piattaforma, in modo che trascorriamo il maggior tempo possibile a guardare contenuti"
]


moneta = ["CROCE", "TESTA"]

@app.route("/")

def home():
    return f'<h1>Fatti interessanti sulle dipendenze tecnologiche!<a href="/fatto_casuale">Vedi un fatto casuale!</a>' f'<h1>Lancio della moneta!<a href="/lancio_moneta">Lancia la moneta!</a>' 

@app.route("/fatto_casuale")
def fatti_casuali():
    return f'<h1>{random.choice(curiosita)}</h1>'

@app.route("/lancio_moneta")
def lancio_moneta():
    return f'<h1>Ti è uscito:{random.choice(moneta)}</h1>'


app.run(debug=True)
