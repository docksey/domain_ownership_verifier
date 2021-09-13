import subprocess
import sys
import whois

def main():
    domainsfile = input("enter your domains list: ")
    registrantsfile = input("enter the list of expected registrants: ")
    with open(domainsfile, "r") as domains:
        for d in domains:
            try:
                who = whois.whois(d.strip())
            except Exception:
                pass
            with open(registrantsfile, "r") as f:
                registrants = f.read().split('\n')
                if who.org in registrants:
                    print(f"{d.strip()} is owned by {who.org}. Writing to dov_match.txt...")
                    with open("dov_match.txt", "a") as o:
                        o.write(d)

if __name__ == "__main__":
    main()