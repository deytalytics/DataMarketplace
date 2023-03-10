from flask import Flask, Response, request, render_template
from fetch_restapi_json import fetch_restapi_json
from fetch_restapi_csv import fetch_restapi_csv
from fetch_metadata import fetch_metadata

prod_tmp_url='https://data-container.azurewebsites.net/'
dev_url = 'http://127.0.0.1:8000/'
url = prod_tmp_url

app = Flask(__name__)

query = "select * from data_products dp"
dp_metadata = fetch_metadata(query)

query = "select ds.name as data_source_name, dsa.name as dsa_name, url_suffix from data_product_data_sources ds, data_source_data_sharing_agreements dsa where dsa.data_source_id=ds.id"
data_src_metadata = fetch_metadata(query)

query = "select * from target_datasets td, target_dataset_versions tdv where tdv.ds_id = td.id"
dataset_metadata = fetch_metadata(query)


@app.route('/')
def home_page():
    return render_template('home_page.html',url=url)

@app.route('/permitted_data_products')
def permitted_data_products():
    return render_template('permitted_data_products.html',url=url,dp_metadata=dp_metadata, dataset_metadata=dataset_metadata, data_src_metadata=data_src_metadata)

@app.route('/dataset')
def dataset():
    args=request.args
    ds_id=int(args['ds_id'])
    ds_version_id=int(args['ds_version_id'])
    for ds in ds_metadata:
        if (ds['ds_id'] == ds_id and ds['id'] == ds_version_id):
            found_ds = ds
            break
    return render_template('dataset.html',url=url,dataset=found_ds)

@app.route('/fetch_json')
def fetch_json():
    username = "Mary"
    password = "tiger"
    args=request.args
    ds_name=args['name']
    ds_version=args['version']
    json_url=url+"ds/%s/%s"%(ds_name,ds_version)
    return fetch_restapi_json(json_url, username, password)

@app.route('/fetch_csv')
def fetch_csv():
    username = "Mary"
    password = "tiger"
    args=request.args
    ds_name=args['name']
    ds_version=args['version']
    csv_url=url+"ds/%s/%s"%(ds_name,ds_version)
    csv=fetch_restapi_csv(csv_url, username, password)
    return Response(csv,mimetype="text/csv",headers={"Content-disposition":
                 "attachment; filename=continents-0.1.csv"})

if __name__ == '__main__':
    app.run()
