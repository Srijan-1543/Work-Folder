#include<bits/stdc++.h>
using namespace std;

int main()
{
	int i,j,n;
	cout<<"Enter n: ";
	cin>>n;
	vector<vector<char>> board(n,vector<char>(n,'t'));
	vector<vector<int>> move(n,vector<int>(n,0));
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			cin>>board[i][j];
		}
	}

	queue<pair<int,int>> q;
	q.push(make_pair(0,0));
	while(!q.empty())
	{
		i=q.front().first;
		j=q.front().second;
		q.pop();

		if(board[i-1][j]=='D' && i>0)
			{
				if(move[i-1][j]>move[i][j]+1)
				{
					move[i-1][j]=move[i][j]+1;
				}
				q.push(make_pair(i-1,j));
			}
		if(board[i+1][j]=='D' && i<n-1)
			{
				if(i==0)
				{
					move[i+1][j]=move[i][j]+1;
				}
				if(move[i+1][j]>move[i][j]+1)
				{
					move[i+1][j]=move[i][j]+1;
				}
				q.push(make_pair(i+1,j));
			}
		
		if(board[i][j-1]=='D' && j>0)
			{
				if(move[i][j-1]>move[i][j]+1)
				{
					move[i][j-1]=move[i][j]+1;
				}
				q.push(make_pair(i,j-1));
			}
		if(board[i][j+1]=='D' && j<n-1)
			{
				if(j==0)
				{
					move[i][j+1]=move[i][j]+1;
				}
				if(move[i][j+1]>move[i][j]+1)
				{
					move[i][j+1]=move[i][j]+1;
				}
				q.push(make_pair(i,j+1));
			}
		
	}
	cout<<move[n-1][n-1];
	return 0;
}