#
# Bitly  CLI test code with login, apikey
# By Rick Anderson rick.rickanderson@gmail.com inspired by the Bit.ly Hackathon on July 14th, 2010
# Feel free to fork or add

import pprint
import getpass
import argparse
import bitly_api


def main():
    parser = argparse.ArgumentParser(prog="bitlycli", description="Command line client for the Python Bit.ly api.")
    #add base arguments  
    parser.add_argument("-u", "--login", dest="login", required=True, help="Specify a login.")
    parser.add_argument("-p", "--apikey", dest="apikey", required=True, action="store_true", help="You will be prompted for apikey if True.")   
    parser.add_argument("-s","--shorten", dest="shorten", help="Provide a URL to shorten.")
    parser.add_argument("-e","--expand", dest="expand", nargs="+", help="Provide a Bit.ly hash.")
    parser.add_argument("-c","--clicks", dest="clicks", nargs="+", help="Provide one or more Bit.ly hashes.")
    parser.add_argument("-v","--verbose", action='store_true', help="Include more info echo request")

    #parse the results
    args = parser.parse_args()


    #Actions 
    get_apikey(args)
    if args.verbose:
    	pprint.pprint( args)
    if  args.shorten != None:
        bitly = bitly_api.Connection(args.login, args.apikey)
        print bitly.shorten(args.shorten)
    elif args.expand != None:
        bitly = bitly_api.Connection(args.login, args.apikey)
        print bitly.expand(args.expand)
    elif args.clicks != None:
        bitly = bitly_api.Connection(args.login, args.apikey)
        print bitly.clicks(args.clicks)

    

def get_apikey(args):
    if args.apikey is True:
        args.apikey = getpass.getpass("Enter apikey: ")

    if len(args.apikey) == 0:
        print "No apikey given\n"
        exit(-1)
       
    return



if __name__=="__main__":
    main()

