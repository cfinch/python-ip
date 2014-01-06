# Utility functions
def quaddot(binary):
    "Returns a quad-dotted string representation of a 32-bit binary number"""
    return "{}.{}.{}.{}".format(int(binary[0:8],2), 
        int(binary[8:16],2), int(binary[16:24],2), int(binary[24:],2))

def binary(ip):
    """Returns a binary string representation of the IP address"""
    return "{0:08b}{1:08b}{2:08b}{3:08b}".format(ip.address[0],
        ip.address[1], ip.address[2], ip.address[3])

def complement(binary_netmask):
    import ctypes
    return ctypes.c_uint32(~int(binary_netmask,2)).value

# Classes
class IPAddress(object):
    def __init__(self, address):
        octet_strings = address.split('.')
        self.address = [int(octet) for octet in octet_strings]

    def __str__(self):
        return "{}.{}.{}.{}".format(self.address[0], self.address[1], 
            self.address[2], self.address[3])

    def __repr__(self):
        return "IPAddress('{}')".format(str(self))

    def binary(self):
        """Returns a binary string representation of the IP address"""
        return binary(self)

    def netmask(self, CIDR_prefix_length):
        CIDR_binary_string = ""
        for i in range(CIDR_prefix_length):
            CIDR_binary_string += "1"

        for i in range(32 - CIDR_prefix_length):
            CIDR_binary_string += "0"

        netmask_string = quaddot(CIDR_binary_string)

        return IPAddress(netmask_string)

    def broadcast(self, netmask):
        binary_netmask = netmask.binary()
        netmask_complement = complement(binary_netmask)
        broadcast_address = int(binary(self), 2) | netmask_complement
        binary_broadcast = "{0:32b}".format(broadcast_address)
        broadcast_string = quaddot(binary_broadcast)
        
        return IPAddress(broadcast_string)

    def __eq__(self, other):
        if self.address == other.address:
            return True
        else:
            return False

    def __add__(self, increment):
        ip = IPAddress(str(self))

        # Private 20-bit block
        if ip.address[0] == 172 and ip.address[1] >= 16 and ip.address[1] <= 31:
            if ip.address[3] <= (254 - increment):
                ip.address[3] += increment;
            elif ip.address[2] < 254:
                ip.address[3] = increment - (254 - ip.address[3])
                ip.address[2] += 1;
            elif ip.address[1] > 16 and ip.address[1] < 31:
                ip.address[3] = increment - (254 - ip.address[3])
                ip.address[2] = 1;
                ip.address[1] += 1;

        # Private 16-bit block
        elif ip.address[0] == 192 and ip.address[1] == 168:
            if ip.address[3] <= (254 - increment):
                ip.address[3] += increment;
            elif ip.address[2] < 254:
                ip.address[3] = increment - (254 - ip.address[3])
                ip.address[2] += 1;

        return ip

    def __isadd__(self, increment):
        self.add(self, increment)
        return self

