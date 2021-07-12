import python_weather
import asyncio

"""
Simple:
    Get current weather (CurrentForecast) (weather.current)
    Get forecast        (WeatherForecast) (forecast in weather.forecasts)
"""


async def getweather():
    # declare the client
    client = python_weather.Client(format=python_weather.IMPERIAL)
    weather = await(client.find("Renton"))
    # print(weather.current.temperature)
    current = weather.current
    # inside of CurrentForecast
    print(current.temperature)
    print(current.sky_code)
    print(current.sky_text)
    print(current.date)
    print(current.observation_point)
    print(current.feels_like)
    print(current.humidity)
    print(current.wind_display)
    print(current.day)
    print(current.short_day)
    print(current.wind_speed)

    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)

    await(client.close())

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())
