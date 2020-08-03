from flask import Flask, request, render_template
from data_sources.dao import DataAccessObjectFactory


app = Flask(__name__, static_url_path='', static_folder='templates')


@app.route('/')
def home_page():
    return "Welcome"


@app.route('/get_data_frame_data', methods=['GET'])
def get_pandas_data():
    data_frame_factory = DataAccessObjectFactory("DataFrame")
    data_frame = data_frame_factory.get_data_access_object()
    return {
        index: value for (index, value) in
        data_frame[request.args['column']][:int(request.args['rows'])].items()
    }


@app.route('/get_database_data', methods=['GET'])
def get_database_data():
    database_factory = DataAccessObjectFactory('Database')
    database = database_factory.get_data_access_object()
    return {
        index: value for (index, value) in
        enumerate(database.query_to_select_data(
            f'select last_name from actor limit %(rows)s',
            {"rows": request.args["rows"]}))
    }


@app.route('/get_drive_data', methods=['GET'])
def get_drive_data():
    spread_sheet_factory = DataAccessObjectFactory("SpreadSheet")
    sheet = spread_sheet_factory.get_data_access_object()
    if request.args:
        return {
            index: value for (index, value) in
            enumerate(sheet.col_values(request.args["column_number"]))
        }
    else:
        return {
            index: value for (index, value) in
            enumerate(sheet.get_all_records())
        }


@app.route('/post_form', methods=['GET'])
def post_form():
    return render_template('index.html')


@app.route('/post_data_frame', methods=['POST'])
def post_to_data_frame():
    data_frame_factory = DataAccessObjectFactory('DataFrame')
    data_frame = data_frame_factory.get_data_access_object()
    form_data = {key: eval(value) for (key, value) in
                 request.values.dicts[1].items()}
    data_frame.loc[len(data_frame)] = [
        str(len(data_frame) + 1),
        form_data['time'],
        form_data['value']]
    return "Success"


@app.route('/post_database', methods=['POST'])
def post_to_database():
    database_factory = DataAccessObjectFactory('Database')
    database = database_factory.get_data_access_object()
    form_data = {key: value for (key, value) in
                 request.values.dicts[1].items()}
    database.query_to_insert_data(
        f'insert into actor (first_name, last_name) '
        f'values (%(first)s, %(last)s)',
        {"first": form_data['first_name'], "last": form_data['last_name']})
    return "Success"


@app.route('/post_drive', methods=['POST'])
def post_to_drive():
    spread_sheet_factory = DataAccessObjectFactory('SpreadSheet')
    sheet = spread_sheet_factory.get_data_access_object()
    form_data = {key: value for (key, value) in
                 request.values.dicts[1].items()}
    sheet.insert_row(
        [form_data['product'], form_data['count']],
        len(sheet.get_all_values()) + 1)
    return "Success"


app.run(port=4995)
