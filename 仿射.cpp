//FMXVEDKAPHFERBNDKRXRSREFMORUDSDKDVSHVUFEDKAPRKDLYEVLRHHRH
#include<stdio.h>
#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define db double
#define io_opt ios::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#ifdef io_opt
#define scanf error
#define printf error
#endif
ll gcd(ll a,ll b){
	return b==0?a:gcd(b,a%b);
}
ll speed(ll a,ll b,ll p){
	ll cur=a,ans=1;
	while(b){
		if(b&1) ans=ans*cur%p;
		cur=cur*cur%p;
		b>>=1;
	}
	return ans%p;
}
ll exgcd(ll a,ll b,ll &x,ll &y){//+mod and %mod before using 
    if(b==0){
        x=1;y=0;
        return a;
    }
    ll ret=exgcd(b,a%b,x,y);
    ll tmp=y;   
    y=x-a/b*y;
    x=tmp;
    return ret;     
}
class AffineCipher{//26
private:
	string Plaintext,Ciphertext;
	ll Key1,Key2,invKey2,mod;
	bool checkKey(ll x){
		return x!=-1;
	}
	bool coPrime(ll x,ll y){
		return gcd(x,y)==1;
	}
	void Atoa(string &x){
		for(int i=0;i<x.size();i++){
			if(x[i]>='A'&&x[i]<='Z'){
				x[i]+='a'-'A';
			}
		}
	}
public:
	void showKey(){
		cout<<"Key1: "<<Key1<<' '<<"Key2: "<<Key2<<' '<<"invKey2: "<<invKey2<<endl;
	}
	string showP(){
		return Plaintext;
	}
	string showC(){
		return Ciphertext;
	}
	AffineCipher(string C,ll mm=26):mod(mm){
		Atoa(C);
		Ciphertext=C;
		Key1=Key2=invKey2=-1;
	}
	AffineCipher(string P,ll K1,ll K2,ll mm=26):mod(mm){
		Atoa(P);
		Plaintext=P;
		if(!fillKey(K1,K2)){
			cout<<"Error"<<endl;
		}
	}
	bool fillKey(ll K1,ll K2,ll iK2=-1){
		if(K2!=-1&&!coPrime(K2,mod)||iK2!=-1&&!coPrime(iK2,mod)){
			return false;
		}
		K1%=mod,K2%=mod,iK2%=mod;
		if(iK2==-1){
			ll tmp;
			exgcd(K2,mod,iK2,tmp);
			iK2=(iK2+mod)%mod;
		}
		else if(K2==-1){
			ll tmp;
			exgcd(iK2,mod,K2,tmp);
			K2=(K2+mod)%mod;
		}
		else{
			ll tmp,tmpiK2;
			exgcd(K2,mod,tmpiK2,tmp);
			tmpiK2=(tmpiK2+mod)%mod;
			if(iK2!=tmpiK2) return false;
		}
		Key1=K1,Key2=K2,invKey2=iK2;
		return true;
	}
	void encode(){
		Ciphertext="";
		for(int i=0;i<Plaintext.size();i++){
			if(Plaintext[i]<'a'||Plaintext[i]>'z'){
				Ciphertext+=Plaintext[i];
				continue;
			}
			ll cur=Plaintext[i];
			cur-='a';
			//cur=(cur+Key1)%mod*Key2%mod;
			cur=(cur*Key2%mod+Key1)%mod;
			Ciphertext+=cur+'a';
		}
		cout<<"Encode succeed! "<<Plaintext<<" -> "<<Ciphertext<<endl;
	}
	void decode(){
		Plaintext="";
		for(int i=0;i<Ciphertext.size();i++){
			if(Ciphertext[i]<'a'||Ciphertext[i]>'z'){
				Plaintext+=Ciphertext[i];
				continue;
			}
			ll cur=Ciphertext[i];
			cur-='a';
			//cout<<invKey2<<endl;
			//cout<<invKey2<<endl;
			//cur=(cur*invKey2-Key1+mod)%mod;
			cur=(cur-Key1+mod)%mod*invKey2%mod;
			Plaintext+=cur+'a';
		}
		//cout<<"Decode succeed! "<<Ciphertext<<" -> "<<Plaintext<<endl;
		//cout<<Plaintext<<endl;
	}
	void analyzeString(string x){
		Atoa(x);
		vector<int>v(26);
		for(int i=0;i<x.size();i++){
			if(x[i]<'a'||x[i]>'z') continue;
			v[x[i]-'a']++;
		}
		for(int i=0;i<26;i++){
			cout<<char(i+'a')<<": "<<v[i]<<endl;
		}
	}
	void analyzePlaintext(){
		analyzeString(Plaintext);
	}
	void analyzeCiphertext(){
		analyzeString(Ciphertext);
	}
};
int main(){
	/*AffineCipher C("FMXVEDKAPHFERBNDKRXRSREFMORUDSDKDVSHVUFEDKAPRKDLYEVLRHHRH");
	C.analyzeCiphertext();
	for(int i=0;i<26;i++){
		for(int j=0;j<26;j++){
			if(C.fillKey(i,-1,j)){
				cout<<"K1:"<<i<<' '<<"iK2:"<<j<<endl;
				C.decode();
				cout<<C.showP()<<endl<<endl;;
			}
		}
	}*/
	AffineCipher C("FMXVEDKAPHFERBNDKRXRSREFMORUDSDKDVSHVUFEDKAPRKDLYEVLRHHRH");
	AffineCipher c("R");
	C.analyzeCiphertext();
	for(int i=0;i<26;i++){
		for(int j=0;j<26;j++){
			if(C.fillKey(i,-1,j)){
				c.fillKey(i,-1,j);
				c.decode();
				if(c.showP()[0]=='e'){
					C.decode();
					C.showKey();
					cout<<C.showP()<<endl<<endl;;
				}
				
				
			}
		}
	}
	/*AffineCipher C("kbcxfi_1q_quxob_ogqc!");
	C.fillKey(6,15,-1);
	C.decode();
	cout<<C.showP();*/
	return 0;
} 
