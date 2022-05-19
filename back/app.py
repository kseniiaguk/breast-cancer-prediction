import glob
import os

from flask import Flask, Response, jsonify, request, abort

import classification
import features
UPLOAD_FOLDER = '/imgs'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'there is no file in form!'
        file1 = request.files['file']
        directory = os.path.join(os.path.dirname(__file__), 'imgs\\')
        if not os.path.exists(directory):
            os.mkdir(directory)
        path = os.path.join(directory, file1.filename)
        file1.save(path)
        if not os.path.exists(path):
            abort(404)
        else:
            response = Response(status=201)
            return response


@app.route('/analyze', methods=['POST'])
def analyze():
    if not request.json:
        abort(404)
    list_of_files = glob.glob(os.path.join(os.path.dirname(__file__), 'imgs\\*'))  # * means all if need specific format then *.csv
    img = max(list_of_files, key=os.path.getctime)
    jdata = request.get_json()
    method = str(jdata['method'])
    classifyer = str(jdata['classifyer'])
    if method == 'hu':
        cols, data = features.get_hu(img)
        x = classification.prepare_data(cols, data)
        if classifyer == 'ada':
            pred = classification.glcm_ada(x)
        if classifyer == 'rf':
            pred = classification.glcm_rf(x)
        if classifyer == 'mlp':
            pred = classification.glcm_mlp(x)
        if classifyer == 'knn':
            pred = classification.glcm_knn(x)
    if method == 'glcm':
        cols, data = features.get_glcm(img)
        x = classification.prepare_data(cols, data)
        if classifyer == 'ada':
            pred = classification.glcm_ada(x)
        if classifyer == 'rf':
            pred = classification.glcm_rf(x)
        if classifyer == 'mlp':
            pred = classification.glcm_mlp(x)
        if classifyer == 'knn':
            pred = classification.glcm_knn(x)
    if method == 'law':
        cols, data = features.get_law(img)
        x = classification.prepare_data(cols, data)
        if classifyer == 'ada':
            pred = classification.glcm_ada(x)
        if classifyer == 'rf':
            pred = classification.glcm_rf(x)
        if classifyer == 'mlp':
            pred = classification.glcm_mlp(x)
        if classifyer == 'knn':
            pred = classification.glcm_knn(x)
    if method == 'zernike':
        cols, data = features.get_zernikes(img)
        x = classification.prepare_data(cols, data)
        if classifyer == 'ada':
            pred = classification.glcm_ada(x)
        if classifyer == 'rf':
            pred = classification.glcm_rf(x)
        if classifyer == 'mlp':
            pred = classification.glcm_mlp(x)
        if classifyer == 'knn':
            pred = classification.glcm_knn(x)
    if method == 'orb':
        cols, data = features.get_orb(img)
        x = classification.prepare_data(cols, data)
        if classifyer == 'ada':
            pred = classification.glcm_ada(x)
        if classifyer == 'rf':
            pred = classification.glcm_rf(x)
        if classifyer == 'mlp':
            pred = classification.glcm_mlp(x)
        if classifyer == 'knn':
            pred = classification.glcm_knn(x)
    if method == 'lbp':
        cols, data = features.get_lbp(img)
        x = classification.prepare_data(cols, data)
        if classifyer == 'ada':
            pred = classification.lbp_ada(x)
        if classifyer == 'rf':
            pred = classification.lbp_rf(x)
        if classifyer == 'mlp':
            pred = classification.lbp_mlp(x)
        if classifyer == 'knn':
            pred = classification.lbp_knn(x)
    pred = str(pred[0])
    return jsonify({"prediction": pred})


if __name__ == '__main__':
    app.run()
