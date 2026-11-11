def maxSubarraySum(arr):
    res = arr[0]
    maxEnding = arr[0]
    for i in range(1, len(arr)):
        maxEnding = max(arr[i], maxEnding + arr[i])
        res = max(res, maxEnding)
    return res

'''
gog
If arr = [2, 3, -8, 7, -1, 2, 3]:

Index (i)	  Element (arr[i])	  Calculation (maxEnding = max(arr[i], maxEnding + arr[i]))   	New maxEnding      	Global Max (res = max(res, maxEnding))0 (start)	2	Initialized	2	2
1	           3	                           max(3, 2 + 3)	                                               5	       max(2, 5) = 5
2	           -8                          	max(-8, 5 + (-8))                                            -3           max(5, -3) = 5
3         	7                            	max(7, -3 + 7)	                                             7           	max(5, 7) = 7
4	        -1	                            max(-1, 7 + (-1))                                        	6               	max(7, 6) = 7
5        	2                            	max(2, 6 + 2)                                             	8             	max(7, 8) = 8
6        	3	                           max(3, 8 + 3)	                                               11           	max(8, 11) = 11
'''
