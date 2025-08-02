from flask import Flask, render_template, request, redirect, url_for, flash
from forms import RegistrationForm

app = Flask(__name__)
app.secret_key  = "my-secret-key"

@app.route("/", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash(f"Registration successful for {name} with email {email}!", "success")
        
        return redirect(url_for("success", name=name, email=email))
    return render_template("register.html", form=form)


@app.route("/success")
def success():
    name = request.args.get('name')
    email = request.args.get('email')
    return render_template("success.html", name=name, email=email)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
