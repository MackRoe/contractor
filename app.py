from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os


host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/contractor')
client = MongoClient(host=f'{host}?retryWrites=false')
# db = client.Contractor
db = client.get_default_database()
products = db.products
cart = db.cart
members = db.members
url_base = "https://www.azuregreen.net/images/"


""" PROPS AND CREDS TO DAVID EVANS FOR BIG BUNCHES OF HELP """





# img_ref = products.find_one({'_id': ObjectID(img_ref)})
# img_url = url_base + img_ref # get help


app = Flask(__name__)

@app.route("/")
def products_index():
    """ renders front page of site and shows featured products """
    # load_catalog() # -- comment out to save for later --
    title = "Witch Store"
    return render_template('store_index.html', products=products.find())


@app.route("/main.html")
def main():
    """renders main from base """
    return render_template("base.html")


@app.route("/signup")
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


@app.route('/<product_id>')
def show_product(product_id):
    """ show individual product detail """
    product = products.find_one({'_id': ObjectId(product_id)})
    return render_template('product.html', product=product)


@app.route('/new_product')
def product_new():
    """Allow user to create a product"""
    return render_template('product_create.html')


@app.route('/product_create', methods=["POST"])
def product_create():
    """Create a product"""
    product = {
        'name': request.form.get('name'),
        'desc': request.form.get('desc'),
        'price': request.form.get('price')
    }
    product_id = products.insert_one(product).inserted_id
    return redirect(url_for('show_product', product_id=product_id))


@app.route('/<product_id>/delete', methods=["POST"])
def product_delete(product_id):
    """Delete a product"""
    products.delete_one({"_id": ObjectId(product_id)})
    return redirect(url_for('product_index'))


@app.route('/product_list')
def product_index():
    """Show all products."""
    return render_template('product_list.html', products=products.find())


@app.route('/<product_id>/edit')
def product_edit(product_id):
    """Show the form to edit a product"""
    product = products.find_one({"_id": ObjectId(product_id)})
    return render_template('product_edit.html', product=product)


@app.route('/<product_id>/edit', methods=["POST"])
def product_update(product_id):
    """Allow a user to update a product"""
    updated_product = {
        'name': request.form.get('name'),
        'desc': request.form.get('desc'),
        'price': request.form.get('price')
    }
    products.update_one(
        {"_id": ObjectId(product_id)},
        {"$set": updated_product})
    return redirect(url_for('show_product', product_id=product_id))


@app.route("/cart")
def cart():
    """ renders cart page - R of CRUD """
    cart_id = cart.insert_one(cart).inserted_id
    return render_template('cart.html', cart=cart)  # removed .find() from =cart

@app.route("/updated_cart")
def create_cart_item():
    """ if prod_code submit then add to cart """
    if input request.form.get('buy') == True:
        print('buy ==' + str(buy))
        cart_item = {
            'name': request.cart.get('name'),
            'price': request.cart.get('price')
            }
            # TODO: create print statement to confirm prod name and price are passed 
            # correctly to the function/method
            #
        cart.update_one(
            {'_id': ObjectId(cart_id)},
            {'$set': cart_item})
    return render_template('cart_item_list.html', cart=cart)


@app.route('/<cart_id>/edit', methods=["POST"])
def cart_item_update(cart_id):
    """Allow user to update a cart item"""
    updated_cart_item = {
        'name': request.form.get('name'),
        'quantity': request.form.get('quantity'),
        'price': request.form.get('price')
    }
    products.update_one(
        {"_id": ObjectId(cart_id)},
        {"$set": updated_cart_item})
    return redirect(url_for('cart_item_list.html', cart_id=cart_id))


@app.route('/<cart_id>/delete', methods=["POST"])
def cart_item_delete(product_id):
    """Delete a product"""
    cart.delete_one({"_id": ObjectId(cart_id)})
    return redirect(url_for('/cart'))
    
# def calc_cart_total():
#     pass

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
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
    
    # -- saving for later scaling --
    # load_catalog()