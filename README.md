# Why I created this
I was tired of waiting for pipelines to finish, 
refreshing the web browser, or looking at my log files.
So I decided to create a toolkit for myself, 
with which I could receive the progress of the pipelines through mails 
or texts. 

# Downloading the package

```python
pip install -i https://test.pypi.org/simple/ dougs-noti
```

# Example code

```python
from dougs_noti import noti
import os

# NAVER_MAIL and NAVER_PW should be saved as environment variables before running the code 
sender_email = os.environ.get("NAVER_MAIL")
sender_password = os.environ.get("NAVER_PW")

noti.send_email(sender_email=sender_email, sender_password=sender_password, to_email='slakingex@gmail.com',
            mail_body='hello!', mail_subject='attachment part1.csv')

# TWILIO_SID and TWILIO_AUTH_TOKEN should be saved as environment variables before running the code 
to_number = '+142446...'
from_number = '+18449991359'
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

noti.send_text(account_sid=account_sid, auth_token=auth_token, from_number=from_number, to_number=to_number, text_body="Sending test #4")
```

# Explanation of the functions

`send_email` 

```python
(function) def send_email(
    sender_email: str,
    sender_password: str,
    to_email: List[str],
    smtp_server: str = None,
    smtp_port: str = None,
    file_loc: str = None,
    mail_body: str = 'this is message generated from s',
    mail_subject: str = <Expression>
) -> bool

sender_email : email you will use to send the alert
sender_password : password for the email you will use to send the alert
to_email : email that will get the alert
ex)'test2@gmail.com'
smtp_server : smtp server for your sender email. If we have the smtp server of your email provider in our db, you might not need to input it ex) gmail.com -> smtp.gmail.com
smtp_port : smtp server for your sender email. If we have the smtp port of your email provider in our db, you might not need to input it ex) gmail.com -> 587 file_loc : full directory of the attachement file (default : None)
mail_body : the content of the mail
mail_subject : the subject of the mail
```

`send_text` 

```python
(function) def send_text(
    account_sid: str,
    auth_token: str,
    from_number: str,
    to_number: str,
    text_body: str
) -> None

account_sid : account id of twilio account. see the READ.MD on how you can get it 
auth_token : authorization token for twilio services see the READ.MD on how you can get it 
from_number : the number you will use to send the text. This should be provided by Twilio. Read the READ.MD for how you should get it 
to_number : the number that will get the text 
text_body : content of the text 
```

# Using the `send_mail` function

### Some emails like @gmail.com requires a separate pw for applications

1. Go to Gmail account settings → security 
2. Search for `app passwords` and click `app passwords`

![Untitled](dougs_noti%20user%20manual%208307f9667923406b83a98548bfbd16cb/Untitled.png)

1. Generate Corresponding password

![Untitled](dougs_noti%20user%20manual%208307f9667923406b83a98548bfbd16cb/Untitled%201.png)

![Untitled](dougs_noti%20user%20manual%208307f9667923406b83a98548bfbd16cb/Untitled%202.png)

1. Copy and assign it as a environment variable 

```python
export GMAIL_PW='jeho....' 
```

# Getting Twilio Credentials for `send_text` function

### 1. Go to [Twilio.com](http://Twilio.com) and sign up

### 2. Go to `Account` → `API Keys & Tokens`

![Untitled](dougs_noti%20user%20manual%208307f9667923406b83a98548bfbd16cb/Untitled%203.png)

### 3. Get the `Account SID` and `Auth Token` in the bottom of the screen

![Untitled](dougs_noti%20user%20manual%208307f9667923406b83a98548bfbd16cb/Untitled%204.png)

### 4. Go to [https://console.twilio.com/](https://console.twilio.com/) and get your Twilio Number you will use to send the texts

![Untitled](dougs_noti%20user%20manual%208307f9667923406b83a98548bfbd16cb/Untitled%205.png)

### 5. Save the credentials as environment variables

```bash
# Assign the variables in your terminal
export TWILIO_SID='AC780838d9c334e9d3b2f3ea55a052ddd6'
export TWILIO_AUTH_TOKEN='e28200aa90c...'
```

### 6. Use the credentials in your code

```python
import os

# Number you're sending the text message to 
to_number = '+1424468..'

# Number you're using to send the text message (Step 4)
from_number = '+18449991359'

# Account_sid you got in step 3 
account_sid = os.environ.get("TWILIO_SID")

# Account Auth token you got in step 3 
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

# Call the function
send_text(account_sid=account_sid, auth_token=auth_token, from_number=from_number, to_number=to_number, text_body="Sending test #3")
```