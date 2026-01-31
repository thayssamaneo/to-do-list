from flask import render_template, request, redirect, url_for
from models.listadb import lista, db

class ListaController:
    @staticmethod
    def index():
        if request.method == 'POST':
            tarefa = request.form['tarefa']
            descricao = request.form['descricao']
            prioridade = request.form['prioridade']
            nova_Tarefa = lista(tarefa=tarefa, descricao=descricao, prioridade=prioridade)
            db.session.add(nova_Tarefa)
            db.session.commit()
            
            return redirect(url_for('index'))

        listaTarefas = lista.query.all()
        return render_template('index.html', listaTarefas=listaTarefas)
    
    @staticmethod
    def excluir(id):
        tarefa_para_excluir = lista.query.get(id)
        if tarefa_para_excluir:
            db.session.delete(tarefa_para_excluir)
            db.session.commit()
        return redirect(url_for('index'))