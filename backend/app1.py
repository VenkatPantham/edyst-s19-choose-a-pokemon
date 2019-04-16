from flask import Flask
import requests

app=Flask(__name__)

@app.route('/api/pokemon/<id>',methods=['GET','POST'])
def id(id):
    return redirect('https://pokeapi.co/api/v2/pokemon/'+id)