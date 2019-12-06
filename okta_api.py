#!/usr/bin/python3

import requests
from requests.auth import HTTPDigestAuth
import json, os

class okta_api:
	def __init__(self, username, password):
		self.username = username
		self.password = password

	def getauthToken(self, username, password):
		settingsFile = os.path.join(os.path.dirname(__file__), 'Resources/settings.json')
		with open(settingsFile,'r') as sf:
			settings = json.load(sf)
		client_id = settings["client_id"]
		client_secret = settings["client_secret"]
		endpoint = 'https://dev-246301.okta.com/oauth2/default/v1/token'
		headers = {
			"Accept" : "application/json",
			"Content-Type" : "application/x-www-form-urlencoded"
		}
		data = {"grant_type": "password", "username": username, "password": password, "scope": "profile openid"}

		r = requests.post(endpoint, headers=headers, auth=HTTPDigestAuth(client_id, client_secret), data=data)
		code = r.status_code
		print(code)
		response = r.json()
		accessToken = response["access_token"]
		return accessToken