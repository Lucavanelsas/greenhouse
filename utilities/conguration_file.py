# STATIC PATH VALUES
GREENHOUSE_PATH = "D:/greenhouse/"  # "/home/pi/greenhouse/"

CODE_PATH = GREENHOUSE_PATH + "code/"
DATABASE_PATH = GREENHOUSE_PATH + "sensorData.db"
OUTPUT_PATH = CODE_PATH + "outputs/"
WEBSITE_PATH = GREENHOUSE_PATH + "website/"
PNG_OUTPUT_PATH = OUTPUT_PATH + "png/"
HOMEPAGE_HTML = "homepage.html"
BLOG_HTML = "blog.html"
GRAPHS_HTML = "graphs_page.html"

# STATIC SENSOR VALUES
HUMIDITY_PICTURE_PATH = PNG_OUTPUT_PATH + "humidity.png"
HUMIDITY = "Humidity"
HUMIDITY_GPIO = -1

TEMPERATURE_PICTURE_PATH = PNG_OUTPUT_PATH + "humidity.png"
TEMPERATURE = "Temperature"
TEMPERATURE_GPIO = -1

WIND_SPEED_PICTURE_PATH = PNG_OUTPUT_PATH + "wind_speed.png"
WIND_SPEED = "Wind speed"
WIND_SPEED_GPIO = -1

# STATIC RASPBERRY PI VALUES
IP_ADDRESS = "127.0.0.1"
