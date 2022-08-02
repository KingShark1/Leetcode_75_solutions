#include <bits/stdc++.h>
#include <vector>

using namespace std;

vector<int> spiralOrder(vector<vector<int>>& matrix){
	int count =0;
        int n=matrix.size();
        int m=matrix[0].size();
        int total= n*m;
        vector<int> ans;
        int start_row=0,end_row=n-1,start_col=0,end_col=m-1;
        
        while(count<total) {
            for(int i=start_col;count<total && i<= end_col;i++) {
                ans.push_back(matrix[start_row][i]);
                count++;
            }
            start_row++;
            
            for(int i=start_row; count<total && i<=end_row;i++){
                ans.push_back(matrix[i][end_col]);
                count++;
            }
            end_col--;
            
            for(int i=end_col;count<total && i>=start_col;i--) {
                ans.push_back(matrix[end_row][i]);
                count++;
            }
            end_row--;
            
            for(int i=end_row;count<total && i>=start_row;i--) {
                ans.push_back(matrix[i][start_col]);
                count++;
            }
            start_col++;
        }
        return ans;
}

int main(){
	vector<vector<int>> matrix = {{1, 2, 3, 4}, {4, 5, 6, 7}, {7, 8, 9, 10}};
	vector<int> ans = spiralOrder(matrix);
	for(int i = 0; i < ans.size(); i++)
		cout << ans[i] << '\t';
	cout<<endl;
	return 0;
}