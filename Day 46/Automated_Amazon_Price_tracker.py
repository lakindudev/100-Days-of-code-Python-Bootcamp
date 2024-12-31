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
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "priority": "u=0, i",
    "x-forwarded-proto": "https",
    "x-https": "on",
    "X-Forwarded-For": "111.223.186.128"
}
response = requests.get(URL, headers=HEADERS)
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


