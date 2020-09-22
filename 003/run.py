from flask import Flask, render_template, flash

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField,  BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'shhh-dont-tell-anyone'


product_list = [
    {
        "name":"t-shirt",
        "price":15.0,
        "in_stock":True
    },

    {
        "name":"banana",
        "price":0.50,
        "in_stock":True
    },

    {
        "name":"mini-yacht",
        "price":150000.0,
        "in_stock":False
    },
    
]


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/products')
def products():

    return render_template("products.html", product_list=product_list)


# Not implemented
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

        print("name:", form.name.data)
        print("price:", form.price.data)
        print("in stock:", form.in_stock.data)

        new_product = {
            "name":form.name.data,
            "price":form.price.data,
            "in_stock":form.in_stock.data
        }

        product_list.append(new_product)

        flash(f"Product '{form.name.data}' saved successfully! ")


    return render_template("admin.html", form=form)



if __name__ == "__main__":
    app.run(debug=True)