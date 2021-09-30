from flaskr.substitution.encrypt import encrypt
from flask import (Blueprint, request, render_template)
from .encrypt import encrypt
from .decrypt import decrypt

bp = Blueprint('substitution', __name__, url_prefix='/substitution')

@bp.route('/', methods=('GET', 'POST'))
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

        return render_template('substitution/index.html', data=data)

    return render_template('substitution/index.html', data=data)