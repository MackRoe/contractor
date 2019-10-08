import pandas as pd
import pymongo
import json
import os

""" python template to import a CSV file into mongodb:
    code credit to Loginworks Softwares Inc, 4870 Sadler Road,
    Suite 300-Office 319 Glen Allen, VA 23060"""

 
def import_csvfile(/data/AG_Complete_Files.csv):
    mng_client = pymongo.MongoClient('localhost', 27017)
    mng_db = mng_client['contractor/db'] # Replace mongo db name
    collection_name = 'products' # Replace mongo db collection name
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)
    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)



if __name__ == "__main__":
 filepath = 'AG_Complete_Files.csv' # pass csv file path
 import_csvfile(filepath)