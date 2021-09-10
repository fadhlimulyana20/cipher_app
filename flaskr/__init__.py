import os
from flask import Flask, render_template, request
from decrypt import decrypt
from encrypt import encrypt


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/', methods=('GET', 'POST'))
    def index():
        data = {
            "mode": "encrypt",
            "input_shift": "",
            "input_text": "",
            "output_text": "",
            "output_style": "1"
        }

        if request.method == 'POST':
            mode = request.form['mode']
            input_text = request.form['input_text']
            shift = int(request.form['input_shift'])
            output_style = request.form['output_style']

            data['mode'] = mode
            data['input_text'] = input_text
            data['input_shift'] = shift
            data['output_style'] = output_style

            if mode == "encrypt":
                if (output_style == "1"):
                    data['output_text'] = encrypt(
                        input_text, shift).replace(" ", "")
                else:
                    new_str = encrypt(input_text, shift).replace(" ", "")

                    data['output_text'] = ' '.join(
                        new_str[i:i+5] for i in range(0, len(new_str), 5))
            else:
                data['output_text'] = decrypt(
                    input_text, shift).replace(" ", "")

            return render_template('index.html', data=data)

        return render_template('index.html', data=data)

    return app
