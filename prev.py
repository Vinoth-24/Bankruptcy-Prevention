import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from tensorflow.keras.models import load_model
from PIL import Image
import time

st.set_page_config(page_title="App-Streamlit",page_icon="random",layout="wide",
                       menu_items={'Get Help': 'http://www.quickmeme.com/img/54/547621773e22705fcfa0e73bc86c76a05d4c0b33040fcb048375dfe9167d8ffc.jpg',
                                   'Report a bug': "https://w7.pngwing.com/pngs/839/902/png-transparent-ladybird-ladybird-bug-miscellaneous-presentation-insects-thumbnail.png",
                                   'About': "# This is a Bankruptcy Prevention App. Very Easy to use!"})
@st.cache(allow_output_mutation=True)
def loading_model():
    model = load_model(r'C:\Users\new\Documents\PythonFiles\bankr.h5')
    return model
with st.spinner('Model is being loaded..'):
    model=loading_model()

    
st.write("""
         # BANKRUPTCY PREVENTION
         """
         )
def predict_bankruptcy(industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk):
    
    
   
    pred=model.predict([[industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk]])
    prediction = (pred >=0.9908809) 
    prediction=1*prediction
    print(prediction)
    return prediction



def main():

                                                        
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bankruptcy Prevention App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    image = Image.open('A:\prev.png')
    st.image(image, caption='')
    check=st.checkbox("Input Values for Features",value=False)
    if check:
        industrial_risk = st.sidebar.number_input("Industrial Risk",min_value=0.0, max_value=1.0, value=0.0, step=0.5,help="low = 0.0, medium = 0.50, high = 1.0")
        management_risk = st.sidebar.number_input("Management Risk",min_value=0.0, max_value=1.0, value=0.0, step=0.5,help="low = 0.0, medium = 0.50, high = 1.0")
        financial_flexibility = st.sidebar.number_input("Financial Flexibility",min_value=0.0, max_value=1.0, value=0.0, step=0.5,help="low = 0.0, medium = 0.50, high = 1.0")
        credibility = st.sidebar.number_input("Credibility",min_value=0.0, max_value=1.0, value=0.0, step=0.5,help="low = 0.0, medium = 0.50, high = 1.0")
        competitiveness=st.sidebar.number_input("Competitiveness",min_value=0.0, max_value=1.0, value=0.0, step=0.5,help="low = 0.0, medium = 0.50, high = 1.0")
        operating_risk=st.sidebar.number_input("Operating Risk",min_value=0.0, max_value=1.0, value=0.0, step=0.5,help="low = 0.0, medium = 0.50, high = 1.0")
        result=""
        if st.button("Predict"):
            with st.spinner('Wait for it...'):
                time.sleep(5)
            result=predict_bankruptcy(industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk)
            

        if result==0:
            result='BANKRUPTED!!'
        elif result==1:
            st.balloons()
            result= 'NOT BANKRUPTED!!'
        else:
            result='yet to submit...'
        st.success("You are {}".format(result))
    else:
        st.write("Check when ready")
    
    
    if st.button("Team Details"):
        st.text("Anand")
        st.text("Hari")
        st.text("Kasi")
        st.text("Nileena")
        st.text("Neha")
        st.text("Vishal")

if __name__=='__main__':
    main()
