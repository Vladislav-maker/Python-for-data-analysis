import streamlit as st
import pickle
import pandas as pd


# Заголовок приложения
st.set_page_config(
    page_title="Price House App",
)

st.title("Price House Prediction")

# Ввод данных
st.write("Enter the passenger details:")

# Выпадающее меню для выбора класса билета

square = st.sidebar.number_input("How total square of room do you want ?", 15, 200)
# pclass = st.selectbox("Total square", [1, 2, 3])
rooms = st.sidebar.number_input("How many rooms do you want ?",1, 10, 1)



model_path = 'model.pkl'

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Кнопка для отправки запроса
if st.button("Predict"):

    # Подготовка данных для отправки
    data = {
        "total_square": float(square),
        "rooms": float(rooms)
    }

    df = inputDF = pd.DataFrame(data, index=[0])
    prediction = model.predict(df)
    value = round(prediction[0])
    if value < 4_000_000:
        st.image('image_house1.jpg', use_column_width=True)

    elif value >= 4_000_000 and value < 10_000_000:
        st.image('image_house2.jpg', use_column_width=True)

    else:
        st.image('image_house3.jpg', use_column_width=True)

    st.write(f"Price of you house: {round(prediction[0])} руб.")








