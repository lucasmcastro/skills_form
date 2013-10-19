from flask import Flask, render_template
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    skills = ['linux', 'python', 'javascript']
    return render_template('form.html',skills=skills)

if __name__ == '__main__':
    app.run()