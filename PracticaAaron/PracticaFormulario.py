from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

mails = {
    "Mercedes": "mcast386@xtec.cat",
    "Rayane": "rayane@rayane.sa",
    "Mohamed": "moha@gmail.com",
    "Jad": "jad@gmail.com",
    "Oriol": "joam@gmail.com",
    "Elias": "hola123@gmail.com",
    "Armau": "arnau@gmail.com",
    "Asdrúbal": "asdrubal@gmail.com",
    "Adrian": "pedrosanchez@asix2.com",
    "Eric": "eric@gmail.com",
    "Emma": "pacosanz@gmail.com",
    "nishwan": "nishwan@gmail.com",
    "Javi": "javi@gmail.com",
    "Novel": "novelferreras49@gmail.com",
    "Bruno": "elcigala@gmail.com",
    "David": "argentino@gmail.com",
    "Judit": "judit@gmail.com",
    "Joao": "joao@gmail.com",
    "Laura": "laura@gmail.com",
    "enrico": "123@gmail.com",
    "Joel": "joelcobre@gmail.com",
    "Aaron": "aaron@gmail.com",
    "Moad": "moad@gmail.com"
}


@app.route('/getmail', methods=['GET', 'POST'])
def get_mail():
    if request.method == 'POST':
        name = request.form['name']

        if name in mails:
            email = mails[name]
            return render_template('getmailresultado.html', result=f'Correo de {name}: {email}')
        else:
            return render_template('getmailresultado.html', result=f'Nombre no encontrado: {name}')

    return render_template('getmailformulario.html')

@app.route('/addmail', methods=['GET', 'POST'])
def add_mail():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        mails[name] = email

        return render_template('addmailresultado.html', result=f'Se ha añadido correctamente: {name} - {email}')

    return render_template('addmail.html')

if __name__ == '__main__':
    app.run(debug=True)
