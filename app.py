from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <img src="/static/blockM.png"/>
        <h1>Michigan Sports Info!</h1>
        <ul>
            <li><a href="/bball"> Men's Basketball </a></li>
        </ul>
    '''

## the default method is that it excepts "get" (like get.requests) and nothing else


# def bball():
#     return render_template("seasons.html", seasons=model.get_bball_seasons())


 ##we can the route to accept two different kinds (will be a post if they submit the form)
@app.route('/bball', methods=['GET', 'POST'])  
def bball():  
    # need to be able to post on the url, so adding that in
    if request.method == 'POST':
        sortby = request.form['sortby']
        sortorder = request.form['sortorder']
        seasons = model.get_bball_seasons(sortby, sortorder)
    else:
        seasons = model.get_bball_seasons()
        
    return render_template("seasons.html", seasons=seasons)



@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
    else:
        firstname = ''
        lastname = ''

    return render_template("hello.html", firstname= firstname, lastname= lastname)


@app.route('/fball', methods=['GET', 'POST'])  
def fball():  
    # need to be able to post on the url, so adding that in
    if request.method == 'POST':
        sortby = request.form['sortby']
        sortorder = request.form['sortorder']
        seasons = model.get_football_seasons(sortby, sortorder)
    else:
        seasons = model.get_football_seasons()
        
    return render_template("seasons.html", seasons=seasons)


if __name__ == '__main__':
    model.init_bball()
    # print(model.get_bball_seasons())
    model.init_football()
    app.run(debug=True, port=8080)
