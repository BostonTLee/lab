# Import flask and datetime module for showing date and time
from flask import Flask, request, jsonify
import datetime
from models import TestData
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
  
x = datetime.datetime.now()
  
# Initializing flask app
app = Flask(__name__)
  

@app.route('/test-data')
def get_data():
    test_data_id = request.args.get('id', type=int)
    # Returning an api for showing in  reactjs
    engine = create_engine('sqlite:////home/boston/test.db?check_same_thread=False')

    # create session and add objects
    #with Session(engine) as session:
    #    stmt = select(TestData).where(TestData.id == test_data_id)
    #    result = session.execute(stmt)
    #    print(result)
    session = Session(engine, future=True)
    result = session.query(TestData).filter_by(id=test_data_id)
    return jsonify({"data": result[0].data})

@app.route('/test-insert')
def get_input_data():
    test_data_value = request.args.get('data', type=str)
    # Returning an api for showing in  reactjs
    engine = create_engine('sqlite:////home/boston/test.db?check_same_thread=False')

    # create session and add objects
    #with Session(engine) as session:
    #    stmt = select(TestData).where(TestData.id == test_data_id)
    #    result = session.execute(stmt)
    #    print(result)
    session = Session(engine, future=True)
    test_data = TestData(data=test_data_value)
    result = session.add(test_data)
    session.flush()
    session.commit()
    return jsonify({"inserted_id": test_data.id})

      
# Running app
if __name__ == '__main__':
    app.run()
