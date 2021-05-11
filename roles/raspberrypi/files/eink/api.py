from datetime import datetime
import requests
import matplotlib.pyplot as plt


clinton_hill_lat_lon = (40.686594, -73.968502)
clinton_hill_points = "34,33"
base_url = "https://api.weather.gov/"


def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0

def forecast_properties():
    response = requests.get(
        f"{base_url}/gridpoints/OKX/{clinton_hill_points}/forecast"
    )
    return response.json()["properties"]


class Forecast:
    def __init__(self, name, time, is_daytime, fahrenheit, celsius):
        self.name = name
        self.time = time
        self.is_daytime = is_daytime
        self.fahrenheit = fahrenheit
        self.celsius = celsius


def forecast_summary(forecast):
    periods = forecast["periods"]
    for period in periods:
        name = period["name"]
        time = datetime.strptime(period["startTime"][:-6], "%Y-%m-%dT%H:%M:%S")
        is_daytime = period["isDaytime"]
        fahrenheit = period["temperature"]
        yield Forecast(
            name,
            time, #.strftime("%H/%d/%m/%Y")
            is_daytime,
            fahrenheit,
            to_celsius(fahrenheit),
        )


def plot(periods):
    periods.pop()  # make the list shorter
    X = range(len(periods))
    Y = [period.fahrenheit for period in periods] # (A list comprehension)
    average = sum(Y) / len(Y)
    plt.plot(X,Y)
    plt.xticks(X, [period.name for period in periods], rotation=45)
    for idx, period in enumerate(periods):
        plt.annotate(
            f"{period.fahrenheit}℉ {period.celsius:.2f}℃", xy=(idx, period.fahrenheit),
            xytext=(-3, 1*3), textcoords="offset points",
            horizontalalignment="right",
            verticalalignment="bottom" if period.fahrenheit > average else "top",
            rotation=45,
        )
    plt.ylim(min(Y) * 0.91, 1.08 * max(Y))


def save_png(filename):
    plt.figure(figsize=(8, 8))

    plot(list(forecast_summary(forecast_properties())))

    plt.savefig(filename)


if __name__ == "__main__":
    save_png("plot.png")
