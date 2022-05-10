from cgitb import html
import os
import smtplib
from email.message import EmailMessage
import imghdr

# env variable
# EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')


EMAIL_ADDRESS = "*******.kcj@gmail.com"
EMAIL_PASSWORD = "************"

msg = EmailMessage()
msg['subject'] = 'whats up your BD is 2morow'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'c******.kcj@gmail.com'
msg.set_content('How about dinner at 6pm this Saturday?')

msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:SlateGray;">This ia an HTMl Email!</h1>
        </body>
    </html>
""", subtype= 'html')

# if you want to send pictures to an email 
 
# files = [ 'ashia.jpeg', 'ashia1.jpeg']
# for file in files:
#     with open(file, 'rb') as f:
#         file_data = f.read()
#         file_type = imghdr.what(f.name)
#         file_name = f.name
#         # print(file_type)

#     msg.add_attachment(file_data, maintype='image', subtype= file_type, filename= file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)


# To test your email on your terminal (am using linux so the command will be different)
# python3 -m smtpd -c DebuggingServer -n localhost:1025 (on terminal)

# with smtplib.SMTP('localhost', 1025) as smtp:

#     subject = "whats up?"
#     body= "How you doing?"
#     msg = f'{subject} \n \n {body}'
#     smtp.sendmail(EMAIL_ADDRESS, 'Reciever_address', msg)