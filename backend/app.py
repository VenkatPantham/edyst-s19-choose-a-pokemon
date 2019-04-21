from flask import Flask,json,render_template

app=Flask(__name__)                                                 # Initialising Flask

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.route('/api/pokemon')
def pokemon():
    data={}
    data['pokemon']=["bulbasaur","charmander","squirtle"]           # Storing data into a variable
    return json.dumps(data)                                            # Returning required JSON Data

if(__name__=='__main__'):
    app.run(host='localhost',port=8006)
