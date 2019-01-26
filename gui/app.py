import os

import zbar
from PIL import Image

from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/app/static/uploads'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        f = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if f.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            f.save(filepath)
            scanner = zbar.ImageScanner()
            scanner.parse_config('enable')
            pil = Image.open(filepath).convert('L')
            width, height = pil.size
            raw = pil.tobytes()
            image = zbar.Image(width, height, 'Y800', raw)

            # scan the image for barcodes
            scanner.scan(image)
            # extract results
            results = []
            for symbol in image:
                # do something useful with results
                # copy data out? is this safe?
                results.append(dict(type=symbol.type,
                                    configs=symbol.configs,
                                    modifiers=symbol.modifiers,
                                    quality=symbol.quality,
                                    count=symbol.count,
                                    data=symbol.data,
                                    location=symbol.location,
                                    orientation=symbol.orientation,
                                    components=symbol.components
                                    ))

            # clean up
            del(image)
            return render_template('upload.html',
                                   filename='uploads/%s' % filename,
                                   results=results)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
