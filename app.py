from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

cor1 = '#D32F2F'  #vermelho
cor2 = '#FFDEAD'  #pêssego
cor3 = '#FFFFFF'  #branco
cor4 = '#000000'  #preto

@app.route('/', methods=['GET', 'POST'])
def tela1():
    if request.method == 'POST':
        nome1 = request.form['nome1']
        nome2 = request.form['nome2']
        escolha1 = request.form['escolha1']
        escolha2 = request.form['escolha2']

        if not nome1 or not nome2:
            return render_template('index.html', error='Por favor, preencha os campos!')
        
        return redirect(url_for('tela2', nome1=nome1, nome2=nome2, escolha1=escolha1, escolha2=escolha2))
    return render_template('index.html')

@app.route('/perguntas', methods=['GET', 'POST'])
def tela2():
    if request.method == 'POST':
        pergunta1 = request.form['pergunta1']
        pergunta2 = request.form['pergunta2']
        pergunta3 = request.form['pergunta3']
        pergunta4 = request.form['pergunta4']

        return redirect(url_for('tela3', pergunta1=pergunta1, pergunta2=pergunta2, pergunta3=pergunta3, pergunta4=pergunta4))
    
    return render_template('perguntas.html')

@app.route('/resultado')
def tela3():
    pergunta1 = request.args.get('pergunta1')
    pergunta2 = request.args.get('pergunta2')
    pergunta3 = request.args.get('pergunta3')
    pergunta4 = request.args.get('pergunta4')

    pontuacao = 0

    if pergunta1 == 'Sim':
        pontuacao += 20
    if pergunta2 == 'Sim':
        pontuacao += 20
    if pergunta3 == 'Sim':
        pontuacao += 20
    if pergunta4 == 'Sim':
        pontuacao += 20

    if pergunta1 == 'Não':
        pontuacao -= 5
    if pergunta2 == 'Não':
        pontuacao -= 5
    if pergunta3 == 'Não':
        pontuacao -= 5
    if pergunta4 == 'Não':
        pontuacao -= 5

    compatibilidade = min(100, max(0, pontuacao + random.randint(0, 20)))

    if compatibilidade < 40:
        imagem = 'triste.png'
        texto = 'Vocês não têm muito em comum!'
    elif compatibilidade > 40 and compatibilidade <= 70:
        imagem = 'medio.png'
        texto = 'Com paciência pode dar certo!'
    else:
        imagem = 'feliz.png'
        texto = 'Vocês são um casal perfeito!'

    return render_template('resultado.html', compatibilidade=compatibilidade, texto=texto, imagem=imagem)

if __name__ == '__main__':
    app.run(debug=True)