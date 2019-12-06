#!/usr/bin/python3

import requests
import os
import time
from getpass import getpass
import okta_api

def main():
	username = input("Okta Username: ")
	password = getpass('Okta Password: ')

	oapi = okta_api.okta_api(username, password)
	authToken = oapi.getauthToken(username, password)

	profile = oapi.getProfile(authToken)
	fullName = profile['name']

	print("Welcome back %s. You've successfully accessd the Okta API." % fullName)


if __name__ == '__main__':
	main()
