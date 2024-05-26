import streamlit as st
import pandas as pd
import time
from datetime import datetime
#st.set_page_config(layout="wide")

def validate_cvv(input_text):
	if input_text.isdigit() and len(input_text) == 3:
		return True
	else:
		st.error("Invalid CVV!")
		return False

def validate_cno(input_text):
	if input_text.isdigit() and len(input_text) == 16:
		return True
	else:
		st.error("Invalid Card No!")
		return False

data_profiles = pd.read_csv('profile.csv')
data_profiles["ID"] = data_profiles["ID"].astype(str)

col1,col2,col3,col4,col5,col6,col7=st.columns([10,1,1,1,1,1,3])
with col1:
	st.markdown('<h3 style="color: #00ffff;">💳 Payment Gateway</h3>', unsafe_allow_html=True)
with col7:
	st.markdown('<style>img {border-radius: 200px;}</style>', unsafe_allow_html=True)
	st.image("dp.jpg", width=50)
st.markdown("""---""")

st.header("Billing Address")
#st.markdown('''The whole Portfolio will be generated automatically based on Small Cap Stocks''')


with st.form(key='form1'):
	st.markdown("<span style='color: yellow;'>Personal Information</span>", unsafe_allow_html=True)
	col1, col2 = st.columns(2)
	with col1:
		user_id = st.text_input("Enter your User Id :")
	with col2:
		amount = st.number_input("Enter the Amount You want to add :", min_value=1000)
	col1,col2=st.columns(2)
	with col1:
		First_Name = st.text_input("First Name")
	with col2:
		Last_Name = st.text_input("Last Name")

	Address = st.text_input("Enter your Address")
	st.markdown("<span style='color: yellow;'>Payment Information</span>", unsafe_allow_html=True)
	col1, col2 = st.columns(2)
	with col1:
		c_no = st.text_input("Card Number")
	with col2:
		c_name = st.text_input("Name on the Card")
	col1, col2 = st.columns(2)
	with col1:
		c_date = st.date_input("Expiration Date")
	with col2:
		c_cvv = st.text_input("CVV")
	col1,col2,col3,col4,col5=st.columns([0.5,1,1,1,1])
	with col2:
		st.image("visa.png", width=60)
	with col3:
		st.image("mastercard.png", width=60)
	with col4:
		st.image("gpay.png", width=60)
	with col5:
		st.image("paypal.png", width=60)
	col1, col2, col3 = st.columns([1.2, 2, 1])
	with col2:
		tc=st.checkbox("I agree to the terms and conditions")
	st.markdown("<br>", unsafe_allow_html=True)
	col1,col2,col3 = st.columns([2.7,2,2])
	with col2:
		submit_form=st.form_submit_button(label="Make Payment")
	if submit_form:
		c1 = validate_cno(c_no)
		c2 = validate_cvv(c_cvv)
		if c1 and c2 and tc and user_id and amount and First_Name and Last_Name and Address and c_no and c_name and c_date and c_cvv:
			if(c_date > datetime.today().date()):
				col1, col2, col3 = st.columns([1.5, 2, 2])
				with col2:
					st.success("Request Processed")
					with st.spinner("Please wait..."):
						time.sleep(5)
						st.success("Payment Made Successfully")
				user = data_profiles.loc[data_profiles['ID'] == user_id]
				# st.write(user)
				if (user.shape[0] == 1):
					# st.write("Yes")
					index = data_profiles.index[data_profiles['ID'] == user_id][0]
					# data_profiles.loc[data_profiles["ID"] == user_id]['Amount']=amount
					amount = amount + data_profiles.at[index, "Amount"]
					data_profiles.at[index, "Amount"] = amount
				else:
					# st.write("No")
					new_row = {"ID": user_id, "Portfolio_No": 0, "Exp": 0.0, "Amount": amount}
					data_profiles = data_profiles.append(new_row, ignore_index=True)
			else:
				st.warning("Your card has been expired!")
		elif user_id and amount and First_Name and Last_Name and Address and c_no and c_name and c_date and c_cvv:
			col1, col2, col3 = st.columns([1.5, 2, 2])
			with col2:
				st.warning("Please check Terms and Conditions")
		else:
			col1, col2, col3 = st.columns([1.3, 2, 2])
			with col2:
				st.error("Please Fill the Form Properly")

data_profiles.to_csv('profile.csv',index=False)