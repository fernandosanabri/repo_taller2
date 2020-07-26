from flask import Flask, jsonify, request

app = Flask(__name__)

from empresas import empresas
from servicios import servicios

# Testing Route
@app.route('/servicios',methods=['GET'])
def getServicios():
    return jsonify({'servicios': servicios})

# Get Data Routes
@app.route('/empresas')
def getEmpresas():
    # return jsonify(empresas)
    return jsonify({'empresas': empresas})


@app.route('/empresas/<string:empresa_name>')
def getempresa(empresa_name):
    empresasFound = [empresa for empresa in empresas if empresa['name'] == empresa_name.lower()]
    if (len(empresasFound) > 0):
        return jsonify({'empresa': empresasFound[0]})
    return jsonify({'message': 'empresa Not found'})

# Create Data Routes
@app.route('/empresas', methods=['POST'])
def addEmpresa():
    new_empresa = {
        'name': request.json['name'],
        'price': request.json['price'],
        'quantity': 10
    }
    empresas.append(new_empresa)
    return jsonify({'empresas': empresas})

# Update Data Route
@app.route('/empresas/<string:empresa_name>', methods=['PUT'])
def editEmpresa(empresa_name):
    empresasFound = [empresa for empresa in empresas if empresa['name'] == empresa_name]
    if (len(empresasFound) > 0):
        empresasFound[0]['name'] = request.json['name']
        empresasFound[0]['price'] = request.json['price']
        empresasFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'empresa Updated',
            'empresa': empresasFound[0]
        })
    return jsonify({'message': 'empresa Not found'})

# DELETE Data Route
@app.route('/empresas/<string:empresa_name>', methods=['DELETE'])
def deleteEmpresa(empresa_name):
    empresasFound = [empresa for empresa in empresas if empresa['name'] == empresa_name]
    if len(empresasFound) > 0:
        empresas.remove(empresasFound[0])
        return jsonify({
            'message': 'empresa Deleted',
            'empresas': empresas
        })

if __name__ == '__main__':
    app.run(debug=True)
