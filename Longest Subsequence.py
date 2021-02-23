def longest_subsq(text1,text2):
    n,m = len(text1),len(text2)
    arr = [[0]*(m+1) for i in range(n+1)]
    for i in range(n):
        for j in range(m):
            if text1[i] == text2[j]:
                arr[i+1][j+1] = arr[i][j]+ 1 
            else:
                arr[i+1][j+1] = max(arr[i+1][j],arr[i][j+1])
    
    return arr[-1][-1]
    
    
text1 = input()
text2 = input()
print(longest_subsq(text1,text2))
