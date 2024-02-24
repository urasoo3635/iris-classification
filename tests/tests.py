import pytest
import pandas as pd
import datarobot_predict as drp


@pytest.fixture()
def test_data():
    datapath = ROOT_DIR / 'data' / 'iris_test.csv'
    df = pd.read_csv(datapath)
    data_json = df.loc[0].to_json()
    
    return data_json


def test_datarobot_predict(test_data):
    """DataRobot APIのリアルタイム推論
    """
    predictions = drp.datarobot_predict(test_data)
    print(predictions)

    assert True