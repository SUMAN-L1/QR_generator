import streamlit as st
import qrcode
from io import BytesIO
import base64

# Title of the project
st.title("QR Generator by SumanEcon")

# Input Section
st.write("Generate a QR code for any input such as links, text, files, or other content.")
input_content = st.text_input("Enter content for the QR code:", placeholder="e.g., https://example.com")

# Generate QR Code and Display
if st.button("Generate QR Code"):
    if input_content:
        # Generate QR Code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(input_content)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Convert image to bytes
        img_bytes = BytesIO()
        img.save(img_bytes, format="PNG")
        img_bytes.seek(0)

        # Display the QR Code Image
        st.image(img_bytes, caption="Generated QR Code", use_column_width=True)

        # Provide Download Link
        b64 = base64.b64encode(img_bytes.getvalue()).decode()
        href = f'<a href="data:image/png;base64,{b64}" download="qr_code.png">Download QR Code</a>'
        st.markdown(href, unsafe_allow_html=True)
    else:
        st.warning("Please enter valid input to generate a QR Code.")
