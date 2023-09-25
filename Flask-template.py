from flask import request, Flask, render_template, redirect



app = Flask(__name__)
# Disable caching for static files
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = None



@app.route("/")
def hello_world():
    return "Hello World!"



@app.route("/template")
def status_page():

    return render_template('template.html', 
                            arg1="Hello", arg2="World")



@app.route('/redirect')
def new_project_redir():

    return redirect("https://www.google.com")



app.run()