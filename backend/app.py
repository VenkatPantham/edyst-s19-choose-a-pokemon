from flask import Flask,jsonify

app=Flask(__name__)                                                 # Initialising Flask

@app.route('/api/pokemon')
def pokemon():
    pokemon=['bulbasaur','charmander','squirtle']                   # Storing data into a variable
    return jsonify(pokemon)                                         # Returning required JSON Data

if(__name__=='__main__'):
    app.run(host='localhost',port=8006,debug=True)
