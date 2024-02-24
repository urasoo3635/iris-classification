import json
import time
import datetime
import streamlit as st
from datarobot_predict import datarobot_predict


def main():
    """メイン関数
    """
    st.title("アヤメの品種分類")
    st.markdown('## 特徴量を入力')
    id = datetime.datetime.now().strftime(
        '%Y%m%d%H%M%S'
    )
    sepal_length = st.number_input('がくの長さ', min_value=4.0, max_value=8.0)
    sepal_width = st.number_input('がくの幅', min_value=2.0, max_value=5.0)
    petal_length = st.number_input('花びらの長さ', min_value=1.0, max_value=7.0)
    petal_width = st.number_input('花びらの幅', min_value=0.1, max_value=3.0)

    if st.button('推論実行'):
        # data to json
        target_data_dict = [
            {
                "ID": id,
                "sepal_length": sepal_length,
                "sepal_width": sepal_width,
                "petal_length": petal_length,
                "petal_width": petal_width
            }
            ]
        target_data_json = json.dumps(target_data_dict)

        # predict
        predictions_dict = datarobot_predict(target_data_json)

        predict_label = predictions_dict['data'][0]['prediction']
        probability_list = predictions_dict['data'][0]['predictionValues']
        probability = 0.0
        for value in probability_list:
            if value['label'] == predict_label:
                probability = value['value']
            else:
                pass

        time.sleep(3)

        # 結果を表示
        st.markdown('## 推論結果')
        st.markdown(f'#### 品種 {predict_label}')
        st.markdown(f'#### 確率 {probability}')

    else:
        pass

    if st.button('リセット'):
        st.experimental_rerun()
    else:
        pass

    return


if __name__ == "__main__":
    main()