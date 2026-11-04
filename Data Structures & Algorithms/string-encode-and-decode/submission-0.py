class Solution:
    # Brute force
    # Each string can be at most 99 characters (1584 bits)
        # Delegate 1584 bits per string, pad with zeros
    # Max of 199 strings to encode/decode ()
        # Decode strings by reading in 1584 bit chunks
    
    # Encode/decode 9-bit numbers
        # Encode each of the 256 ASCII characters to codewords (0-255)
        # Codeword 256 can represent the end of each string
        # Encode the list of string into one long string containing 9-bit numbers next to each other        

    def encode(self, strs: List[str]) -> str:
        bitstring = ""
        for string in strs:
            for c in range(len(string)):
                bitstring += f"{ord(string[c]):09b}"
            bitstring += f"{256:09b}"
        return bitstring

    def decode(self, s: str) -> List[str]:
        c = 0
        decoded_list = []
        decoded_string = ""
        while(c < len(s)):
            codeword = int(s[c:c + 9], 2)
            if(codeword == 256):
                decoded_list.append(decoded_string)
                decoded_string = ""
            else:
                decoded_string += chr(codeword)
            
            c += 9
        
        return decoded_list

