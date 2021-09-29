from flask import (Blueprint, request, render_template)
from .engine import encrypt, decrypt

bp = Blueprint('affine', __name__, url_prefix='/affine')

@bp.route('/', methods=('GET', 'POST'))
def index():
    data = {
        "mode": "encrypt",
        "input_key_a": "",
        "input_key_b": "",
        "input_text": "",
        "output_text": "",
        "output_style": "1"
    }

    if request.method == 'POST':
        mode = request.form['mode']
        input_text = request.form['input_text']
        key_a = int(request.form['input_key_a'])
        key_b = int(request.form['input_key_b'])
        output_style = request.form['output_style']

        data['mode'] = mode
        data['input_text'] = input_text
        data['input_key_a'] = key_a
        data['input_key_b'] = key_b
        data['output_style'] = output_style

        if mode == "encrypt":
            if (output_style == "1"):
                data['output_text'] = encrypt(
                    input_text, [key_a, key_b]).replace(" ", "")
            else:
                new_str = encrypt(input_text, [key_a, key_b]).replace(" ", "")

                data['output_text'] = ' '.join(
                    new_str[i:i+5] for i in range(0, len(new_str), 5))
        else:
            data['output_text'] = decrypt(
                input_text, [key_a, key_b]).replace(" ", "")

        return render_template('affine/index.html', data=data)

    return render_template('affine/index.html', data=data)