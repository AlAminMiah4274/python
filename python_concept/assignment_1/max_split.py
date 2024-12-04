""" 
Solution in C++:

#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;

    int balance = 0; 
    vector<string> balanced_strings;
    string current_substring;

    for (char c : S) {
        current_substring += c;
        if (c == 'R') {
            balance++;
        } else if (c == 'L') {
            balance--;
        }

        if (balance == 0) {
            
            balanced_strings.push_back(current_substring);
            current_substring.clear();
        }
    }


    cout << balanced_strings.size() << endl;
    for (const string &str : balancedStrings) {
        cout << str << endl;
    }

    return 0;
}


"""

""" ------ python solution ----------- """

def split_balanced_strings(S):
    balance = 0  # To track the balance between 'R' and 'L'
    balanced_strings = []
    current_substring = ""

    for char in S:
        current_substring += char
        if char == 'R':
            balance += 1
        elif char == 'L':
            balance -= 1
        
        if balance == 0:
            # A balanced substring is found
            balanced_strings.append(current_substring)
            current_substring = ""

    # Print the results
    print(len(balanced_strings))
    for s in balanced_strings:
        print(s)

# Input
S = input()
split_balanced_strings(S)