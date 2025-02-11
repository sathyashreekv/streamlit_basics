import streamlit as st
import random
st.title("welcome to my world")
user_text=st.text_input("enter some")
if user_text:
    st.write(f"the text entered : {user_text}")

upload_file=st.file_uploader("Upload any image",type=["jpg","png","jpeg"])
if upload_file:
    st.image(upload_file,caption="Uploaded Image",use_container_width=True)

fun=[
     "Bananas are berries, but strawberries aren't! 🍌",
    "Octopuses have three hearts. 🐙",
    "Honey never spoils. Archaeologists found 3000-year-old honey still edible! 🍯",
]
if st.button("Show a Fun fact"):
    st.write(random.choice(fun))

st.title("BMI - Calculator")
weight=st.number_input("Enter your weight (kg)",min_value=1.0,step=0.1)
height=st.number_input("Enter your height (m)",min_value=0.5,step=0.01)

if st.button("Calculate BMI"):
    if weight>0 and height>0:
        bmi=weight/(height**2)
        st.success(f"Your BMI is : {bmi:.2f}")
        if bmi<18.5:
            st.warning("You are underweight!")
        elif 18.5 <=bmi<24.9:
            st.success("You have a normal weight")
        elif 25<=bmi<29.9:
            st.warning("You are overweight!!")
        else:
            st.error("you are obese! Consider a healthier lifestyle ")
else:
    st.error("please enter valid values")