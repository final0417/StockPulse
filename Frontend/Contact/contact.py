import streamlit as st
import re


def validate_mobile_number(mobile):
    # Regular expression to validate mobile number format
    pattern = r"^\d{10}$"  # Assumes a 10-digit number without any additional characters

    if re.match(pattern, mobile):
        return True
    else:
        return False

def app():
    st.markdown('''<h1>☎ Contact Us</h1>''', unsafe_allow_html=True)
    st.markdown("""---""")

    st.markdown('''<h3 style="color: #00ffff;">Try out our Smart Chatbot for your queries</h3>''', unsafe_allow_html=True)
    st.markdown('<a href="https://ai-chat-for-customer-service-2665b0.zapier.app/chat" style="font-size: 24px;">💬 Assistly</a>',unsafe_allow_html=True)
    st.markdown("""---""")

    st.write("<span style='color:yellow'>Or fill out the form below to get in touch with us.</span>", unsafe_allow_html=True)
    name = st.text_input("Name")
    email = st.text_input("Email")
    mobile = st.text_input("Mobile Number")
    message = st.text_area("Message", height=150)


    if st.button("Submit"):
        if name and email and mobile and message:
            # Here you can integrate with your backend or send an email
            if validate_mobile_number(mobile):
                st.success("Thank you for your message! We will get back to you soon.")
            else:
                st.error("Invalid Mobile Number.")
        else:
            st.error("Please fill out all the fields.")

    st.markdown("""---""")

if __name__ == "__main__":
    main()
