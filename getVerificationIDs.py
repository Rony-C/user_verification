import os
import base64
from typing import List
import time
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

class GmailException(Exception):
	"""gmail base exception class"""

class NoEmailFound(GmailException):
	"""no email found"""

def getCredentials():
    #Gets credentials to log in to Google API
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

creds = getCredentials()

def search_emails(query_stirng, label_ids: List=None):
	try:
		message_list_response = service.users().messages().list(
			userId='me',
			labelIds=label_ids,
			q=query_string
		).execute()

		message_items = message_list_response.get('messages')
		next_page_token = message_list_response.get('nextPageToken')
		
		while next_page_token:
			message_list_response = service.users().messages().list(
				userId='me',
				labelIds=label_ids,
				q=query_string,
				pageToken=next_page_token
			).execute()

			message_items.extend(message_list_response.get('messages'))
			next_page_token = message_list_response.get('nextPageToken')
		return message_items
	except Exception as e:
		raise NoEmailFound('No emails returned')

def get_file_data(message_id, attachment_id, file_name, save_location):
	response = service.users().messages().attachments().get(
		userId='me',
		messageId=message_id,
		id=attachment_id
	).execute()

	file_data = base64.urlsafe_b64decode(response.get('data').encode('UTF-8'))
	return file_data

def get_message_detail(message_id, msg_format='metadata', metadata_headers: List=None):
	message_detail = service.users().messages().get(
		userId='me',
		id=message_id,
		format=msg_format,
		metadataHeaders=metadata_headers
	).execute()
	return message_detail


if __name__ == '__main__':
	service = build('gmail', 'v1', credentials=creds)

	query_string = "is:unread subject:'FW: Alert: ID Verification - FLs stuck in PENDING from last 8 weeks + this week has results'"

	save_location = os.getcwd()
	email_messages = search_emails(query_string)

	for email_message in email_messages:
		messageDetail = get_message_detail(email_message['id'], msg_format='full', metadata_headers=['parts'])
		messageDetailPayload = messageDetail.get('payload')
		
		if 'parts' in messageDetailPayload:
			for msgPayload in messageDetailPayload['parts']:
				file_name = msgPayload['filename']
				body = msgPayload['body']
				if 'attachmentId' in body:
					attachment_id = body['attachmentId']
					attachment_content = get_file_data(email_message['id'], attachment_id, file_name, save_location)
					
					with open(os.path.join(save_location, file_name), 'wb') as _f:
						_f.write(attachment_content)
						print(f'File {file_name} is saved at {save_location}')
		time.sleep(0.5)