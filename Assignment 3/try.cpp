#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

int main(){

    string test = "qmnjvsa nv wewc flct vprj tj tvvplvl fv xja vqildhc xmlnvc nacyclpa fc gyt vfvw. fv wgqyp, pqq pqcs y wsq rx qmnjvafy cgv tlvhf cw tyl aeuq fv xja tkbv cqnsqs. lhf avawnc cv eas fuqb qvq tc yllrqr xxwa cfy. psdc uqf avrqc gefq pyat trac xwv taa wwd dv eas flcbq. vd trawm vupq quw x decgqcwt, yq yafl vlqs yqklhq! snafq vml lhvqpawr nqg_vfusr_ec_wawy qp fn wgawdgf.";

    vector<int> freq(26,0);
    int t=0;

    for(int i=0; i<test.size(); i++)
    {
        if('A'<=test[i] && test[i]<='Z')
        test[i] = test[i] - 'A' + 'a';

        if('a'<=test[i] && test[i]<='z')
        freq[ test[i]-'a' ]++;
            
    }

    string test1 = test;

    test1.erase(remove(test1.begin(),test1.end(), ' '), test1.end());
    test1.erase(remove(test1.begin(),test1.end(), '.'), test1.end());
    test1.erase(remove(test1.begin(),test1.end(), '!'), test1.end());
    test1.erase(remove(test1.begin(),test1.end(), ','), test1.end());
    test1.erase(remove(test1.begin(),test1.end(), '_'), test1.end());

    map<char,char> sub;
    
    sub = {{'a','T'}, {'b','V'}, {'c','I'}, {'d','U'}, {'e','C'}, {'f','H'}, {'g','G'}, {'h','P'}, {'i','Q'}, {'j','B'}, {'k','Z'}, {'l','S'}, {'m','K'}, {'n','R'}, {'o','J'}, {'p','D'}, {'q','A'}, {'r','W'}, {'s','F'}, {'t','L'}, {'u','M'}, {'v','E'}, {'w','O'}, {'x','Y'}, {'y','N'}, {'z','X'}};

    for(int i=0; i<test.size()-5; i++)
    {

        if(('a'<=test[i] && test[i]<='z') && (t+3)<test1.size())
        {
            if(t%5==0)
            test[i] = sub[test1[t+3]];
            else if(t%5==1)
            test[i] = sub[test1[t+1]];
            else if(t%5==2)
            test[i] = sub[test1[t+2]];
            else if(t%5==3)
            test[i] = sub[test1[t-3]];
            else if(t%5==4)
            test[i] = sub[test1[t-3]];

            t++;
        }

    }

    for(int i=test.size()-1; ;i--)
    {
        if('A'<=test[i] && test[i]<='Z')break;

        if('a'<=test[i] && test[i]<='z')
        test[i] = sub[test[i]];
    }

    cout << test << endl;

    return 0;

}