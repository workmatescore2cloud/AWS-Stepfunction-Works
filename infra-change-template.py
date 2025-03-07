def send_email(recipient, subject, body):
              response = ses_client.send_email(
                  Source="<configured -identity-email-id>", #Add your Email Id to send mails to Customers via SES
                  Destination={'ToAddresses': [recipient]},
                  Message={'Subject': {'Data': subject}, 'Body': {'Text': {'Data': body}}}
              )
