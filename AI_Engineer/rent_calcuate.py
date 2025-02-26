# RENT CALCULATION

# from flask import Flask, render_template, request

# app = Flask(__name__)


# # hostel = int(input("Enter the the total hostel rent per_month = "))
# # food = float(input("Enter the total bill of food in per_month = "))
# # person = int(input("Enter the total persone in room/flat = "))

# def calculate_electricity_bill(units_consumed, rate_per_unit, fixed_charge=0, tax_rate=0):
#     # Calculate the cost based on units consumed
#     cost = units_consumed * rate_per_unit

#     # Add fixed charge
#     total_cost = cost + fixed_charge

#     # Calculate tax
#     tax = (total_cost * tax_rate) / 100

#     # Add tax to the total cost
#     total_bill = total_cost + tax

#     return total_bill



# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         # Get input values from the form
#         units = float(request.form["units"])
#         rate = float(request.form["rate"])
#         fixed = float(request.form["fixed"])
#         tax = float(request.form["tax"])
#         hostel = int(request.form["hostel"])
#         food = float(request.form["food"])
#         person = int(request.form["person"])

#         # Calculate the electricity bill
#         bill = calculate_electricity_bill(units, rate, fixed, tax)

#         # Calculate the total rent per person
#         output_show = (hostel + food + bill) // person

#         # Render the result in the template
#         return render_template("result.html", output_show=output_show)

#     # Render the input form for GET requests
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)

















# # Input values
# units =float(input("Enter the number of units consumed: "))
# rate = float(input("Enter the rate per unit (in PKR): "))
# fixed = float(input("Enter the fixed charge (if any, in PKR): "))
# tax = float(input("Enter the tax rate (in %): "))

# # Calculate the bill
# bill = calculate_electricity_bill(units, rate, fixed, tax)
# # # Output the result
# # print(f"Your electricity bill is: ${bill:.2f}")

# hostel = int(input("Enter the the total hostel rent per_month = "))
# food = float(input("Enter the total bill of food in per_month = "))
# person = int(input("Enter the total persone in room/flat = "))

# output_show = (hostel + food + bill) // person
# print(f"Each person will pay = {output_show}") 










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