import pickle
import streamlit as st
from PIL import Image

image = Image.open('images/phishing web.jpg')

st.image(image, caption='Credits: Pexel.com',width=700)
 
# loading the trained model
pickle_in = open('RFclassifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
      
@st.cache_data()

# defining the function which will make the prediction using the data which the user inputs 
def prediction(having_IP_Address, URL_Length, having_At_Symbol, Prefix_Suffix, having_Sub_Domain, SSLfinal_State, port, Request_URL, URL_of_Anchor, Links_in_tags, SFH, Submitting_to_email, on_mouseover, RightClick, age_of_domain, DNSRecord, web_traffic, Page_Rank, Google_Index, Links_pointing_to_page, Statistical_report):   
 
    # Making predictions 
    prediction = classifier.predict( 
        [[having_IP_Address, URL_Length, having_At_Symbol, Prefix_Suffix, having_Sub_Domain, SSLfinal_State, port, Request_URL, URL_of_Anchor, Links_in_tags, SFH, Submitting_to_email, on_mouseover, RightClick, age_of_domain, DNSRecord, web_traffic, Page_Rank, Google_Index, Links_pointing_to_page, Statistical_report]])
    return prediction
      
# this is the main function in which we define our webpage 
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:black;padding:13px"> 
    <h1 style ="color:blue;text-align:center;">Phishing Website Detection ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
    # st.header('Phishing Website Detection App')

    col1, col2, col3, col4 = st.columns(4, gap='medium')
      
    # following lines create boxes in which user can enter data required to make prediction
    with col1:
        having_IP_Address = st.selectbox('Has IP Address ?',("-1","1"))
        URL_Length = st.selectbox('URL Length ?',("-1","0","1"))
        having_At_Symbol = st.selectbox('Has @ Symbol ?',("-1","1"))
        Prefix_Suffix = st.selectbox('Has Prefix Suffix ?',("-1","1"))
        having_Sub_Domain = st.selectbox('Has Sub Domain ?',("-1","0","1"))
        Statistical_report = st.selectbox('Has Statistical_report ?',("-1","1"))
    
    with col2:
        SSLfinal_State = st.selectbox('Has SSL final State ?',("-1","0","1"))
        port = st.selectbox('Has port ?',("-1","1"))
        Request_URL = st.selectbox('Has Request URL ?',("-1","1"))
        URL_of_Anchor = st.selectbox('Has URL_of_Anchor ?',("-1","0","1"))
        Links_in_tags = st.selectbox('Has Links_in_tags ?',("-1","0","1"))
    
    with col3:
        SFH = st.selectbox('Has SFH ?',("-1","0","1"))
        Submitting_to_email = st.selectbox('Has Submitting to email ?',("-1","1"))
        on_mouseover = st.selectbox('Has on_mouseover ?',("-1","1"))
        RightClick = st.selectbox('Has RightClick ?',("-1","1"))
        age_of_domain = st.selectbox('Has age_of_domain ?',("-1","1"))

    with col4:
        DNSRecord = st.selectbox('Has DNSRecord ?',("-1","1"))
        web_traffic = st.selectbox('Has web_traffic ?',("-1","0","1"))
        Page_Rank = st.selectbox('Has Page_Rank ?',("-1","1"))
        Google_Index = st.selectbox('Has Google_Index ?',("-1","1"))
        Links_pointing_to_page = st.selectbox('Links_pointing_page?',("-1","0","1"))
        result = ""
        y=st.button("Predict")
      
    # when 'Predict' is clicked, make the prediction and store it 
    if y: 
        result = prediction(having_IP_Address, URL_Length, having_At_Symbol, Prefix_Suffix, having_Sub_Domain, SSLfinal_State, port, Request_URL, URL_of_Anchor, Links_in_tags, SFH, Submitting_to_email, on_mouseover, RightClick, age_of_domain, DNSRecord, web_traffic, Page_Rank, Google_Index, Links_pointing_to_page, Statistical_report) 
        # st.success('Your domain is {}'.format(result))
        if result[0]==-1:
            st.error('Be Careful, Its a Phishing Domain!!', icon='🚨')
        else:
            st.success('It is a Safe domain.')
            st.balloons()
        # print(LoanAmount)
    
     
if __name__=='__main__': 
    main()
