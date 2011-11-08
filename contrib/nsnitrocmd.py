#!/usr/bin/env python
#import the necessary libraries
import argparse
import sys
import json
import nsnitro


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Netscaler NITRO controller')
	parser.add_argument('--lbip', metavar='IP', required=True, help='lb ip address')
	parser.add_argument('--user', metavar='USERNAME', default='api_user', help='lb username')
	parser.add_argument('--password', metavar='PASSWORD', default='api_user', help='lb password')
	parser.add_argument('--enablevserver', metavar='VSERVERNAME', help='enable vserver')
	parser.add_argument('--disablevserver', metavar='VSERVERNAME', help='disable vserver')
	parser.add_argument('--enableservice', metavar='SERVICENAME', help='enable service')
	parser.add_argument('--disableservice', metavar='SERVICENAME', help='disable service')
	parser.add_argument('--getservice', metavar='SERVICENAME', nargs='?', const='list', help='show service')
	parser.add_argument('--getserviceslist', action='store_true', help='show services list')
	parser.add_argument('--getservicesstatus', action='store_true', help='show services status')
	parser.add_argument('--dargs', action='store_true', help='show service')
	args = parser.parse_args()	

	nitro = nsnitro.NSNitro(args.lbip, args.user, args.password)

	try:
		if args.dargs:
			print(args)
			sys.exit(0)

		nitro.login()

		if args.enablevserver:
			nitro.enable_lbvserver(args.enablevserver)
			print "Enabled vserver: %s" % args.enablevserver
			sys.exit(0)

		if args.disablevserver:
			nitro.disable_lbvserver(args.disablevserver)
			print "Disabled vserver: %s" % args.disablevserver
			sys.exit(0)

		if args.enableservice:
			nitro.enable_service(args.enableservice)
			print "Enabled service: %s" % args.enableservice
			sys.exit(0)

		if args.disableservice:
			nitro.disable_service(args.disableservice)
			print "Disabled service: %s" % args.disableservice
			sys.exit(0)

		if args.getservice:
			if args.getservice == "list":
				response = nitro.get_service("")
			else:
				response = nitro.get_service(args.getservice)

			for service in response.get_response_field("service"):
				print "--- Service: " + service['name'] + " ---"
				for k, v in service.iteritems():
					print "\t%s: %s" % (k, v)

			#print "Here: " +  response
			sys.exit(0)

		if args.getserviceslist:
			response = nitro.get_service("")
			print "-- Cconfigured services ---"
			for service in response.get_response_field("service"):
				print "\t" + service['name']
			sys.exit(0)

		if args.getservicesstatus:
			response = nitro.get_service("")
			print "-- Cconfigured services (with status) ---"
			for service in response.get_response_field("service"):
				print "\t" + service['name'] + ": " + service['svrstate']
			sys.exit(0)


		print "No action specified. Exiting."
		sys.exit(0)
			

	except nsnitro.NSNitroError, e:
		print "Something went wrong: " + e.message
