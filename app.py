from flask import Flask, render_template, request, redirect, abort
import requests as superapi
app=Flask(__name__)
url='https://api-videojuegos-bc4d.onrender.com/api/videojuegos'
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method=='GET':
        print("entre al get")
        videojuegos=superapi.get(url).json()['videojuegos']
        response={"videojuegos":videojuegos}
        #print(response)
        return render_template("index.html", response=response)
    else:
        print("entre al post")
        titulo=request.form.get('titulo')
        print(titulo)
        videojuegos2=[]
        videojuegos=superapi.get(url).json()['videojuegos']
        for videojuego in videojuegos:
            if titulo==videojuego['titulo']:
                videojuegos2.append(videojuego)
            else:
                abort(404)
        response={"videojuegos":videojuegos2}
        return render_template('videogame.html', response=response)
        """try:
            #requests.post(url,json={"titulo":titulo,"desarrollador":desarrollador, "anio_lanzamiento":anio_lanzamiento, "plataforma":plataforma, "clasificacion":clasificacion})
            return redirect('/')
        except:
            return abort(500)"""

@app.route('/<string:titulo>', methods=['GET'])
def search_vg(titulo):
    #print(titulo)
    videojuegos2=[]
    if request.method=='GET':
        videojuegos=superapi.get(url).json()['videojuegos']
        for videojuego in videojuegos:
            if titulo==videojuego['titulo']:
                videojuegos2.append(videojuego)
        response={"videojuegos":videojuegos2}
        return render_template('videogame.html', response=response)
    else:
        abort(404)

if __name__=='__main__':
    app.run(debug=True)