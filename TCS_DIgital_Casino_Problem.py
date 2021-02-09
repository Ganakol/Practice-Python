def max_sum(arr):
    current_sum = arr[0]
    max_so_far = 0
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            current_sum = current_sum + arr[i]
            
        
        else:
            current_sum = arr[i]
        max_so_far = max(max_so_far, current_sum)  
    return max_so_far

n = int(input("enter number of elements:"))
arr = [int(input()) for i in range(n)]
print("Result is:",max_sum(arr))
