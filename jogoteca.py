from flask import Flask, render_template, request, redirect, session, flash, url_for

class Usuario:
    def __init__(self, nome, nick, senha):
        self.nome = nome
        self.nick = nick
        self.senha = senha

usuario1 = Usuario('Teste 1', 'ts', 'ts')
usuario2 = Usuario('Teste 2', 'ts1', 'ts1')
usuario3 = Usuario('Teste 3', 'bolo', 'bolo')


usuarios = {
    usuario1.nick: usuario1,
    usuario2.nick: usuario2,
    usuario3.nick: usuario3
}

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
    if ('usuario_logado' not in session or session['usuario_logado'] == None):
        return redirect(url_for('login', proxima = 'novo'))
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST', ])
def criar():
        nome = request.form['nome']
        categoria = request.form['categoria']
        console = request.form['console']
        jogo = Jogo(nome, categoria, console)
        lista.append(jogo)
        return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima  = request.args.get('proxima')
    return render_template('login.html', proxima = proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    login = request.form['usuario']
    senha = request.form['senha']
    if (login in usuarios):
        if (usuarios[login].senha == senha):
            session['usuario_logado'] = usuarios[login].nome
            flash(usuarios[login].nome + ' logou com sucesso!')
            return redirect(url_for('index'))
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None;
    flash('Usuario deslogado')
    return redirect(url_for('index'))

app.run(debug=True)
