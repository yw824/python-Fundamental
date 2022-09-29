import socket

#Service List has a list of application protocols

serviceList = ["echo", 
                "ftp",
                "ssh",
                "telnet",
                "smtp",
                "domain",
                "http",
                "kerberos",
                "bgp",
                "https"]

underlyingProtocol = "tcp"
# note : "ntp" with tcp will generate an error as NTP only supports UDP

for service in serviceList:
    portNum = socket.getservbyname(service, underlyingProtocol)
    print("The service {} uses port number {}".format(service, portNum))