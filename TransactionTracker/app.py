from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mystatement.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class Statement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50),nullable=False)
    name = db.Column(db.String(100),nullable=False)
    amount = db.Column(db.Integer,nullable=False)
    category = db.Column(db.String(50),nullable=False)

with app.app_context():
    db.create_all()


@app.template_filter()
def currencyFormat(amount):
    value = float(amount)
    return "{:,.2f}".format(value)

@app.route("/addForm")
def addForm():
    return render_template("addForm.html")

# recieve data from user's input/form via browser/client 
@app.route("/addStatement", methods=['POST'])
def addStatement():
    date = request.form["date"]
    name = request.form["name"]
    amount = request.form["amount"]
    category = request.form["category"]
    statement=Statement(date=date,name=name,amount=amount,category=category)
    db.session.add(statement)
    db.session.commit()
    return redirect("/")

# retrive data from the database and display on the web
@app.route("/")
def showData():
    statements = Statement.query.all()
    return render_template("statement.html", statements=statements)

# delete item from database via browser/client
@app.route("/delete/<int:id>")
def deleteStatement(id):
    statement = Statement.query.filter_by(id=id).first()
    db.session.delete(statement)
    db.session.commit()
    return redirect("/")

# edit item 
@app.route("/edit/<int:id>")
def editStatement(id):
    statement = Statement.query.filter_by(id=id).first()
    return render_template("editForm.html", statement=statement)

# update statements
@app.route("/updateStatement", methods=['POST'])
def updateStatement():
    id = request.form["id"]  # takes it from editForm.html which is hidden on the page
    date = request.form["date"]
    name = request.form["name"]
    amount = request.form["amount"]
    category = request.form["category"]
    # searching all value from recorded table
    statement = Statement.query.filter_by(id=id).first()
    # stored the new statement's values
    statement.date = date
    statement.name = name
    statement.amount = amount
    statement.category = category
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
