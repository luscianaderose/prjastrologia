from flask import Flask

@app.route('/')
def get_home():
    head = '''<head>
    </head>'''

    banner = ''

    barra_menu = '<div class="barra-menu"></div>'

    texto = 'Hello, world!'

    rodape = '© Criado em 2024. Todos os direitos reservados.'

    return head + banner + barra_menu + texto + rodape


