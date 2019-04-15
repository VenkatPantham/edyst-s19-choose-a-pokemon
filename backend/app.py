from flask import Flask,jsonify

app=Flask(__name__)

@app.route('/api/pokemon')
def pokemon():
    pokemon=['bulbasaur','charmander','squirtle']
    return jsonify(pokemon)

if(__name__=='__main__'):
    app.run(host='localhost',port=8206,debug=True)
