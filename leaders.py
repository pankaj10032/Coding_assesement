def find_leaders(arr):
    n=len(arr)
    leaders=[]
    # initially Rightmost element(arr[n-1]) will always be the leader because there is no element greater than iy
    max_right=arr[n-1]
    leaders.append(max_right)

    for i in range(n-2, -1, -1):
        if arr[i]>max_right:
            max_right=arr[i]
            leaders.append(max_right)
    return leaders[::-1] # reverse the leaders list to get correct order
arr = [7, 10, 4, 10, 6, 5, 2]
leaders = find_leaders(arr)
print(leaders)