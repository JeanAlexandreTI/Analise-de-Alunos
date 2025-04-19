# %%
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

def analise_alunos():

    dados = {
        'Matricula' : ['202294', '202244', '202290', '202245'],
        'Nome Aluno' : ['Paula', 'Pedro', 'Roberto', 'Julia'],
        'Prova 01' : [10, 7, 8, 5], 
        'Prova 02' : [8, 8, 9, 7],
        'Prova 03' : [9, 7, 6, 3]
    }

    nota_media = []
    status = []
    for i in range(len(dados['Matricula'])):
        # dados['Matricula'][i]
        # dados['Nome Aluno'][i]
        nota_media.append(((dados['Prova 01'][i] + dados['Prova 02'][i] + dados['Prova 03'][i]) / 3))
        
    for i in range(len(dados['Matricula'])):
        
        print(dados['Nome Aluno'][i], end = ' - ')

        if nota_media[i] > 6:
            status.append('Aprovado')
            print('Aprovado')
        else:
            status.append('Reprovado')
            print('Reprovado')

    df = pd.DataFrame(dados, index = None)
    df['Media'] = nota_media
    df['Status'] = status

    data_sistema = dt.datetime.now()
    df.to_excel(f'Analise Alunos_{data_sistema.date()}.xlsx')

    # Exibir grafico
    plt.title('Media dos Alunos')
    plt.xlabel('Nome Aluno')
    plt.ylabel('Media')
    plt.bar(df['Nome Aluno'], df['Media'])
    plt.show()

analise_alunos()
