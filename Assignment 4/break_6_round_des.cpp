#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <cstdlib>
#include <time.h>
using namespace std;

string charac1 = "4008000004000000";
string charac2 = "0020000800000400";
map<char,string> hex2bin {{'0',"0000"}, {'1',"0001"}, {'2',"0010"}, {'3',"0011"}, {'4',"0100"}, {'5',"0101"}, {'6',"0110"}, {'7',"0111"}, {'8',"1000"}, {'9',"1001"}, {'A',"1010"}, {'B',"1011"}, {'C',"1100"}, {'D',"1101"}, {'E',"1110"}, {'F',"1111"}}; 
map<int,string> dec2plain {{0,"f"}, {1,"g"}, {2,"h"}, {3,"i"}, {4,"j"}, {5,"k"}, {6,"l"}, {7,"m"}, {8,"n"}, {9,"o"}, {10,"p"}, {11,"q"}, {12,"r"}, {13,"s"}, {14,"t"}, {15,"u"}};
map<string,string> bin2plain {{"0000","f"}, {"0001","g"}, {"0010","h"}, {"0011","i"}, {"0100","j"}, {"0101","k"}, {"0110","l"}, {"0111","m"}, {"1000","n"}, {"1001","o"}, {"1010","p"}, {"1011","q"}, {"1100","r"}, {"1101","s"}, {"1110","t"}, {"1111","u"}};
map<char,string> plain2bin {{'f',"0000"}, {'g',"0001"}, {'h',"0010"}, {'i',"0011"}, {'j',"0100"}, {'k',"0101"}, {'l',"0110"}, {'m',"0111"}, {'n',"1000"}, {'o',"1001"}, {'p',"1010"}, {'q',"1011"}, {'r',"1100"}, {'s',"1101"}, {'t',"1110"}, {'u',"1111"}}; 
vector<vector<int>> ip {{58,50,42,34,26,18,10,2},
                      {60,52,44,36,28,20,12,4},
                      {62,54,46,38,30,22,14,6},
                      {64,56,48,40,32,24,16,8},
                      {57,49,41,33,25,17,9,1},
                      {59,51,43,35,27,19,11,3},
                      {61,53,45,37,29,21,13,5},
                      {63,55,47,39,31,23,15,7}};
vector<vector<int>> rev_ip {{40,8,48,16,56,24,64,32},
                    {39,7,47,15,55,23,63,31},
                    {38,6,46,14,54,22,62,30},
                    {37,5,45,13,53,21,61,29},
                    {36,4,44,12,52,20,60,28},
                    {35,3,43,11,51,19,59,27},
                    {34,2,42,10,50,18,58,26},
                    {33,1,41,9,49,17,57,25}};
vector<vector<int>> fp {{8, 40, 16, 48, 24, 56, 32, 64},
                        {7, 39, 15, 47, 23, 55, 31, 63},
                        {6, 38, 14, 46, 22, 54, 30, 62},
                        {5, 37, 13, 45, 21, 53, 29, 61},
                        {4, 36, 12, 44, 20, 52, 28, 60},
                        {3, 35, 11, 43, 19, 51, 27, 59},
                        {2, 34, 10, 42, 18, 50, 26, 58},
                        {1, 33, 9,  41, 17, 49, 25, 57}};

vector<vector<int>> rev_fp {{57, 49, 41, 33, 25, 17, 9, 1},
                       {59, 51, 43, 35, 27, 19, 11, 3},
                       {61, 53, 45, 37, 29, 21, 13, 5},
                       {63, 55, 47, 39, 31, 23, 15, 7},
                       {58, 50, 42, 34, 26, 18, 10, 2},
                       {60, 52, 44, 36, 28, 20, 12, 4},
                       {62, 54, 46, 38, 30, 22, 14, 6},
                       {64, 56, 48, 40, 32, 24, 16, 8}};

vector<int> expand {32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1};

vector<int> s_box_perm {16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25};

