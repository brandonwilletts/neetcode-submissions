class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        
        # Delimeter: length + #
        for string in strs:
            encoded += (str(len(string)) + "#" + string)
        
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        ch = 0

        while ch < len(s):
            # Get length
            len_str = ""
            while s[ch] != "#":
                len_str += s[ch]
                ch += 1
            print("|" + len_str + "|")
            len_int = int(len_str)
            
            # Advance passed #
            ch += 1

            # Parse string
            string = ""
            for i in range(len_int):
                string += s[ch]
                ch += 1

            decoded.append(string)
      
        return decoded

            



            
            


        return decoded