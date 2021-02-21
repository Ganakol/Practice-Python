Problem Statement- Find longest length of substring without repetition of character.

def longest_substring(string):
    dic = {}
    max_length=start=0
    for i in range(len(string)):
        if string[i] in dic and start<=dic[string[i]]:
            start = dic[string[i]]+1
            print(start)
        else:
            max_length = max(max_length,i-start+1)
            
        dic[string[i]]=i 
    print(dic)
        
    return max_length
    
    
string ="abcabcbb"
print(longest_substring(string))
