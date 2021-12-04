from flask import Flask, render_template, session, request, redirect
from APIManager import API



app = Flask(__name__)

# Secret key
app.secret_key = 'asdfs'

# Config
app.config['configDB'] = {
    'host': '127.0.0.1',
    'user': 'filmUser',
    'password': 'filmuserpasswd',
    'database': 'FilmDB'
}


'''Home url has by default 6 films'''

@app.route('/')
@app.route('/home', methods=['POST', 'GET'] )
def home():
    
    # Default films

    defaultFilm = {"static/images/akk.png": 'akk', "static/images/joker.png": 'joker',
    "static/images/squidgame.png": 'squid game',  "static/images/badboys.png": 'bad boys',
    "static/images/Titanic.png": 'Titanic', "static/images/Thor.png": 'Thor', }

    filmData = {}

    for k in defaultFilm:
        api = API(app.config['configDB'],  defaultFilm[k]  )

        if api.exist():
            filmData[ api.data[2] ] = {k: defaultFilm[k]}
            
    
    return render_template('home.html', the_title="Home", data=filmData)



'''Show url'''

@app.route("/show", methods=['POST', 'GET'])
def show():

    keys = ('Released', 'Genre', 'Director', 'Writer', 'Actors', 'Awards')
    dic = {}

    # If there is a POST
    if request.method == 'POST':
        api = API(app.config['configDB'], request.form['title'] )

        if api.exist():
            title = api.data[0]
            imageLink = api.data[1]

            # Pop the first to element in the list
            api.delete2()

            # Here create the dict
            for x in range( len(keys) ):
                dic[ keys[x] ] = api.data[x]
        else:
            if api.execute():
                imageLink = api.path
                title = api.title

                # Call the funtion (addToList ) in API
                api.addToList()

                # Create the dict
                for x in range( len(keys) ):
                    dic[ keys[x] ] = api.data[x]
            else:

                # When the film doesn't exist just redirect to home
                return redirect("home")
    else:
        # When was not a POST just redirect to home
        return redirect("home")
        
    
    return render_template('show.html', title="Show", film_title=title, image= imageLink,
    data=dic)


'''Joker url'''

@app.route("/joker")
def joker():
    keys = ('Released', 'Genre', 'Director', 'Writers', 'Actors', 'Awards')
    dic = {}

    api = API(app.config['configDB'], 'joker' )

    if api.exist():
        title = api.data[0]
        imageLink = api.data[1]
        
        # Pop the first to element in the list
        api.delete2()

        # Here create the dict
        for x in range( len(keys)):
            dic[ keys[x] ] = api.data[x]
    
    
    return render_template('show.html', title="Show", film_title=title, image= imageLink,
    data=dic)


'''Akk url'''

@app.route("/akk")
def akk():
    keys = ('Released', 'Genre', 'Director', 'Writers', 'Actors', 'Awards')
    dic = {}

    api = API(app.config['configDB'], 'akk' )

    if api.exist():
        title = api.data[0]
        imageLink = api.data[1]
        
        # Pop the first to element in the list
        api.delete2()

        # Here create the dict
        for x in range( len(keys)):
            dic[ keys[x] ] = api.data[x]
    
    
    return render_template('show.html', title="Show", film_title=title, image= imageLink,
    data=dic)



'''squid game url'''

@app.route("/squid")
def squidGame():
    keys = ('Released', 'Genre', 'Director', 'Writers', 'Actors', 'Awards')
    dic = {}

    api = API(app.config['configDB'], 'squid game' )

    if api.exist():
        title = api.data[0]
        imageLink = api.data[1]
        
        # Pop the first to element in the list
        api.delete2()

        # Here create the dict
        for x in range( len(keys)):
            dic[ keys[x] ] = api.data[x]
    
    
    return render_template('show.html', title="Show", film_title=title, image= imageLink,
    data=dic)




'''Bad boys url'''

@app.route("/bad")
def badBoys():
    keys = ('Released', 'Genre', 'Director', 'Writers', 'Actors', 'Awards')
    dic = {}

    api = API(app.config['configDB'], 'bad boys' )

    if api.exist():
        title = api.data[0]
        imageLink = api.data[1]
        
        # Pop the first to element in the list
        api.delete2()

        # Here create the dict
        for x in range( len(keys)):
            dic[ keys[x] ] = api.data[x]
    
    
    return render_template('show.html', title="Show", film_title=title, image= imageLink,
    data=dic)



'''Titanic  url'''

@app.route("/Titanic")
def titanic():
    keys = ('Released', 'Genre', 'Director', 'Writers', 'Actors', 'Awards')
    dic = {}

    api = API(app.config['configDB'], 'Titanic' )

    if api.exist():
        title = api.data[0]
        imageLink = api.data[1]
        
        # Pop the first to element in the list
        api.delete2()

        # Here create the dict
        for x in range( len(keys)):
            dic[ keys[x] ] = api.data[x]
    
    
    return render_template('show.html', title="Show", film_title=title, image= imageLink,
    data=dic)



'''Thor  url'''

@app.route("/Thor")
def thor():
    keys = ('Released', 'Genre', 'Director', 'Writers', 'Actors', 'Awards')
    dic = {}

    api = API(app.config['configDB'], 'Thor' )

    if api.exist():
        title = api.data[0]
        imageLink = api.data[1]
        
        # Pop the first to element in the list
        api.delete2()

        # Here create the dict
        for x in range( len(keys)):
            dic[ keys[x] ] = api.data[x]
    
    
    return render_template('show.html', title="Show", film_title=title, image= imageLink,
    data=dic)


if __name__ == '__main__':
    app.run(debug=True)