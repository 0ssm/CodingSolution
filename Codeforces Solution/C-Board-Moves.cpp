#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    long long n;
	    cin>>n;
	    
	    if(n == 1){
	        cout<<0<<endl;
	    } else{
	    
	    long long result = 0;
	    for(long long i = 1; i <= n/2; ++i){
	        result += 8 * i * i;
	   }
	   
	    cout << result << endl;
	    
	        
	    }
	}   
}
