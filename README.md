# Secret Santa Script

This is a script to make a secret santa, by sending an email to all the participants with their partner.
Using a simple html email template, and a list of people.

## Usage
First, create a list of the people that want to participate in the secret santa, collect their names, an email address and if they have any people they really don't want to get a gift. Save these in a `.csv` file using the headers `name,email,exclusion`, see [people.csv](./people.csv) as an example.

Then adapt your HTML Email, if needed, by changing the file `email.html`. Use `{{giver}}` as the name of the person you are addressing the email and `{{receiver}}` as the person they will give the present to.

Finally, adapt the file `main.py` to fill your needs. Change the subject of the email, add your own sender email address and put your `smtp` Server.

Finally, hit run, and the email are sent!

## Notice

No guarantee of it working. No guarantee, your email account will not get flagged as spam