vector<int> rev_s_box_perm {9,17,23,31,13,28,2,18,24,16,30,6,26,20,10,1,8,14,25,3,4,29,11,19,32,12,22,7,5,27,15,21};

string hex_to_bin(string k){

    string res = "";
    for(int i=0; i<k.size(); i++)
    {
        res += hex2bin[k[i]];
    }

    return res;

}

string apply_per(string n, vector<vector<int>> perm){

    if(n.size()==16)
        n = hex_to_bin(n);
    string res = "";

    for(int i=0; i<perm.size(); i++)
    {
        for(int j=0; j<perm[i].size(); j++)
        res += n[perm[i][j]-1];
    }

    return res;

}

string bt_xor(string n, string m){

    string res = "";

    for(int i=0; i<n.size(); i++)
    {
        res += to_string( (n[i]-'0')^(m[i]-'0') );
    }

    return res;

}

string bin_to_plain(string k){

    string res = "";

    for(int i=0; i+3<k.size(); i=i+4)
    {
        string p;
        p += k[i];
        p += k[i+1];
        p += k[i+2];
        p += k[i+3];
        res += bin2plain[p];
    }

    return res;

}

string e32to48(string k){

    string res;

    for(int i=0; i<48; i++)
    {
        res += k[expand[i]-1];
    }

    return res;

}

vector<string> create_plain(int n, string charac){

    vector<string> res;
    string in_charac = apply_per(charac, rev_ip);

    for(int i=0; i<n; i++)
    {
        string plain_text = "";
        string binary_pt = "";
        for(int j=0; j<16; j++)
        {
            int h = rand()%16;
            plain_text += dec2plain[h];
            binary_pt += plain2bin[dec2plain[h][0]];
        }
        string binary_pt2 = bt_xor(binary_pt, in_charac);
        string plain_text2 = bin_to_plain(binary_pt2);

        res.push_back(plain_text);
        res.push_back(plain_text2);
    }

    return res;

}

void create_cipher(string charac){

    if(charac == charac1)
        system("python3 gen_out.py 1");
    else
        system("python3 gen_out.py 2");

    return ;

}

void generate_plain_cipher(int no_plaintext, string charac){

    vector<string> inpu = create_plain(no_plaintext, charac);

    fstream infile;

    if(charac == charac1)
    infile.open("plaintext1.txt", ios::trunc | ios::out | ios::in);
    else
    infile.open("plaintext2.txt", ios::trunc | ios::out | ios::in);

    for(int i=0; i<inpu.size(); i++)
    infile << inpu[i] << endl;

    infile.close();

    create_cipher(charac);

}

