import os.path
import pickle
import re
import base64
import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json


# if modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    creds = None
    # the file token.pickle stores the user's access and refresh tokens
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    #if there are no valid credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

   
    # Build the service object
    service = build('gmail', 'v1', credentials=creds)

    
    #call the Gmail API to fetch the emails
    results = service.users().messages().list(userId='me', q='transaction@notice.aliexpress.com').execute()
    #get the messages
    messages = results.get('messages', [])
    #create a hash table to store the new filtered emails
    filtered_emails = {}
    if not messages:
        print('No messages found.')
    else:
        print('loading messages.....')
        
        for message in messages:
           
            # get the message
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            
            # filter to get only the ones that give me the tracking of the orders
            snippet=msg.get('snippet', '')
            if 'track your order' in snippet.lower():
                # extract the body of the message
                if 'payload' in msg:
                    body = get_message_body(msg['payload'])
                    # find the order number in the body of the message using regular expressions
                    order_number = re.search(r'orderId=(\d+)', body)
                    if order_number:
                        # obtain new filtered emails in a hash table
                        order_number_id=str(order_number.group(1))
                        filtered_emails[order_number_id] = {
                            "order_number": order_number.group(1)
                        }
        
        
        # get the old filtered emails archive in 'filtered_emails.json'
        old_filtered_emails=get_archive('filtered_emails.json')
        #get the new orders 
        new_orders=find_new_orders(old_filtered_emails, filtered_emails)
        
        # save the new orders archive in 'new_orders.json'
        update_archivo('new_orders.json',new_orders)
        print(f"New Orders traking numbers: {new_orders}")
        # update the tracking adding the new orders that have trackings
        update_archivo('filtered_emails.json',filtered_emails)

# Extract the message body function
def get_message_body(payload):
    body = ""
    if 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain' or part['mimeType'] == 'text/html':
                body += base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
            elif 'parts' in part:
                body += get_message_body(part)
    else:
        body += base64.urlsafe_b64decode(payload['body']['data']).decode('utf-8')
    return body


# get json archive
def get_archive(archive_name):
    with open(archive_name, 'r', encoding='utf-8') as file:
        return json.load(file)

# get the new orders
def find_new_orders(old_orders, new_orders):
    updated_orders=[]
    for order in new_orders:
        if order not in old_orders:
            updated_orders.append(order)
            
    return updated_orders

# update json archive
def update_archivo(archive_name,archive):
    with open(archive_name, 'w', encoding='utf-8') as file:
        json.dump(archive, file)

if __name__ == '__main__':
    main()