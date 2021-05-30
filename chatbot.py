import os


def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}. Redes(TCP/IP), programação(Python ou Javascript é uma boa ideia), sistemas operacionais(Linux ou Windows), arquitetura de computadores e pilares de segurança{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}. Um blue team ou equipe azul é um grupo de especialistas em segurança da informação que tem uma visão de dentro para fora da organização.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}. Um red team ou equipe vermelha é um grupo de profissionais de segurança que atua como adversários, para derrubar ou contornar os controles de segurança cibernética. {os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}. A programação é um dos pré-requisitos mais importantes para ingressar na área pois essa te ajudar a entender como a aplicação funciona e a partir disso o profissional conseguir explorar as falhas ou até mesmo criar um exploit.{os.linesep}')
    else:
        return start()
        


def start():
    # Apresentar o chatbot
    print('Olá! Bem-vindo ao chatBot de Segurança da Informação.')
    # pedir o nome
    nome = input('Digite seu nome: ')
    
    # pedir o e-mail
    email = input('Digite seu e-mail: ')
  
    while True:
        # Oferer o menu de opções
        resposta = input(
            f'Qual sua dúvida sobre Segurança da Informação{os.linesep}[1] - O que preciso aprender para entrar na área de segurança da informação?{os.linesep}[2] - Desejo saber o que é um BLUE team. {os.linesep}[3] - Desejo saber o que é RED team. {os.linesep}[4] - Preciso aprender programação para entrar na área de segurança?{os.linesep}[5] - Digite qualquer caracter para sair.{os.linesep}')
        # Processar a resposta enviada
        processar_resposta(resposta, nome)


if __name__ == '__main__':
    start()