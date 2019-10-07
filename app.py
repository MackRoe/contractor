from flask import Flask
from flask import render_template
from pymongo import MongoClient
client = MongoClient()
db = client.Contractor
product_catalog = db.product_catalog
# product_catalog = read(AG_Contractor_Files.csv)

app = Flask(__name__)

@app.route("/")
def products_index():
    # message = "Hello World"
    
    # load_catalog() # -- comment out to debug --
    title = "Buy This Stuff"
    return render_template('index.html', title=title)
    # --- removed from return ---
    # product_catalog=product_catalog.find()
    # --- ----- ----- ----- ----- ---

def load_catalog():
    f = open('AG_Complete_Files.csv', 'r')
    products = f.readlines()
    f.close()
    products = products[0].split(',')
    products = list(products)


def catalog_sort():
    # sort items from AG_Complete_Files.csv
    # as either product codes or product descriptions
    pass


if __name__ == "__main__":
    app.run(debug=True)
    load_catalog()