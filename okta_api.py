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
		# client_id = settings['client_id']
		# client_secret = settings['client_secret']
		api_auth = settings['auth']
		endpoint = 'https://dev-246301.okta.com/oauth2/default/v1/token'
		headers = {
			"Accept" : "application/json",
			"Content-Type" : "application/x-www-form-urlencoded",
			"Authorization" : "Basic %s" % api_auth
		}
		data = {"grant_type": "password", "username": username, "password": password, "scope": "profile openid"}

		r = requests.post(endpoint, headers=headers, data=data)
		response = r.json()
		accessToken = response["access_token"]
		return accessToken

	def getProfile(self, authToken):
		endpoint = 'https://dev-246301.okta.com/oauth2/default/v1/userinfo'
		headers = {
			"Authorization" : "Bearer %s" % authToken
		}
		r = requests.post(endpoint, headers=headers)
		data = r.json()
		return data