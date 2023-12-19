# Recursive Brute Force

import string

charSet = string.ascii_lowercase

def brute(n): # n - character depth
    soFar = ""
    
    bruteAux(n, soFar, 1)

def bruteAux(n, soFar, i): # Should only run through all options of length N
    spawned_once = False

    for j in range(len(charSet)):
        if i != n:# if spaned letters number != total letters
            if not spawned_once:
                soFar += charSet[j]
                spawned_once = True
            else:
                soFar = soFar[:-1] + charSet[j]
                
            bruteAux(n, soFar, i+1)
        else:
            
            print(soFar + charSet[j])

        if i == (n - 1) and soFar[-1] == charSet[-1]:
            return

    


brute(3)
