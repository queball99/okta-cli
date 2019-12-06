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

	print("I'm sorry %s I can't do that." % fullName)


if __name__ == '__main__':
	main()
