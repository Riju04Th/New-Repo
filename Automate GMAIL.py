import smtplib as s
ob = s.SMTP('smtp.gmail.com')
ob.ehlo()
ob.starttls()
ob.login('riju041199@gmail.com')
subject = "Test Python"
body = "I Love Python"
msg = f"Subject: {subject}\n\n{body}"
listadd = ['subhasish.addya@gmail.com']
ob.sendmail('riju041199@gmail.com', listadd, msg)
print("sent")
ob.quit()