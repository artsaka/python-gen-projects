from flask import Flask, render_template, request,session,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey' # using the security
Bootstrap(app)

class UserInputForm(FlaskForm):
    name = StringField("Please enter your name: ", validators=[DataRequired()])
    isAccept = BooleanField("Accept all services on this website")
    gender = RadioField('Gender:', choices=[('male', 'ชาย'), ('female', 'หญิง'), ('other', 'อื่นๆ')])
    #dropdown using SelectField() method
    skill = SelectField('Skills:', choices=[('Painting', 'เพ้นท์ภาพ'), ('Music', 'ร้องเพลง'), ('Programming', 'เขียนโปรแกรม')])
    address = TextAreaField("Address:")
    submit = SubmitField("Submit")

@app.route('/', methods=['GET', 'POST'])
def index():
    name = False
    isAccept = False
    gender = False
    address = False
    skill = False
    # objects are sending to html file
    form = UserInputForm()    
    
    # data submition from the input fields, then display results back to the user / record them to database
    if form.validate_on_submit():
        flash("Data has been recorded successfully!")
        session['name'] = form.name.data
        session['isAccept'] = form.isAccept.data
        session['gender'] = form.gender.data
        session['skill'] = form.skill.data
        session['address'] = form.address.data    

        # clear data after display the selection
        form.name.data = ""
        form.isAccept.data = ""
        form.gender.data = ""
        form.address.data = ""
    return render_template("index.html", form=form, name=name, isAccept=isAccept, gender=gender, skill=skill, address=address)
    # return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True) # debug mode helps us detecting errors