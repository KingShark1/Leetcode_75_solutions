#include <bits/stdc++.h>
#include <vector>

using namespace std;

int util(vector<vector<int>>&grid,bool top,int i,int j)
	{   
		if(top==0&&i==grid.size()-1)return j;
		if(top==1)
		{
			if(grid[i][j]==1)
			{   
				if(j+1>=grid[0].size()||grid[i][j+1]==-1)return -1;
				return util(grid,!top,i,j+1);
			}
			else
			{
				if(j-1<0||grid[i][j-1]==1)return -1;
				return util(grid,!top,i,j-1);
			}
		}
		else
		{
			return util(grid,!top,i+1,j);
		}        
	}

vector<int> findBall(vector<vector<int>>& grid) {
	vector<int>ans(grid[0].size(),-1);
	for(int i=0;i<grid[0].size();i++)
	{
		ans[i]=util(grid,true,0,i);
	}
	return ans;
}

int main(){
	vector<vector<int>> grid = {{1,1,1,-1,-1},{1,1,1,-1,-1},{-1,-1,-1,1,1},{1,1,1,1,-1},{-1,-1,-1,-1,-1}};
	vector<int> ans = findBall(grid);
	
	for(int i = 0; i < ans.size(); i++){
		cout << ans[i] << ' ';
	}
	cout<<endl;
	return 0;
}