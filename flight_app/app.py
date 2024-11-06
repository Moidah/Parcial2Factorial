from flask import Flask, render_template, request
from math import factorial

app = Flask(__name__)


class Flight:
    id_counter = 1

    def __init__(self, name, flight_type, price):
        self.id = Flight.id_counter
        Flight.id_counter += 1
        self.name = name
        self.flight_type = flight_type
        self.price = price

flights = [
    Flight("Vuelo a Bogotá", "Nacional", 300),
    Flight("Vuelo a Miami", "Internacional", 700)
]

@app.route("/flights")
def list_flights():
    return render_template("flights.html", flights=flights)


@app.route("/factorial/<int:number>")
def show_factorial(number):
    result = factorial(number)
    return render_template("factorial.html", number=number, result=result)

if __name__ == "__main__":
    app.run(debug=True)
