from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/calculonotas', methods=['GET', 'POST'])
def calculonotas():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])
        resultado1 = round((nota1 + nota2 + nota3)/3)
        if asistencia >= 75 and resultado1 >= 40:
            resultado2 = 'APROBADO'
        else:
            resultado2 = 'REPROBADO'
        return render_template('calculonotas.html', resultado1=resultado1, resultado2=resultado2)
    return render_template('calculonotas.html')


@app.route('/largonombres', methods=['GET', 'POST'])
def largonombres():
    if request.method == 'POST':
        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])

        # Obtención largo de cadena
        long_nom1 = len(nombre1)
        long_nom2 = len(nombre2)
        long_nom3 = len(nombre3)

        if long_nom1 > long_nom2 and long_nom1 > long_nom3:
            resultado1 = nombre1
            resultado2 = long_nom1

        elif long_nom2 > long_nom1 and long_nom2 > long_nom3:
            resultado1 = nombre2
            resultado2 = long_nom2

        else:
            resultado1 = nombre3
            resultado2 = long_nom3
        return render_template('largonombres.html', resultado1=resultado1, resultado2=resultado2)
    return render_template('largonombres.html')


if __name__ == '__main__':
    app.run(debug=True)
