#include <iostream>
#define ll long long
using namespace std;
int main(){
	int i,t;
	cin>>t;
	while(t--){
		int sum=0;
		int b=0;
		int n,k;
		cin>>n>>k;
		int a[n];
		for (int j=0;j<n;j++){
			cin>>a[j];
		}
		
		for (int m=0;m<n;m++){
			sum=sum+a[m];
			if (a[m]>k){
				cout<<-1<<endl;
				break;
			}
			if (sum>k){
				b=b+1;
				sum=a[m];
			}
		}
		cout<<b+1<<endl;
	}
    return 0;
}
