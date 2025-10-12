from flask import Flask, render_template, request
import struct
import numpy as np
import re
convert_expr = lambda s: re.sub(r'\bpi\b', 'np.pi',
                      re.sub(r'\^', '**',
                      re.sub(r'\bsqrt\s*\(', 'np.sqrt(',
                      re.sub(r'√\s*\(', 'np.sqrt(',
                      re.sub(r'\bexp\s*\(', 'np.exp(',
                      re.sub(r'\bcos\s*\(', 'np.cos(',
                      re.sub(r'\bsin\s*\(', 'np.sin(', s)))))))
float_to_bin64 = lambda x: format(struct.unpack('>Q', struct.pack('>d', x))[0], '064b')

def project_1_question_2_part_1(realNumberString):
    expr = convert_expr(realNumberString)
    if realNumberString == '':
        return ''
    try:
        result = eval(expr, {"__builtins__": {}}, {"np": np})
        return float_to_bin64(result)
    except Exception:
        return "Invalid Input for Real Number"

def project_1_question_2_part_2(binaryString):
    if binaryString == '':
        return ''
    try: return str(struct.unpack('>d', struct.pack('>Q', int(binaryString, 2)))[0])
    except Exception:
        return "Invalid Input for Binary"

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    text = ''
    input_type = "Real Valued Expression"
    example = "e.g. sqrt(2) or 3*pi"
    mode = request.form.get('mode', 'part_1')
    switch_type = 'Binary Input'
    if request.method == 'POST':
        text = request.form['user_input']

        if mode == 'part_1':
            func = project_1_question_2_part_1
            input_type = "Real Valued Expression"
            example = "e.g. sqrt(2) or 3*pi"
            switch_type = 'Binary Input'
        else:
            func = project_1_question_2_part_2
            input_type = "64-bit Binary String"
            example = "e.g. 0100000000001001001000011111101101010100010001000010110100011000"
            switch_type = 'Real Input'

        result = func(text)

    return render_template('index.html', result=result, user_input=text, input_type=input_type,
                           example=example, mode=mode, switch_type=switch_type)


if __name__ == '__main__':
    app.run()
