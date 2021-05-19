"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

"""



class Solution:
    def defangIPaddr(self, address: str) -> str:
            defanged = ""
            for currentLetter in address:
                if currentLetter == ".":
                    defanged += "[.]"
                else:
                    defanged += currentLetter
            return defanged