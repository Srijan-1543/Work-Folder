// C++ program to find Minimum
// number of jumps to reach end
#include <bits/stdc++.h>
#include <conio.h>
using namespace std;

// Function to return the minimum number
// of jumps to reach arr[h] from arr[l]
int minJumps(int arr[], int n)
{

	// Base case: when source and
	// destination are same
	// cout<<"start arr \n";
	// for(int j=0;j<n;j++)
	// {
	// 	cout<<arr[j]<<"\n";
	// }
	// cout<<"start n \n";
	// cout<<n;
	if (n == 1)
		return 0;

	// Traverse through all the points
	// reachable from arr[l]
	// Recursively, get the minimum number
	// of jumps needed to reach arr[h] from
	// these reachable points
	int res = INT_MAX;
	for (int i = n - 2; i >= 0; i--) {
		// cout<<"i:"<<i<<" n:"<<n<<endl;
		if (i + arr[i] >= n - 1) {
			// cout<<"i:"<<i<<" n:"<<n<<"arr[i]:"<<arr[i]<<endl;
			int sub_res = minJumps(arr, i + 1);
			cout<<"sub_res:"<<sub_res<<endl;
			if (sub_res != INT_MAX)
				res = min(res, sub_res + 1);
				cout<<"res:"<<res<<endl;
		}
	}

	return res;
}

// Driver Code
int main()
{
	system("CLS");
	int arr[] = { 1, 3, 6, 3, 2,
				3, 6, 8, 9, 5 };
	int n = sizeof(arr) / sizeof(arr[0]);
	cout << "Minimum number of jumps to";
	cout << " reach the end is " <<endl<< minJumps(arr, n);
	return 0;
}


