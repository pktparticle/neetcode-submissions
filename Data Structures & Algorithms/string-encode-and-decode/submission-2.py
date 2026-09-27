class Solution:
    def encode(self, strs: List[str]) -> str:
        delimeter = '#'
        encoded = ''
        for s in strs:
            size = len(s)
            encoded += f'{size}{delimeter}{s}'
        print('encoded string: ', encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        decoded = []
        n=len(s)
        i=0
        while i<n:
            j=i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            j=j+1
            text = s[j:j+length]
            print('decoded text: ', text)
            decoded.append(text)
            i=j+length
        return decoded
