# Email/Text Alert Module

# Using the `send_mail` function

![Untitled](Email%20Text%20Alert%20Module%208307f9667923406b83a98548bfbd16cb/Untitled.png)

![Untitled](Email%20Text%20Alert%20Module%208307f9667923406b83a98548bfbd16cb/Untitled%201.png)

![Untitled](Email%20Text%20Alert%20Module%208307f9667923406b83a98548bfbd16cb/Untitled%202.png)

# Getting Twilio Credentials for `send_text` function

### 1. Go to [Twilio.com](http://Twilio.com) and sign up

### 2. Go to `Account` → `API Keys & Tokens`

![Untitled](Email%20Text%20Alert%20Module%208307f9667923406b83a98548bfbd16cb/Untitled%203.png)

### 3. Get the `Account SID` and `Auth Token` in the bottom of the screen

![Untitled](Email%20Text%20Alert%20Module%208307f9667923406b83a98548bfbd16cb/Untitled%204.png)

### 4. Go to [https://console.twilio.com/](https://console.twilio.com/) and get your Twilio Number you will use to send the texts

![Untitled](Email%20Text%20Alert%20Module%208307f9667923406b83a98548bfbd16cb/Untitled%205.png)

### 5. Save the credentials as environment variables

```sql
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