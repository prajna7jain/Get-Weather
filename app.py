from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve



app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        # You could render "City Not Found" instead like we do below
        city = "Mumbai"

    weather_data = get_current_weather(city)

        # City is not found by API
    if weather_data.get('cod') != 200:
        return render_template('notfound.html')


    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )


if __name__ == "__main__":
    app.run(debug=True)

# if __name__ == "__main__":
#     app.run(debug=True, host="127.0.0.1", port=8000)
