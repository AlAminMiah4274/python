""" 
Solution in c++:

#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes 
	
	int n;
	cin >> n;
	
	int arr[n];
	for (int i = 0; i < n; i++)
	{
	    cin >> arr[i];
	}
    
    
    map<int, int> count;
    
    for (int i = 0; i < n; i++)
    {
        count[arr[i]]++;
    }
    
    int to_be_removed = 0;
    for (int i = 0; i < n; i++)
    {
        // cout << num.first << " " << num.second << "\n";
        
        if (arr[i] != count[arr[i]])
        {
            to_be_removed++;
            if (arr[i] != count[arr[i]] && count[arr[i]] != 0)
            {
                count[arr[i]]--;
            }
        }
    }
    
    
    cout << to_be_removed;

    return 0;
}


"""

""" ------ python solution ----------- """


n = int(input())
arr = list(map(int, input().split()))



def remove_numbers(n, arr):
    count = {}
    
    for i in range(n):
        count[arr[i]] = count.get(arr[i], 0) + 1
    
    to_be_removed = 0
    for i in range(n):
        if arr[i] != count[arr[i]]:
            to_be_removed += 1
            if arr[i] != count[arr[i]] and count[arr[i]] != 0:
                count[arr[i]] -= 1
    
    return to_be_removed



result = remove_numbers(n, arr)
print(result)

