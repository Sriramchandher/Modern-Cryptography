#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){

    string test = "Mewa wa mey twsam iepjoys gt mey ipbya. Pa xgn iph ayy, meysy wa hgmewhr gt whmysyam wh mey iepjoys. Agjy gt mey kpmys iepjoysa vwkk oy jgsy whmysyamwhr meph mewa ghy! Mey iguy nayu tgs mewa jyaapry wa p awjfky anoamwmnmwgh iwfeys wh vewie uwrwma epby oyyh aewtmyu ox 8 fkpiya. Mey fpaavgsu wa \"mxSrN03uwdd\" vwmegnm mey dngmya.";

    string test1 = test;

    vector<int> freq(26,0);

    for(int i=0; i<test.size(); i++)
    {
        if('A'<=test[i] && test[i]<='Z')
        test[i] = test[i] - 'A' + 'a';

        freq[ test[i]-'a' ]++;
    }

    for(int i=0; i<freq.size(); i++)
    {
        char k = 'a'+i;
        cout << k << ": " << freq[i] << endl;
    }

    for(int i=0; i<test.size(); i++)
    {
        if(test[i] == 'y')
        test[i] = 'E';
        if(test[i] == 'm')
        test[i] = 'T';
        if(test[i] == 'e')
        test[i] = 'H';
        if(test[i] == 'p')
        test[i] = 'A';
        if(test[i] == 'w')
        test[i] = 'I';
        if(test[i] == 'a')
        test[i] = 'S';
        if(test[i] == 'f')
        test[i] = 'P';
        if(test[i] == 'v')
        test[i] = 'W';
        if(test[i] == 'g')
        test[i] = 'O';
        if(test[i] == 's')
        test[i] = 'R';
        if(test[i] == 'u')
        test[i] = 'D';
        if(test[i] == 't')
        test[i] = 'F';
        if(test[i] == 'n')
        test[i] = 'U';
        if(test[i] == 'd')
        test[i] = 'Q';
        if(test[i] == 'x')
        test[i] = 'Y';
        if(test[i] == 'i')
        test[i] = 'C';
        if(test[i] == 'h')
        test[i] = 'N';
        if(test[i] == 'r')
        test[i] = 'G';
        if(test[i] == 'o')
        test[i] = 'B';
        if(test[i] == 'j')
        test[i] = 'M';
        if(test[i] == 'b')
        test[i] = 'V';
        if(test[i] == 'k')
        test[i] = 'L';
        if('0'<=test[i] && test[i]<='9')
        {
            int k = test[i]-'0';
            k = ((k-4)+10)%10;
            test[i] = '0'+k;
        }
    }

    for(int i=0; i<test1.size(); i++)
    {
        if('a'<=test1[i] && test1[i]<='z')
        test[i] = test[i] - 'A' + 'a';
    }

    cout << test << endl;

    return 0;

}