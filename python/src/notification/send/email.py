import smtplib,os,json
from email.message import EmailMessage

def noification(message):
    try:
        message=json.loads(message)
        result=message["result"]
        sender_address=os.environ.get("GMAIL_ADDRESS")
        sender_password=os.environ.get("GMAIL_PASSWORD")
        receiver_address=message["username"]

        msg=EmailMessage()
        msg.set_content(f"your loan application result is :{result}")
        msg["Subject"]="Loan Application result"
        msg["From"]=sender_address
        msg["To"]=receiver_address

        session=smtplib.SMTP("smtp.gmail.com")
        session.starttls()
        session.login(sender_address,sender_password)
        session.send_message(msg,sender_address,receiver_address)
        session.quit()
        print("Mail Sent")
    except Exception as err:
        print(err)
        return err



