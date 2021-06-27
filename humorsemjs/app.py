from flask import Flask, app, render_template

app = Flask(__name__)

@app.route("/<status>")
def index(status=None):
    nome = "Jim"
    sobrenome = "Coffee"
    idade = 40

    if status == "coffee":
        coffee = True
        #http://127.0.0.1:5000/coffee
    else :
        coffee = False
        #http://127.0.0.1:5000/semcoffee

    imagem_cafe = "https://memeguy.com/photos/thumbs/mrw-i-finally-get-my-girlfriend-on-reddit-and-her-first-post-does-infinitely-better-than-al-combined-45182.gif"
    imagem_sem_cafe = "https://media1.tenor.com/images/9c0645bbcabd5404e2779f9b22b840b9/tenor.gif?itemid=15444898"

    return render_template('index.html', nome = nome, sobrenome = sobrenome, idade = idade, coffee = coffee,
    imagem_cafe = imagem_cafe, imagem_sem_cafe = imagem_sem_cafe)

if (__name__ == "__main__"):
    app.run(debug=True)



