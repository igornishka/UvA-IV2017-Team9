from flask import render_template
from app import app

import commons
import utils 


@app.route('/')
@app.route('/index')


def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]

    app.logger.warning("You've been warned")
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)


#TODO: I'm still not convinced that this is the way to handle data...
@app.route('/counts')
def counts():
    country_counts = commons.GTD_DATA.get_country_counts()
 
    app.logger.warning("Gonna print counts now")
    return render_template("counts.html",
                           country_counts=country_counts)


@app.route('/country/<country>')
def display_country(country):
    country_data = commons.GTD_DATA.get_country_data(country)
    country_data.update({'country': country})

    app.logger.warning("Gonna display country stuffs")
    return render_template("country.html",
                           country_data=country_data)


#TODO: it should be @app.route('/attack/<int:attack_id>')
@app.route('/attack')
def display_random_attack():
    attack_id = utils.generate_random_attack_id(commons.GTD_DATA.n_attacks)
    attack_data = commons.GTD_DATA.get_attack_data(attack_id)
    attack_data.update({'attack_id': attack_id})

    app.logger.warning("Gonna display a random attack now")
    return render_template("attack.html",
                           attack_data=attack_data)


@app.route('/map')
def map():
    attack_locations = commons.GTD_DATA.get_location()

    app.logger.warning("Gonna map counts now")
    return render_template("map.html",
                           attack_locations=attack_locations)