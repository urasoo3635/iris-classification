import pytest
import pandas as pd
import json
import datarobot_predict as drp
from conftest import ROOT_DIR


@pytest.fixture()
def test_data():
    datapath = ROOT_DIR / 'data' / 'iris_test.csv'
    df = pd.read_csv(datapath)
    json_str = df.loc[:0].to_json(orient='records')

    return json_str


def test_datarobot_predict(test_data):
    """DataRobot APIのリアルタイム推論
    """

    predictions = drp.datarobot_predict(test_data)
    print("-------------")
    print(test_data)
    print("-------------")
    print(predictions)

    assert True