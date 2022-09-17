# Description:
#
# Take the following IPv4 address: 128.32.10.1
#
# This address has 4 octets where each octet is a single byte (or 8 bits).
#
#     1st octet 128 has the binary representation: 10000000
#     2nd octet 32 has the binary representation: 00100000
#     3rd octet 10 has the binary representation: 00001010
#     4th octet 1 has the binary representation: 00000001
#
# So 128.32.10.1 == 10000000.00100000.00001010.00000001
#
# Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361
#
# Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.
#
# My solution:
def int32_to_ip(int32):
    binary = str(bin(int32))[2:]
    if int32 != 0:
        p1 = int(binary[:-24], 2)
        p2 = int(binary[-24:-16], 2)
        p3 = int(binary[-16:-8], 2)
        p4 = int(binary[-8:], 2)
        return f'{p1}.{p2}.{p3}.{p4}'
    if int32 == 0:
        return '0.0.0.0'
