## Domain Ownership Verifier
This script will accept both a list of domains and a list of potential registrants, and will write to file a list of domains that are indeed owned by one of the specified registrants.
Is this useful? iono.
My use case is bounty programs. Some specify that servers owned by other entities are off limits. Also helpful when pulling in a big domain list gathered by someone else.

For example
_domains list_
```
└─$ cat test.txt   
hp.com
hp.demdex.net
hp.net
hpconnected.com
hpe.com
hpeprint.com
hpeaccesspoint.com
dopplerweekly.com
```
_registrants list_
```
└─$ cat registrants.txt 
Hewlett Packard Enterprise Company
HP Inc.
```
_usage_
```
└─$ python3 ~/Tools/domain_ownership_verifier/domain_ownership_verifier.py
enter your domains list: test.txt
enter the list of expected registrants: registrants.txt
hp.com is owned by HP Inc.. Writing to dov_match.txt...
hp.net is owned by HP Inc.. Writing to dov_match.txt...
hpconnected.com is owned by HP Inc.. Writing to dov_match.txt...
hpe.com is owned by Hewlett Packard Enterprise Company. Writing to dov_match.txt...
hpeprint.com is owned by HP Inc.. Writing to dov_match.txt...
hpeaccesspoint.com is owned by Hewlett Packard Enterprise Company. Writing to dov_match.txt...
dopplerweekly.com is owned by Hewlett Packard Enterprise Company. Writing to dov_match.txt...
```
_output_
```
└─$ cat dov_match.txt 
hp.com
hp.net
hpconnected.com
hpe.com
hpeprint.com
hpeaccesspoint.com
dopplerweekly.com
```

### Using pipenv

```bash
pipenv run pip install -r requirements.txt
pipenv run python domain_ownership_verifier.py
```
