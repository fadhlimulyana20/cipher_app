from flaskr.substitution.encrypt import encrypt
from flask import (Blueprint, request, render_template)
from .engine import encrypt, decrypt, generateKey

bp = Blueprint('vigenere', __name__, url_prefix='/vigenere')

@bp.route('/', methods=('GET', 'POST'))
def index():
    data = {
        "mode": "encrypt",
        "input_key": "",
        "input_text": "",
        "output_text": "",
        "output_style": "1"
    }

    if request.method == 'POST':
        mode = request.form['mode']
        input_text = request.form['input_text']
        key = request.form['input_key']
        output_style = request.form['output_style']

        data['mode'] = mode
        data['input_text'] = input_text
        data['input_key'] = key
        data['output_style'] = output_style
        input_text = input_text.replace(" ", "")
        generate_key = generateKey(input_text, key)

        if mode == "encrypt":
            cipher_text = encrypt(input_text, generate_key)

            if (output_style == "1"):
                data['output_text'] = cipher_text
            else:
                data['output_text'] = ' '.join(
                    cipher_text[i:i+5] for i in range(0, len(cipher_text), 5))
        else:
            plain_text = decrypt(input_text, generate_key)
            data['output_text'] = plain_text

        return render_template('vigenere/index.html', data=data)

    return render_template('vigenere/index.html', data=data)