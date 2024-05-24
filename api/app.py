from flask import Flask, jsonify
import routeros_api

app = Flask(__name__)

# إعداد الاتصال بجهاز MikroTik
connection = routeros_api.RouterOsApiPool(
    '172.16.0.1', 
    username='admin', 
    password='password'
)
api = connection.get_api()

@app.route('/vlan_data', methods=['GET'])
def get_vlan_data():
    vlan_data = api.get_resource('/interface/vlan').get()
    return jsonify(vlan_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
