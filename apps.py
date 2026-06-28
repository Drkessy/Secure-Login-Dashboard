import streamlit as st
from auth_logic import check_credentials

# Page Configuration
st.set_page_config(
    page_title="Login System",
    page_icon="🔐",
    layout="centered"
)

# CUSTOM CSS
st.markdown("""
<style>
.main { background-color: #f5f7fa; }
.login-box { 
    padding: 2rem; 
    border-radius: 15px; 
    background-color: white; 
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1); 
}
h1 { text-align: center; }
.stButton>button { 
    width: 100%; 
    border-radius: 10px; 
    height: 45px; 
}
</style>
""", unsafe_allow_html=True)

# Initialize Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# UI Logic
st.title("🔐 Secure Login")

if not st.session_state.logged_in:
    # Sidebar
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    
    username = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Calling the external logic from auth_logic.py
        if check_credentials(username, password):
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid credentials")

else:
    # Dashboard View
    st.success("Welcome to Day 38, Kessington!")
    st.subheader("Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("Projects", "40")
    col2.metric("Tasks", "76")
    col3.metric("Completed", "65")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()