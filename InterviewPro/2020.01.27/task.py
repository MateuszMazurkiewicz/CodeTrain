'''
An IP Address is in the format of A.B.C.D, where A, B, C, D are all integers between 0 to 255.

Given a string of numbers, return the possible IP addresses you can make with that string by splitting into 4 parts of A, B, C, D.

Keep in mind that integers can't start with a 0! (Except for 0)

Example:
Input: 1592551013
Output: ['159.255.101.3', '159.255.10.13']
'''


def ip_addresses(s, ip_parts = []):
    if len(ip_parts) == 4 and len(s) > 0:
        return []

    if len(ip_parts) < 4 and len(s) == 0:
        return []

    if len(ip_parts) == 4 and len(s) == 0:    
        r = [ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.' + ip_parts[3]]    
        return r

    ip_parts = [] if ip_parts is None else ip_parts

    result = []

    k = min(3, len(s))

    if s[0] == "0":
        tmp = ip_parts.copy()
        tmp.append([s[0]])      
        if len(s) > 1:  
            x = s[1:]
            r = ip_addresses(x, tmp)
            if r:
                result += r

    else:
        for i in range(k): 
            tmp = ip_parts.copy()
            part = s[:i + 1]
            if int(part) > 255:
                continue
            tmp.append(part)
            x = s[i + 1:]
            r = ip_addresses(x, tmp)
            if r:
                result += r

    return result

result = ip_addresses('1592551013')
print(result)
# ['159.255.101.3', '159.255.10.13']