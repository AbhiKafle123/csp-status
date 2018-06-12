#!/usr/bin/python2.7
import requests
import os

def main():
	file = 'top-1m.csv'
	errcount = 0
	cspcount = 0
	unsafecount = 0
	safecsp = []
	requests.packages.urllib3.disable_warnings()


	if not os.path.isfile(file):
		print 'File path {} doesn\'t exist'

	with open(file) as fp:
		lines = fp.readlines()
		lines = [line.split(',',1)[1].strip() for line in lines]
		fewlines = lines[0:10000]

		headers = {'user-agent': 'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0'}

		for line in fewlines:
			try:
				response = requests.head('http://'+line, allow_redirects=True,headers=headers,verify=False,timeout=5)

				if 'content-security-policy' in response.headers:
					print'{} has CSP set'.format(line)
					with open('all_csp.csv','a') as fp:
						fp.write(line+','+response.headers['content-security-policy']+'\r\n')

					if (response.headers['content-security-policy'].find('unsafe-inline')) != -1:
						unsafecount +=1
					else:
						safecsp.append(line)
						


					cspcount+=1

				else:
					print "."



			except requests.exceptions.Timeout:
				errcount+=1
				print "Time out accessing{}, errorcount = {}".format(line,errcount)
				continue
			except requests.exceptions.TooManyRedirects:
				errcount+=1
				print "Too many redirections while accessing{}, errorcount = {}".format(line,errcount)
				continue
			except requests.exceptions.SSLError:
				errcount += 1
				print "SSL Error while accessing{}, errorcount = {}".format(line,errcount)

			except	requests.exceptions.ConnectionError:
				errcount += 1
				print "ConnectionError Error while accessing{}, errorcount = {}".format(line,errcount)

		print "Total Webpages with CSP is {}".format(cspcount)
		print "Total Webpages with directives with unsafe-inline CSP is {}".format(unsafecount)
		print "Total number of errors {}.".format(errcount)



			# try:
			# 	response = requests.head('http://'+line, allow_redirects=True,headers=headers)

			# except requests.exceptions:
			# 	print '{}'.format(line)

			# 	if 'content-security-policy' in response.headers:
			# 		print '{} has CSP Set'.format(line)

			# 	else:
			# 		print '{} doesn\'t have CSP Set.'.format(line)

			


if __name__ == '__main__':
	main()
