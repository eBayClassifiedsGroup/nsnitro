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
	parser.add_argument('--enablevserver', metavar='VSERVERNAME', help='enable lb vserver')
	parser.add_argument('--disablevserver', metavar='VSERVERNAME', help='disable lb vserver')
	parser.add_argument('--enableservice', metavar='SERVICENAME', help='enable service')
	parser.add_argument('--disableservice', metavar='SERVICENAME', help='disable service')
	parser.add_argument('--getservice', metavar='SERVICENAME', nargs='?', const='list', help='show service')
	parser.add_argument('--getservicestatus', metavar='SERVICENAME', help='show service status')
	parser.add_argument('--getserviceslist', action='store_true', help='show services list')
	parser.add_argument('--getservicesstatus', action='store_true', help='show services status')
	parser.add_argument('--renamelbvserver', metavar=('NAME', 'NEWNAME'), nargs=2, help='rename lb vserver from NAME to NEWNAME')
	parser.add_argument('--renameservice', metavar=('NAME', 'NEWNAME'), nargs=2, help='rename service from NAME to NEWNAME')
	parser.add_argument('--bindservicetolbvserver', metavar=('VSERVER', 'SERVICE', 'WEIGHT'), nargs=3, help='bind SERVICE to lb VSERVER with WEIGHT')
	parser.add_argument('--dargs', action='store_true', help='show service')
	args = parser.parse_args()	

	if args.dargs:
		print(args)
		sys.exit(0)

	nitro = nsnitro.NSNitro(args.lbip, args.user, args.password)

	try:
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
			print "-- Configured services ---"
			for service in response.get_response_field("service"):
				print "\t" + service['name']
			sys.exit(0)

		if args.getservicesstatus:
			response = nitro.get_service("")
			print "-- Configured services (with status) ---"
			for service in response.get_response_field("service"):
				print "\t" + service['name'] + ": " + service['svrstate']
			sys.exit(0)

		if args.getservicestatus:
			response = nitro.get_service(args.getservicestatus)
			for service in response.get_response_field("service"):
				print service['name'] + ": " + service['svrstate']
			sys.exit(0)

		if args.renamelbvserver:
			response = nitro.rename_lbvserver(args.renamelbvserver[0], args.renamelbvserver[1])
			print "Renamed '%s' to '%s'." % (args.renamelbvserver[0], args.renamelbvserver[1]) 
			sys.exit(0)

		if args.renameservice:
			response = nitro.rename_service(args.renameservice[0], args.renameservice[1])
			print "Renamed '%s' to '%s'." % (args.renameservice[0], args.renameservice[1]) 
			sys.exit(0)

		if args.bindservicetolbvserver:
			response = nitro.bind_service_to_lbvserver(args.bindservicetolbvserver[0], args.bindservicetolbvserver[1], args.bindservicetolbvserver[2])
			print "Bound service '%s' to lb vserver '%s' with weight '%s'." % (args.bindservicetolbvserver[0], args.bindservicetolbvserver[1], args.bindservicetolbvserver[2]) 
			sys.exit(0)


		print "No action specified. Exiting."
		sys.exit(0)
			

	except nsnitro.NSNitroError, e:
		print "Error: " + e.message
