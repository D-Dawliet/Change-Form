from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # handle the form submission here
        return 'Form submitted!'
    return render_template('Certificate-Project.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    age = request.form.get('number')
    state = request.form.get('dropdown')
    change = request.form.get('choice-of-change')
    reason = request.form.get('why')
    improvements = request.form.getlist('what')
    extra_info = request.form.get('textarea')

    return f"""
    <body style="background: linear-gradient(90deg, rgba(0, 38, 255, 0.2), rgba(55, 0, 255, 0.2)), url(static/img-CP/background.png);
    background-repeat: no-repeat;
    background-size: cover;
    background-position: absolute;
    margin-bottom: 50px;">
    <h1 style="text-shadow: 0 0 3px black; margin-top: 30px; text-align: center; color: rgb(255, 255, 255);">Submission Details</h1>
    <div style="word-wrap: break-word; box-shadow: 0 0 5px black; border-radius: 7px; padding: 10px 20px; background-color: rgba(37, 82, 206, 0.5); width: 30%; margin-left: auto; margin-right: auto;">
        <p style="text-shadow: 0 0 2px; font-size: 23px;"><strong style="color: rgb(13, 5, 90);">Name:</strong> <span style="text-shadow: 0 0">{name}</span></p>
        <p style="text-shadow: 0 0 2px; font-size: 23px;"><strong style="color: rgb(13, 5, 90);">Email:</strong> <span style="text-shadow: 0 0">{email}</span></p>
        <p style="text-shadow: 0 0 2px; font-size: 23px;"><strong style="color: rgb(13, 5, 90);">Age:</strong> <span style="text-shadow: 0 0">{age}</span></p>
        <p style="text-shadow: 0 0 2px; font-size: 23px;"><strong style="color: rgb(13, 5, 90);">Current State:</strong> <span style="text-shadow: 0 0">{state}</span></p>
        <p style="text-shadow: 0 0 2px; font-size: 23px;"><strong style="color: rgb(13, 5, 90);">Sure about Change:</strong> <span style="text-shadow: 0 0">{change}</span></p>
        <p style="text-shadow: 0 0 2px; font-size: 23px;"><strong style="color: rgb(13, 5, 90);">Reason for Change:</strong> <span style="text-shadow: 0 0">{reason}</span></p>
        <p style="text-shadow: 0 0 2px; font-size: 23px;"><strong style="color: rgb(13, 5, 90);">Improvements:</strong> <span style="text-shadow: 0 0">{', '.join(improvements)}</span></p>
        <p style="text-shadow: 0 0 2px; font-size: 23px;"><strong style="color: rgb(13, 5, 90);">Additional Information:</strong> <span style="text-shadow: 0 0">{extra_info}</span></p>
    </div>
    """

if __name__ == '__main__':
    app.run(debug=True)
