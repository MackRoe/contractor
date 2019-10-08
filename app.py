from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/contractor')
client = MongoClient()
db = client.Contractor # may not be correct name
products= db.products
url_base = "https://www.azuregreen.net/images/"


client = MongoClient(host=f'{host}?retryWrites=false')

db = client.get_default_database()



# img_ref = products.find_one({'_id': ObjectID(img_ref)})
# img_url = url_base + img_ref # get help


app = Flask(__name__)

@app.route("/")
def products_index():
    # message = "Hello World"
    
    # load_catalog() # -- comment out to save for later --
    title = "Witch Store"
    return render_template('store_index.html', title=title)


@app.route("/cart.html")
def cart():
    """ renders cart page """
    return render_template('cart.html')


@app.route("/main.html")
def main():
    """renders main from base ?"""
    return render_template("base.html")


@app.route("/signup.html")
def signup():
    """ renders signup page """
    return render_template("signup.html")

# HELP! ... app.route(what?)
@app.route('/members.txt', methods=['POST'])
def signup_submit():
    """Submit a new profile"""
    new_user = {
        "user_name": request.form.get("user_name"),
        "user_email": request.form.get("user_email")
    }
    # --- what to do with input data ?? ---
    # print(request.form.to_dict()) -- NO
    return redirect(url_for('main'))


@app.route('/product.html')
def show_product():
    return render_template(product.html)


def create_cart_item():
    pass

def show_cart_item():
    pass

def update_cart_item():
    pass

def remove_cart_item():
    pass

# ---- not this time Tilda ----
# def load_catalog():
#     f = open('AG_Complete_Files.csv', 'r')
#     products = f.readlines()
#     f.close()
#     products = products[0].split(',')
#     products = list(products)


# def catalog_sort():
#     # sort items from AG_Complete_Files.csv
#
#     pass
# -- -- -- -- -- -- -- -- -- --


if __name__ == "__main__":
    app.run(debug=True)
    # load_catalog()