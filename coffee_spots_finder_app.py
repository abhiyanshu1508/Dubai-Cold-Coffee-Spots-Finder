import streamlit as st
import pandas as pd
from geopy.distance import geodesic
from datetime import datetime

st.set_page_config("Dubai Cold Coffee Finder")

st.title("☕ Dubai Cold Coffee Finder")
st.subheader("Nearest Coffee Spots")

df = pd.read_csv("./dubai_cold_coffee_spots_clean.csv")
 
def calculate_dis(user_location,spot_location):
    return round(geodesic(user_location,spot_location).km,2)


def is_open_now(opening_time,closing_time):
    current_time = datetime.now().strftime("%H:%M")
    return opening_time <= current_time <= closing_time

with st.sidebar:
    st.title("Search Filters")
    st.subheader("Find Best Coffee Spots!")

    user_lat = st.number_input("Enter latitude:",25.20)
    user_lng = st.number_input("Enter longitude:",55.27)

    is_open = st.checkbox("is open",False)
    max_distance = st.slider("Max Distanse",1,20,10)
    spot_type = st.selectbox("Spot Type",["All","cart","cafe","truck"])

# user_location = (user_lat,user_lng)
# df["max_dis"]= df.apply(lambda row: calculate_dis(user_location,(row["lat"],row["lng"])),axis=1)
# df["is_open"] = df.apply(lambda row: is_open_now(row["opening_time"],row["closing_time"]),axis=1)

# if type == "All":
#     data = df
# else:
#     data = df[df["type"] == type]

# st.dataframe(data)


data = []
if spot_type == "All":
    data = df
else:
    data = df[df["type"] == spot_type]

def calculate_dis(user_location,spot_location):
    return round(geodesic(user_location,spot_location).km,2)


user_location=(25.2,55.2)
df["distance"]=df.apply(
    lambda row: calculate_dis(
        user_location,(row["lat"],row["lng"])),axis=1
        )
st.dataframe(data)
