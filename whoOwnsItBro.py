from ipwhois import IPWhois

file1 = open('targets.txt', 'r')
Lines = file1.readlines()

# Strips the newline character
for line in Lines:
	IPAddr = line.strip()
	obj = IPWhois(IPAddr)
	result = IPWhois.lookup_whois(obj)
	resultList = result['nets'][0]
	description = resultList['description']
	print(IPAddr + " \t\t\t\t\t\t" + description)
