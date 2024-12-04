""" 
Solution in C++:

#include <bits/stdc++.h>
using namespace std;

int main() {
    
    int n;
    cin >> n;
    
    int hash = 1, space = n - 1;
    
    for (int i = 0; i < n; i++)
    {
        for (int h = 1; h <= hash; h++)
        {
            cout << "#";
        }
        for (int s = 1; s <= space; s++)
        {
            cout << " ";
        }
        cout << "\n";
        hash++;
        space--;
    }
    

    return 0;
}


"""

""" ------ python solution ----------- """

n = int(input())

hash_char = 1
space = n - 1

for i in range(n):
	for i in range(hash_char):
		print("#", end = "")

	for i in range(space):
		print(" ", end = "")

	print()
	hash_char += 1
	space -= 1