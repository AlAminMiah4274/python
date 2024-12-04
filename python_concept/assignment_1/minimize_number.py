"""
Solution in C++:

#include <bits/stdc++.h>
using namespace std;

int main() {
    
    int n;
    cin >> n;
    
    int arr[n];
    bool is_even = true;
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
        
        if (arr[i] % 2 != 0) is_even = false;
    }
    
    
    bool is_even_during_operation = true;
    int operation_count = 0;
    while (is_even)
    {
        for (int i = 0; i < n; i++)
        {
            arr[i] = arr[i] / 2;
            
            
            if (arr[i] % 2 != 0) is_even_during_operation = false;
        }
        
        operation_count++;
        if (!is_even_during_operation)
        {
            break;
        }
    }
    
    
    cout << operation_count;
    

    return 0;
}


"""


""" ------ python solution ----------- """

n = int(input())

arr = list(map(int, input().split()))
is_even = all(num % 2 == 0 for num in arr)

is_even_during_operation = True
operation_count = 0

while is_even:
    for i in range(n):
        arr[i] = arr[i] // 2

        if arr[i] % 2 != 0:
            is_even_during_operation = False

    operation_count += 1
    if not is_even_during_operation:
        break

print(operation_count)

