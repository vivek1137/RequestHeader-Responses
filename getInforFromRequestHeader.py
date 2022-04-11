# Pre-requisite of running this script
# Configure the domains by this process
# Step1: Use either Dig or Ping tool to obtain the IP address of an Akamai staging edge server for the staging hostname
#        Ping sellerapp.tatacliq.com.edgekey - staging.net
#        Or
#        Dig sellerapp.tatacliq.com.edgekey - staging.net
#
# Step2: Edit your local hosts file and update the IP / Domain mapping at the end of the file.
#        Windows: C:\Windows\System32\drivers\etc\hosts
#        GNU / Linux or Mac
#        OS
#        X: / etc / hosts
#        IP
#        obtained
#        from step1 < space > sellerapp.tatacliq.com

# Step 3 : Run this script to check the Akamai Setup


import requests
import pytest as py

# This is the list of domain value


domains = ["sellerapp.tatacliq.com",
           'sellerapp.tatacliq.com',
           'sellerinterp.tatacliq.com',
           'sellerzoneerp.tatacliq.com',
           'sellerzoneapi.tatacliq.com',
           'sellerzonebatch.tatacliq.com',
           'sellerzonereport.tatacliq.com',
           'integra.tatacliq.com',
           'dlintegra.tatacliq.com',
           'intbatch.tatacliq.com',
           'intapp.tatacliq.com',
           ]

# This function checks if a given value is present in the main string or not

def isPresent(headerValue,valueToCheck) :
    if valueToCheck in headerValue :
        return True
    else :
        return False

# This methods returns a list of domains which has / hasn't Akamai Setup


def findValueinHeaders(domain_list,valueInfo):
    urls_withNoValue = []
    urls_WithValue = []
    for domains in domain_list:
        domain = "https://" + domains
        responses = requests.get(domain)
        verify_availability = isPresent(responses.headers,valueInfo)

        if verify_availability is False :

            urls_withNoValue.append(domains)
        else :
            urls_WithValue.append(domains)
        assert (verify_availability)
    return urls_withNoValue , urls_WithValue


domainsWithAkamai, domainsWithoutAkamai  = verify_availability(domains,"'X-Akamai-Staging': 'ESSL'")


print('domains with akamai',domainsWithAkamai)
print('domains without akamai',domainsWithoutAkamai)





