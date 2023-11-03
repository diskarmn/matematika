from flask import Flask, render_template, request, jsonify

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')
@app.route('/kurang')
def kurang():
    return render_template('kurang.html')
@app.route('/kali')
def kali():
    return render_template('perkalian.html')
@app.route('/bagi')
def bagi():
    return render_template('pembagian.html')

@app.route('/penjumlahan', methods=['POST'])
def penjumlahan():
    data = request.get_json()
    bilangan1 = data.get('bilangan1')
    bilangan2 = data.get('bilangan2')
    hasil = bilangan1 + bilangan2
    return jsonify({'result': hasil})

@app.route('/pengurangan', methods=['POST'])
def pengurangan():
    data = request.get_json()
    bilangan1 = data.get('bilangan1')
    bilangan2 = data.get('bilangan2')
    hasil = bilangan1 - bilangan2
    return jsonify({'result': hasil})
    
    

@app.route('/perkalian', methods=['POST'])
def perkalian():
    data = request.get_json()
    bilangan1 = data.get('bilangan1')
    bilangan2 = data.get('bilangan2')
    hasil = bilangan1 * bilangan2
    return jsonify({'result': hasil})
@app.route('/pembagian', methods=['POST'])
def pembagian():
    data = request.get_json()
    bilangan1 = data.get('bilangan1')
    bilangan2 = data.get('bilangan2')
    hasil = bilangan1 / bilangan2
    return jsonify({'result': hasil})

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)
