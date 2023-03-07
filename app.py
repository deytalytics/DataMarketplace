from flask import Flask, Response,render_template
from fetch_restapi_json import fetch_restapi_json
from fetch_restapi_csv import fetch_restapi_csv
from fetch_metadata import fetch_metadata

prod_tmp_url='https://data-container.azurewebsites.net/'
dev_url = 'http://127.0.0.1:8000/'
url = prod_tmp_url

app = Flask(__name__)

query = "select * from data_products dp, dp_docs d where d.dp_id = dp.id"
dp_metadata = fetch_metadata(query)

query = "select * from target_datasets td, target_dataset_versions tdv where tdv.ds_id = td.id"
ds_metadata = fetch_metadata(query)


@app.route('/')
def home_page():
    return render_template('home_page.html',url=url)

@app.route('/permitted_data_products')
def permitted_data_products():
    return render_template('permitted_data_products.html',url=url,dp_metadata=dp_metadata, ds_metadata=ds_metadata)

@app.route('/continents-0.1')
def datasets():
    return render_template('continents-0.1.html',url=url)

@app.route('/continents-0.1.json')
def fetch_json():
    username = "Mary"
    password = "tiger"
    return fetch_restapi_json(url + 'ds/continents/0.1', username, password)

@app.route('/continents-0.1.csv')
def fetch_csv():
    username = "Mary"
    password = "tiger"
    csv=fetch_restapi_csv(url + 'ds/continents/0.1', username, password)
    return Response(csv,mimetype="text/csv",headers={"Content-disposition":
                 "attachment; filename=continents-0.1.csv"})

if __name__ == '__main__':
    app.run()
