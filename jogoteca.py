from flask import Flask, render_template, request, redirect, session, flash
import sqlite3 as sql


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Teatris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.secret_key = 'gatinho manhoso'

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogo', jogos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST', ])
def criar():
        nome = request.form['nome']
        categoria = request.form['categoria']
        console = request.form['console']
        jogo = Jogo(nome, categoria, console)
        lista.append(jogo)
        return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    senha = request.form['senha']
    if 'gato' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso!')
        return redirect('/')
    else:
        flash('Usuário não logado.')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None;
    flash('Usuario deslogado')
    return redirect('/')

app.run(debug=True)
