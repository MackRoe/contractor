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
    # --- commented out experimental code ---
    # f = open('AG_Complete_Files.csv', 'r')
    # product_catalog_items = f.readlines()
    # f.close()
    # product_catalog = product_catalog[0].split(',')
    # product_catalog = list(product_catalog)
    # --- end commented out code ---
    title = "Buy This Stuff"
    return render_template('index.html', title=title)
    # --- removed from return ---
    # product_catalog=product_catalog.find()
    # --- ----- ----- ----- ----- ---



if __name__ == "__main__":
    app.run(debug=True)