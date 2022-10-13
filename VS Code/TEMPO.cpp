#include<bits/stdc++.h>
using namespace std;
 
int main()
{
	string s;
	s="if";
	char arr[]="ifendifififendifendif";
	int i;
	for(i=0;i<sizeof(arr)/sizeof(arr[0])-1;i++)
	{
		s+=arr[i];
	}
	for(auto j=s.begin();j!=s.end();j++)
	{
		cout<<*j<<" ";
	}
	cout<<endl<<s.size()<<endl;
	for(i=0;i<s.size();i++)
	{
		cout<<s[i];
	}
	cout<<endl;
	string temp=s.substr(0,2);
	if(temp=="if")
	cout<<"working if found";
	temp=s.substr(s.size()-5,5);
	if(temp=="endif")
	cout<<"working endif found";

	return 0;
}