import random
import sys

if len(sys.argv) == 2:
    try:
        quantidade_provas = int(sys.argv[1])
        if int(sys.argv[1]) > 500:
            raise ValueError
    except ValueError:
        print('Argumento inválido.')
        exit()

elif len(sys.argv) == 1:
    quantidade_provas = 35
else:
    print('Foram passados muitos argumentos')
    exit()


capitais = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia':
            'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
            'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky':
            'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
            'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska':
            'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon':
            'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina':
            'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin',
            'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington':
            'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

cabecalho = '''Nome:
Data:
Série:
<<<<<<<<<<<<<<<<<<<<<<<<<<PROVA DE GEOGRAFIA>>>>>>>>>>>>>>>>>>>>>>>>>>


'''

for cada_uma in range(1, quantidade_provas + 1):
    # preenche o cabeçalho e limpa o arquivo
    with open('provas\\Prova ' + str(cada_uma) + '.txt', 'w') as prova:
        prova.write(
            cabecalho + f'==========================     PROVA  {cada_uma}     ==========================\n')

    with open('gabaritos\\Gabarito ' + str(cada_uma) + '.txt', 'w') as gabarito:  # limpa o arquivo
        gabarito.write('')
    estados = list(capitais.keys())
    random.shuffle(estados)
    for k, estado in enumerate(estados):
        alternativas = []
        alternativas.append(capitais[estado])
        for diferentes in range(3):
            escolhido = random.choice(list(capitais.values()))
            while escolhido == capitais[estado] or escolhido in alternativas:
                escolhido = random.choice(list(capitais.values()))
            else:
                alternativas.append(escolhido)

        random.shuffle(alternativas)
        resposta = alternativas.index(capitais[estado])
        with open('provas\\Prova ' + str(cada_uma) + '.txt', 'a') as prova:
            prova.write(f'''Questão {k+1}: Qual é a capital do estado de {estado}?
    A) {alternativas[0]}
    B) {alternativas[1]}
    C) {alternativas[2]}
    D) {alternativas[3]}

''')
        alternativas_letras = ['A', 'B', 'C', 'D']
        with open('gabaritos\\Gabarito ' + str(cada_uma) + '.txt', 'a') as gabarito:
            gabarito.write(f'{k + 1}) {alternativas_letras[resposta]}\n')

print(f'{quantidade_provas} provas criadas.')