void break_6_round_des(int no_plaintext){

    fstream in1, in2, out1, out2;

    in1.open("plaintext1.txt", ios::in);
    in2.open("plaintext2.txt", ios::in);
    out1.open("ciphertext1.txt", ios::in);
    out2.open("ciphertext2.txt", ios::in);

    vector<string> inlist1, inlist2, outlist1, outlist2;
    string line;

    while (in1) {
        getline(in1, line);
        if(line!="") inlist1.push_back(line);
    }
    in1.close();
    while (in2) {
        getline(in2, line);
        if(line!="") inlist2.push_back(line);
    }
    in2.close();
    while (out1) {
        getline(out1, line);
        if(line!="") outlist1.push_back(line);
    }
    out1.close();
    while (out2) {
        getline(out2, line);
        if(line!="") outlist2.push_back(line);
    }
    out2.close();

    vector<string> bi_out1, bi_out2;

    for(int i=0; i<outlist1.size(); i++)
    {
        string k = "";
        for(int j=0; j<outlist1[i].size(); j++)
        {
            k += plain2bin[outlist1[i][j]];
        }
        bi_out1.push_back(k);
    } 
    for(int i=0; i<outlist2.size(); i++)
    {
        string k = "";
        for(int j=0; j<outlist2[i].size(); j++)
        {
            k += plain2bin[outlist2[i][j]];
        }
        bi_out2.push_back(k);
    } 

    vector<string> rev_fp1, rev_fp2;

    for(int i=0; i<bi_out1.size(); i++) rev_fp1.push_back(apply_per(bi_out1[i],rev_fp));
    for(int i=0; i<bi_out2.size(); i++) rev_fp2.push_back(apply_per(bi_out2[i],rev_fp));

    vector<string> r5_1, r5_2;

    for(int i=0; i<bi_out1.size(); i++)
    {
        string k = "";
        for(int j=0; j<32; j++)
        k += rev_fp1[i][j];

        r5_1.push_back(k);
    }
    for(int i=0; i<bi_out2.size(); i++)
    {
        string k = "";
        for(int j=0; j<32; j++)
        k += rev_fp2[i][j];
        
        r5_2.push_back(k);
    }

    for(int i=0; i<r5_1.size(); i++) r5_1[i] = e32to48(r5_1[i]);
    for(int i=0; i<r5_2.size(); i++) r5_2[i] = e32to48(r5_2[i]);

    vector<string> in_sbox1, in_sbox2;

    for(int i=0; i+1<r5_1.size(); i = i+2) in_sbox1.push_back((bt_xor(r5_1[i],r5_1[i+1])));
    for(int i=0; i+1<r5_2.size(); i = i+2) in_sbox2.push_back((bt_xor(r5_2[i],r5_2[i+1])));

    vector<string> rout1, rout2;

    for(int i=0; i+1<rev_fp1.size(); i = i+2) rout1.push_back(bt_xor(rev_fp1[i],rev_fp1[i+1]));
    for(int i=0; i+1<rev_fp2.size(); i = i+2) rout2.push_back(bt_xor(rev_fp2[i],rev_fp2[i+1]));

    vector<string> fout1, fout2;
    for(int i=0; i<rout1.size(); i++)
    {
        string k = "";
        for(int j=32; j<rout1[i].size(); j++)
        {
            k += rout1[i][j];
        }
        fout1.push_back(k);
    }
    for(int i=0; i<rout2.size(); i++)
    {
        string k = "";
        for(int j=32; j<rout2[i].size(); j++)
        {
            k += rout2[i][j];
        }
        fout2.push_back(k);
    }

    fstream in_sbox_xor1, in_sbox_xor2, fiout1, fiout2, eout1, eout2;
    in_sbox_xor1.open("sbox_in_xor1.txt",ios::trunc | ios::out | ios::in);
    in_sbox_xor2.open("sbox_in_xor2.txt",ios::trunc | ios::out | ios::in);
    fiout1.open("fiout1.txt",ios::trunc | ios::out | ios::in);
    fiout2.open("fiout2.txt",ios::trunc | ios::out | ios::in);
    eout1.open("expansion1.txt",ios::trunc | ios::out | ios::in);
    eout2.open("expansion2.txt",ios::trunc | ios::out | ios::in);

    for(int i=0; i<in_sbox1.size(); i++)
    in_sbox_xor1 << in_sbox1[i] << endl;
    in_sbox_xor1.close();
    for(int i=0; i<in_sbox2.size(); i++)
    in_sbox_xor2 << in_sbox2[i] << endl;
    in_sbox_xor2.close();

    for(int i=0; i<r5_1.size(); i++)
    eout1 << r5_1[i] << endl;
    eout1.close();
    for(int i=0; i<r5_2.size(); i++)
    eout2 << r5_2[i] << endl;
    eout2.close();

    for(int i=0; i<fout1.size(); i++)
    fiout1 << fout1[i] << endl;
    fiout1.close();
    for(int i=0; i<fout2.size(); i++)
    fiout2 << fout2[i] << endl;
    fiout2.close();

    system("python3 key_generator.py");

}

int main(){

    srand(time(0));
    int no_plaintext = 7000;
    generate_plain_cipher(no_plaintext, charac1);
    generate_plain_cipher(no_plaintext, charac2);
    break_6_round_des(no_plaintext);

    return 0;

}