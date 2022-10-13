// C++ program to find number of ways to get sum 'x' with 'n'
// dice where every dice has 'm' faces
#include <iostream>
#include <string.h>
using namespace std;

// The main function that returns number of ways to get sum 'x'
// with 'n' dice and 'm' throws.
int findWays(int m, int n, int x)
{
    // Base cases
    if (x < 1)   return 0;
    if (n == 1)  return (x <= m);

    int i, numberOfWays = 0;
    for (i = 1; i <= m; ++i)
        numberOfWays += findWays(m, n-1, x - i);
    return numberOfWays;
}

// Driver program to test above functions
int main()
{
	int n,m,x;
	cout<<"Enter values: \n";
	cout<<"No of faces: ";
	cin>>m;
	cout<<"No of dice: ";
	cin>>n;
	cout<<"Sum: ";
	cin>>x;
    cout << "No of ways: "<<findWays(m, n, x) << endl;
    
    return 0;
}