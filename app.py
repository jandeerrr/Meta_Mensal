from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        desejo = request.form['desejo']
        meta_financeira = float(request.form['meta_financeira'].replace(',', ''))
        economia_mensal = float(request.form['economia_mensal'].replace(',', ''))

        if economia_mensal <= 0 or meta_financeira <= 0:
            raise ValueError("Os valores devem ser positivos.")

        tempo_necessario = meta_financeira / economia_mensal

        return render_template('resultado.html', economia_mensal=economia_mensal, meta_financeira=meta_financeira, tempo_necessario=int(tempo_necessario), desejo=desejo)

    except ValueError as e:
        return render_template('erro.html', mensagem=str(e))

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
