#----------------------CODE-------------------#
#-----------------------BY-------------------#
#-------------------ABHISHEK RAJ-------------------#
#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
    while(t--){
        int d;
        int c;
        cin>>d>>c;
        while(d>0 && c>0){
            d=d-c;
            c=c//2;
        }
        if c==0 && d<=0{
            cout<<1<<endl;
        }
        else if (c==0){
            cout<<0<<endl;
        }
        else if d<=0{
            cout<<1<<endl;
        }
    }
