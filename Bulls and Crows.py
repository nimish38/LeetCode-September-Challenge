class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        b = 0
        secret = list(secret)
        guess = list(guess)
        
        
        # calculate exact number and position matching - bull
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
                secret[i] = -1
                guess[i] = -1
                
        # find if character is present but at diff position - cow
        for i in range(len(secret)):
            if guess[i] != -1:
                #print(guess[i], secret)
                if guess[i] in secret:
                    for j in range(len(secret)):
                        if secret[j] == guess[i]:
                            b += 1
                            secret[j] = -1
                            break
            #print(secret)               
        return str(a) + 'A' + str(b) + 'B'                
            
        