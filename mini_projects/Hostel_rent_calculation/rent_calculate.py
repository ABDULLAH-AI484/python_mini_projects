# RENT CALCULATION
from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_electricity_bill(units_consumed, rate_per_unit, fixed_charge=0, tax_rate=0):
    # Calculate the cost based on units consumed
    cost = units_consumed * rate_per_unit

    # Add fixed charge
    total_cost = cost + fixed_charge

    # Calculate tax
    tax = (total_cost * tax_rate) / 100

    # Add tax to the total cost
    total_bill = total_cost + tax

    return total_bill, cost, fixed_charge, tax

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get input values from the form
        units = float(request.form["units"])
        rate = float(request.form["rate"])
        fixed = float(request.form["fixed"])
        tax = float(request.form["tax"])
        hostel = int(request.form["hostel"])
        food = float(request.form["food"])
        person = int(request.form["person"])

        # Calculate the electricity bill and its sub-parts
        total_bill, cost, fixed_charge, tax_amount = calculate_electricity_bill(units, rate, fixed, tax)

        # Calculate the total rent per person
        output_show = (hostel + food + total_bill) // person

        # Render the result in the template with all details
        return render_template(
            "result.html",
            output_show=output_show,
            units=units,
            rate=rate,
            fixed_charge=fixed_charge,
            tax_rate=tax,
            cost=cost,
            tax_amount=tax_amount,
            total_bill=total_bill,
            hostel=hostel,
            food=food,
            person=person
        )

    # Render the input form for GET requests
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
