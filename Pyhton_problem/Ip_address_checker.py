#Ip address checker
def ip_checker(ip):
    if len(ip) == 0:
        return "IP address should not be empty"
    parts = ip.split('.')
    if len(parts) != 4:
        return "Invalid IP address format"
    for part in parts:
        if not part.isdigit() or not (0 <= int(part) and int(part) <= 255):
            return "Invalid IP address format (or) out of IP Address to use the 0 to 255"
    return f"{ip} => Valid IP address"
ip = input("Enter an IP address: ")
result = ip_checker(ip)
print(result)
