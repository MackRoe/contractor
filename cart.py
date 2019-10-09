
class Cart()
    def __init__(self):
        self.add_to_cart = None #bool
        

@app.route("/cart.html")
def cart():
    """ renders cart page - R of CRUD """
    return render_template('cart.html', cart=cart.find())

def create_cart_item():
    pass


def update_cart_item():
    pass

def remove_cart_item():
    pass
