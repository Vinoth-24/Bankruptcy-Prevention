    
#Importing Libraries:
import streamlit as st 
from keras.models import load_model
from PIL import Image
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
#-------------------------------------------------------------------------------------------------------------------------------
st.set_page_config(page_title="App-Streamlit",page_icon="random",layout="wide",
                       menu_items={'Get Help': 'http://www.quickmeme.com/img/54/547621773e22705fcfa0e73bc86c76a05d4c0b33040fcb048375dfe9167d8ffc.jpg',
                                   'Report a bug': "https://w7.pngwing.com/pngs/839/902/png-transparent-ladybird-ladybird-bug-miscellaneous-presentation-insects-thumbnail.png",
                                   'About': "# This is a Bankruptcy Prevention App. Very Easy to use!"})

@st.cache(allow_output_mutation=True) #For Autoupdate in app.

def loading_model():
    model = load_model(r'C:\Users\new\Documents\PythonFiles\EXCELR Project\bankr.h5')
    return model
with st.spinner('Model is being loaded..'):
    model=loading_model()     #Model is loaded.

# Reading File:
bank_data=pd.read_csv("A:\\Data Science by Excelr\\PROJECT\\bankruptcy_prevention.csv",sep=";")
label_encoder = preprocessing.LabelEncoder()
bank_data[" class"] = label_encoder.fit_transform(bank_data[" class"])
features=bank_data.columns[0:6]
#-------------------------------------------------------------------------------------------------------------------------------
st.write("""
         # BANKRUPTCY PREVENTION
         """)

# Model Prediction func:
def predict_bankruptcy(industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk):
    
    pred=model.predict([[industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk]])
    prediction = (pred >=0.9995045) 
    prediction=1*prediction
    print(prediction)
    return prediction
#-------------------------------------------------------------------------------------------------------------------------------

# Graph function:
def graph1(choice):
    plt.rcParams.update({'font.size': 6})
    if choice=='None':
        g=0
        h=0
        return g,h
    else:
        g=sns.catplot(" class", hue=choice, data=bank_data, kind="count",height=2,aspect=1.25, 
                          palette={0:"yellow", 0.5:"orange", 1:"red"})
        g.legend.set_title(choice, prop={"size":7})
        g.set_xticklabels(["Bankrupted", "Not Bankrupted"])
        g.fig.suptitle("%s vs Bankruptcy"%choice);
        plt.gcf().set_size_inches(3,3)
#--------------------            
        h=sns.catplot(choice, hue=" class", data=bank_data, kind="count",height=2,aspect=1.25,
                        palette={1:"blue", 0:"green"}) 
        h.legend.set_title("Bankruptcy", prop={"size":7}) 
        h.set_xticklabels(["Low", "Medium","High"]) 
        h.fig.suptitle("%s vs Bankruptcy"%choice);
        plt.gcf().set_size_inches(3,3)
        return g,h
            
#-------------------------------------------------------------------------------------------------------------------------------    

# Teams Func:
def team():
    st.text("Anand")
    st.text("Hari")
    st.text("Kasi")
    st.text("Nileena")
    st.text("Neha")
    st.text("Vishal")    
#-------------------------------------------------------------------------------------------------------------------------------

# Decor Func:    
def decor():
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bankruptcy Prevention App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    image = Image.open('A:\prev.png')
    st.image(image, caption='')    
#--------------------------------------------------------------------------------------------------------------------------------

def main():
    
    decor()
    
# taking Inputs:
    check=st.checkbox("Input Values for Features",value=False)
    if check:
        industrial_risk = st.sidebar.number_input("Industrial Risk",min_value=0.0, max_value=1.0, value=0.0, step=0.5,help="low = 0.0, medium = 0.50, high = 1.0")
        management_risk = st.sidebar.number_input("Management Risk",min_value=0.0, max_value=1.0, value=0.0, step=0.5,help="low = 0.0, medium = 0.50, high = 1.0")
        financial_flexibility = st.sidebar.number_input("Financial Flexibility",min_value=0.0, max_value=1.0, value=0.0, step=0.5,help="low = 0.0, medium = 0.50, high = 1.0")
        credibility = st.sidebar.number_input("Credibility",min_value=0.0, max_value=1.0, value=0.0, step=0.5,help="low = 0.0, medium = 0.50, high = 1.0")
        competitiveness=st.sidebar.number_input("Competitiveness",min_value=0.0, max_value=1.0, value=0.0, step=0.5,help="low = 0.0, medium = 0.50, high = 1.0")
        operating_risk=st.sidebar.number_input("Operating Risk",min_value=0.0, max_value=1.0, value=0.0, step=0.5,help="low = 0.0, medium = 0.50, high = 1.0")
        
    #---------------------------------------------------------------------------------------------------------------------------

# Result:       
        result=""
        if st.button("Predict"):
            with st.spinner('Wait for it...'):
                time.sleep(3)
            result=predict_bankruptcy(industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk)
            
        if result==0:
            result='BANKRUPTED!!'
        elif result==1:
            st.balloons()
            result= 'NOT BANKRUPTED!!'
        else:
            result='yet to submit...'
        st.success("# You are {}".format(result))
    else:
        st.write("Whenever you're ready..!")
    #---------------------------------------------------------------------------------------------------------------------------
    
# Graph:    
    if st.checkbox("Show Graphs",value=False):
        choice = st.selectbox("Choose Feature Values :",
                     ('None','industrial_risk', ' management_risk', ' financial_flexibility',
                      ' credibility',' competitiveness',' operating_risk'))        
        
        col1,col2=st.columns(2)
        plot1,plot2=graph1(choice)
        if plot1!=0:
            with col1:
                st.pyplot(plot1)
            with col2:
                st.pyplot(plot2)
        else:
            st.write("No Feature chosen!")
#---------------------------------------------------------------------------------------------------------------------------
    
# Team Details:
    if st.button("Team Details"):
        team()
#-------------------------------------------------------------------------------------------------------------------------------

# Program Starts:
if __name__=='__main__':
    main()
