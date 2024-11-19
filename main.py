import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass  # For secure password input
import pandas as pd
import random


password = getpass.getpass(prompt="email password: ")
people_information = pd.read_csv('people.csv') # people.csv needs to have 2 colums, name and email.
people_information['exclusion'] = people_information.apply(lambda s: str(s['exclusion']).split(',') if str(s['exclusion']) != 'nan' else [], axis=1)
people = list(people_information['name'])

exclusions = dict(zip(people, people_information['exclusion']))
def is_valid_match(giver, receiver):
    return receiver not in exclusions.get(giver, []) and giver != receiver
if len(people) < 2:
    print('Not enough participants')
else:
    for _ in range(100): # avoid infinit loop
        shuffle_people = people[:]
        random.shuffle(shuffle_people)
        matches = {}

        valid = True
        for giver in people:
            for receiver in shuffle_people:
                if is_valid_match(giver, receiver):
                    matches[giver] = receiver
                    shuffle_people.remove(receiver)
                    break
            else:
                valid = False
                break

        if valid:
            break
people_information['match'] = people_information['name'].map(matches)
print(people_information)

def send(recipient_email, html_content, password):
    sender_email = "my@gmail.com" # add your email address
    subject = "Your Partner for Secret Santa" # change the subject if needed
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(html_content, 'html'))
    try:
        with smtplib.SMTP('your smtp server', 587) as server: # include your smtp Server
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
            print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")


with open('email.html', 'r') as file:
        html_template = file.read()

for index, row in people_information.iterrows():
    giver = row['name']
    reciever = row['match']
    email = row['email']
    personalised_html =  html_template.replace('{{giver}}', giver).replace('{{receiver}}', reciever)
    send(email, personalised_html, password)
