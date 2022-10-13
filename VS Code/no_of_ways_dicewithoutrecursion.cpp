// C++ program to find number of ways to get sum 'x' with 'n'
// dice where every dice has 'm' faces
#include <iostream>
#include <string.h>
#include<iomanip>
using namespace std;

// The main function that returns number of ways to get sum 'x'
// with 'n' dice and 'm' with m faces.
int findWays(int m, int n, int x)
{
  // Create a table to store results of subproblems. One extra
  // row and column are used for simplicity (Number of dice
  // is directly used as row index and sum is directly used
  // as column index). The entries in 0th row and 0th column
  // are never used.
  int table[n + 1][x + 1];
  memset(table, 0, sizeof(table)); // Initialize all entries as 0

  // Table entries for only one dice
  for (int j = 1; j <= m && j <= x; j++)
    {
        table[1][j] = 1;
    }
    cout<<endl;

  // Fill rest of the entries in table using recursive relation
  // i: number of dice, j: sum
  for (int i = 2; i <= n; i++)
    for (int j = 1; j <= x; j++)
      for (int k = 1; k <= m && k < j; k++)
        {
        // cout<<"table["<<i<<"]["<<j<<"]: "<<table[i][j]<<endl<<endl;
        table[i][j] += table[i-1][j-k];
        }
        cout<<endl;

  for (int i = 0; i <= n; i++)
  {
  for (int j = 0; j <= x; j++)
  {
    cout<<setw(3);
    cout << table[i][j] << " ";
  }
  cout << endl;
  } 
  cout<<endl;
  return table[n][x];
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
    cout << "No of ways: \n\n"<<findWays(m, n, x) << endl;
    
    return 0;
}
