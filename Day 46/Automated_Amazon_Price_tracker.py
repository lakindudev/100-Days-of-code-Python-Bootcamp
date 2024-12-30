from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve sensitive information from environment variables
sender_email = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")
smtp_address = os.getenv("SMTP_ADDRESS")
receiver_email = "lakinduperera18@yahoo.com"  # Receiver's email (static)

URL = "https://appbrewery.github.io/instant_pot/"

response = requests.get(URL)
price_tracker = response.text

soup = BeautifulSoup(price_tracker, "html.parser")

price_element = soup.select_one(".aok-offscreen").getText()
price = price_element.split("$")[1]
price_as_float = float(price)
print(price_as_float)


#create email content
subject = "price deducted"
body = f"Instant Pot Duo Plus 9-in-1 Electric Pressure Cooker, Slow Cooker, Rice Cooker, Steamer, Sauté, Yogurt Maker, ""Warmer & Sterilizer, Includes App With Over 800 Recipes, Stainless Steel, 3 Quart  is now ${price}"

# Prepare email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach body in UTF-8 encoding
msg.attach(MIMEText(body, 'plain', 'utf-8'))

if price_as_float < 100:
    # Send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, password)  # Login to Gmail with App Password
            server.sendmail(sender_email, receiver_email, msg.as_string())  # Send the email
            print("Email sent successfully!")
    except Exception as e:
        print(f"An Error occurred: {e}")


