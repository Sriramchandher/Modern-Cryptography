#include<iostream>
#include<vector>
using namespace std;

int main(){

    vector<int> key{9,2,9,2,5,5,2,2,2,1};
    string cipher = "Kg fcwd qh vin pnzy hjcocnt, cjjwg ku wnth nnyvng kxa cjjwg. Urfjm xwy yjg rbbufqwi \"vjg_djxn_ofs_dg_rmncbgi\" yq iq uqtxwlm. Oca zxw qcaj vjg tctnplyj hqs cjn pjcv ejbvdnt. Yt hkpe cjn gcnv, aqv okauy bknn ongm vt zvvgs vcpkh bqtft cjntj.";
    int k=0;

    for(int i=0; i<cipher.size(); i++)
    {
        if('a'<=cipher[i] && cipher[i]<='z')
        {
            cipher[i] = (cipher[i]-'a'-key[k]+26)%26 + 'a';
            k = (k+1)%10;
        }
        else if('A'<=cipher[i] && cipher[i]<='Z')
        {
            cipher[i] = (cipher[i]-'A'-key[k]+26)%26 + 'A';
            k = (k+1)%10;
        }
    }

    cout << cipher << endl;

    return 0;

}