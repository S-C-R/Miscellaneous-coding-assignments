#include <iostream>
#include <string>

using namespace std;

string stringOne = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA";  //Place first string here
string stringTwo = "GTCGTTCGGAATGCCGTTGCTCTGTAAA";  //Place second string here
//ACCGGTCGAGTGCGCGGAAGCCGGCCGAA
//GTCGTTCGGAATGCCGTTGCTCTGTAAA

//1 means up
//-1 means left
//0 means diag


void Print_LCS(int** b,int i,int j)
{
	if(i==0||j==0)
	{
		return;
	}
	if(b[i][j]==0)
	{
		Print_LCS(b,i-1,j-1);
		cout<<stringOne[i]<<" ";
	}
	else if(b[i][j]==1)
	{
		Print_LCS(b,i-1,j);
	}
	else
	{
		Print_LCS(b,i,j-1);
	}
}

int main()
{
	int sizeOne = stringOne.length();
	int sizeTwo = stringTwo.length();
	int a[sizeOne+1][sizeTwo+1];
	int c[sizeOne][sizeTwo];
	for(int i=1;i<sizeOne;i++)
	{
		c[i][0] = 0;
	}
	for(int i=0;i<sizeTwo;i++)
	{
		c[0][i] = 0;
	}
	for(int i=1;i<sizeOne;i++)
	{
		for(int j=1;j<sizeTwo;j++)
		{
			if(stringOne[i]==stringTwo[j])
			{
				c[i][j] = c[i-1][j-1]+1;
				a[i][j] = 0;
			}
			else if(c[i-1][j]>=c[i][j-1])
			{
				c[i][j] = c[i-1][j];
				a[i][j] = 1;
			}
			else
			{
				c[i][j] = c[i][j-1];
				a[i][j] = -1;
			}
		}
	}
	int *b[sizeOne+1];
    for (int i = 1; i < sizeOne+1;i++)
    {
        b[i] = new int[sizeTwo+1];
        for(int j=1;j < sizeTwo+1;j++)
        {
            b[i][j] = a[i][j];
        }
    }
	Print_LCS(b,sizeOne,sizeTwo);
	return 0;
}