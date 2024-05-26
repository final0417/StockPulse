import streamlit as st
from home import app as home_app
from explore import app as explore_app
from portfolio import app as portfolio_app
from contact import app as contact_app
from streamlit_option_menu import option_menu

# Create a dictionary to map page names to their corresponding functions
st.set_page_config(
        page_title="StockPulse",
        page_icon="coin",
        layout="wide"
    )

pages = {
    "Investment": home_app,
    "Portfolio": portfolio_app,
    "Explore": explore_app,
    "Contact": contact_app
}

# Create a sidebar with page selection
with st.sidebar:
    col1, col2, col3 = st.columns([2, 3, 2])
    with col2:
        st.image("logo.png")
    selected = option_menu(
        menu_title="StockPulse",
        options=["Investment", "Portfolio", "Explore", "Contact","Home"],
        icons=["cart3", "database-up", "search", "chat-right-dots","house"],
        menu_icon="graph-up-arrow",
        default_index=0,
    )

# Display the selected page
pages[selected]()