import streamlit as st
import pytesseract
from PIL import Image
import re

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Streamlit UI
st.title("📧 Extract Emails from Image")
st.write("Upload an image containing email addresses, and the app will extract them.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Open the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Perform OCR
    with st.spinner("Extracting text..."):
        extracted_text = pytesseract.image_to_string(image)

    # Extract email addresses using regex
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_pattern, extracted_text)

    # Remove duplicates and sort
    unique_emails = sorted(set(emails))

    # Display Results
    if unique_emails:
        st.success("✅ Emails Extracted Successfully!")
        
        # Show each email on a new line
        for idx, email in enumerate(unique_emails, 1):
            st.write(f"{idx}. {email}")
    else:
        st.warning("⚠ No emails found in the image!")
