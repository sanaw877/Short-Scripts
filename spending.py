import imapclient
import pyzmail
import pprint
import re 
import pandas as pd

imapObj = imapclient.IMAPClient('imap.gmail.com',ssl=True)

imapObj.login('myemail@gmail.com', 'mypassword')

imapObj.select_folder('INBOX', readonly=True)
ids = imapObj.search(['FROM', 'capitalone@notification.capitalone.com','SUBJECT',"A new transaction was charged to your account"])

# ids = ids[0:200]
dates = []
stores = []
amounts = []
for id in ids:
	messages = imapObj.fetch(id,['BODY[]'])
	# pprint.pprint(messages)
	message = pyzmail.PyzMessage.factory(messages[id][b'BODY[]'])
	message_text = message.text_part.get_payload().decode(message.text_part.charset)
	try:
		date = re.search(r"(\d+/\d+/\d+)", message_text).group()
		store = re.search(r"\b(at) (.+),", message_text).group(2)
		amount = re.search(r"\$\d+.\d+", message_text).group()
		
		dates.append(date)
		stores.append(store)
		amounts.append(amount)
	except:
		pass

df_data = {'date': dates,
		   'store': stores,
		   'amount': amounts}

df = pd.DataFrame(df_data)
print(df)
df.to_csv('spending.xlsx', mode='a', header=False)
	
