from flask import Flask, request, render_template
import re

app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"
app.config['DEBUG'] = True


@app.route("/", methods=["GET", "POST"])
def valadation():
      if request.method == 'POST':            
         name = request.form['username']
         pass1 = request.form['password']
         verify = request.form['verify']
         email = request.form['email']
         validated = validate(name, pass1, verify, email)
         
         if validated[0]:
            return render_template("welcome.html", name=name)
         else:
               return render_template("signup.html", name=name, email=email, username_error=validated[1], password_error = validated[2], verify_password_error=validated[3], email_error=validated[4])
      return render_template("signup.html")

def validate_field(field):
      match = re.search(r'^((?!\s).){3,20}$', field)
      if match:             
            return True
      else:
            return False
            
def validate(name, pass1, verify, email=""):
      error = "That's not a valid"
      usernameError = ""
      passwordError = ""
      verifyError = ""
      emailError = ""
      valid = True

      if not validate_field(name):
            usernameError = error + " username"
            valid = False
      if not validate_field(pass1):
            passwordError = error + " password"
            valid = False
      if not validate_field(verify) or not pass1 == verify:
            verifyError = "Passwords do not match"
            valid = False
      if len(email) > 0 or not email == "": 
            if not re.search(r'^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$', email):
                  emailError = error + " email" 
                  valid = False
      return [valid, usernameError, passwordError, verifyError, emailError]
      

            

      

              






app.run()


