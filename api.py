from flask import Flask, jsonify
from downloader import download_dataset, search_datasets, get_github_files, get_github_file
from flask_cors import CORS


"""
    My api, run on pythonAnywhere
"""


app = Flask(__name__)
CORS(app)


@app.route('/', methods = ['GET'])
def home():
    data = "hello this is my api"
    return jsonify({'data': data})

@app.route('/search/<string:name>', methods=['GET'])
def search(name):
    data = search_datasets(name=f'q={name}')
    return jsonify({'data': data['data']})

@app.route('/download/<string:id>', methods=['GET'])
def download(id):
    data, geo = download_dataset(id=id)
    return jsonify({'data': data, 'geo': geo})

@app.route('/files', methods=['GET'])
def files():
    config, data, geo = get_github_files()
    return jsonify({'data': data, 'geo': geo, 'config': config})

@app.route('/file/<string:dir>/<string:subdir>/<string:file>', methods=['GET'])
def file(dir, subdir, file):
    data = get_github_file(dir, subdir, file)
    return jsonify({'data': data})

if __name__ == "__main__":
    app.run()