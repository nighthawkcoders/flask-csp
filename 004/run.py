from flask import Flask, render_template, flash

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField,  BooleanField, SubmitField
from wtforms.validators import DataRequired

from flask_sqlalchemy import SQLAlchemy

from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class Item(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), index=True)
    price = db.Column(db.Float)
    in_stock = db.Column(db.Boolean)
    
    def __repr__(self):
        return f'<Item: {self.name}>'

    


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/products')
def products():

    product_list = Item.query.all()

    return render_template("products.html", product_list=product_list)


@app.route('/search')
def product_search():
    return render_template("search.html")



class AddProductForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    price = FloatField('price', validators=[DataRequired()])
    in_stock = BooleanField('in stock')
    submit = SubmitField("update")

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = AddProductForm()

    if form.validate_on_submit():

        name = form.name.data
        price = form.price.data
        in_stock = form.in_stock.data

        new_item = Item(name=name, price=price, in_stock=in_stock)
        db.session.add(new_item)
        db.session.commit()

        flash(f"Product '{form.name.data}' saved successfully! ")


    return render_template("admin.html", form=form)



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)