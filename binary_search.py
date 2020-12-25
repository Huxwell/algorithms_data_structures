def bin_search_eq(arr, target, mini, maxi): #looking for value equal to target
    mid = (mini+maxi)//2
    print("bin_search_eq t,m,g, mid", target, mini, maxi, mid)
    
    # if mini == maxi:
    if mini > maxi:
        # if arr[mini] == target:
        #     return mini
        # else:
            return None
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        maxi = mid -1
        return bin_search_eq(arr, target, mini, maxi)
    else:
        mini = mid +1
        return bin_search_eq(arr, target, mini, maxi)

def bin_search_lower_bound(arr, target, mini, maxi): #looking for first value higher than target
    #pass
    
#     UpperBound Implementation in C++:

# int UpperBound(int A[],int N,int K){
#     int low , high , mid ;
#     low = 1 ;
#     high = N ;
#     while(low <= high){
#         mid = ( low + high ) / 2 ; // finding middle element 
#         if(A[mid] > K && ( mid == 1 || A[mid-1] <= K )) // checking conditions for upperbound
#             return mid ;
#         else if(A[mid] > K) // answer should be in left part 
#             high = mid - 1 ;
#         else                // answer should in right part if it exists
#             low = mid + 1 ;
#     }
#     return mid ; // this will execute when there is no element in the given array which > K
# }
# LowerBound Implementation in C++:

# int LowerBound(int A[],int N,int K){
#     int low , high , mid ;
#     low = 1 ;
#     high = N ;
#     while(low <= high){
#         mid = ( low + high ) / 2 ; // finding middle element 
#         if(A[mid] >= K && ( mid == 1 || A[mid-1] < K )) // checking conditions for lowerbound
#             return mid ;
#         else if(A[mid] >= K) // answer should be in left part 
#             high = mid - 1 ;
#         else                // answer should in right part if it exists
#             low = mid + 1 ;
#     }
#     return mid ; // this will execute when there is no element in the given array which >= K
# }
