#!/usr/local/bin/python3

import requests
import os
import time
from getpass import getpass
import okta_api

def main():
	username = raw_input("Okta Username: ")
	password = getpass('Okta Password: ')

	authToken = okta_api.okta_api(username, password)
	print(authToken)

if __name__ == '__main__':
	main()
