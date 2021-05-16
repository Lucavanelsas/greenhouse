import datetime
import random

from flask import Flask, render_template
from utilities.conguration_file import *

app = Flask(__name__)


def generate_random_sensor_value():
    """
    This function generates a random value between 0 and 50.
    It is used for testing the website.
    """
    return random.randint(0, 50)


@app.route('/')
def greenhouse_homepage():
    """
    This function creates a homepage for the website.
    """
    humidity_value = generate_random_sensor_value()
    temperature_value = generate_random_sensor_value()
    wind_speed_value = generate_random_sensor_value()
    return render_template(HOMEPAGE_HTML,
                           humidity_value="{0}%".format(humidity_value),
                           temperature_value="{0}\u2103".format(temperature_value),
                           wind_speed_value="{0}\u2103".format(wind_speed_value))


@app.route('/blog')
def blog():
    """
    This function creates the blog page for the website.
    """
    return render_template(BLOG_HTML)


@app.route('/sensorGraphs')
def graphs_page():
    """
    This function creates the graphs page for the website.
    """
    return render_template(GRAPHS_HTML,
                           humidity_name=HUMIDITY,
                           humidity_picture=HUMIDITY_PICTURE_PATH,
                           temperature_name=TEMPERATURE,
                           temperature_picture=TEMPERATURE_PICTURE_PATH,
                           wind_speed_name=WIND_SPEED,
                           wind_speed_picture=WIND_SPEED_PICTURE_PATH)


if __name__ == '__main__':
    random.seed(datetime.datetime.now())
    app.run(debug=True, host=IP_ADDRESS)
