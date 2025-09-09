from flask import Flask, render_template, request
app = Flask(__name__, template_folder='template')

# Emission factors in kg CO₂ per liter
emission_factors = {
    'petrol': 2.31,
    'diesel': 2.68,
    'lpg': 1.51
}
@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        fuel_type = request.form['fuel_type']
        try:
            liters = float(request.form['liters'])
            if fuel_type.lower() in emission_factors:
                co2_emitted = liters * emission_factors[fuel_type.lower()]
                result = f"CO₂ Emitted: {co2_emitted:.2f} kg"
            else:
                result = "Invalid fuel type."
        except ValueError:
            result = "Please enter a valid number for liters."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
