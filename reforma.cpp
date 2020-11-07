#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <iterator>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <math.h>
#include <stdio.h>
#include <exception>
#include <algorithm>
#include <functional>
#include <cctype>
#include <locale>

using namespace std;

bool contains(vector<int> arr, int val)
{
    int i;
    for(i = 0; i < arr.size(); i++)
    {
        if(arr[i] == val) return true;
    }
    return false;
}

int main()
{
    vector<int> VALS;
    VALS.push_back(0);
    int N, Q, q;
    scanf("%d %d", &N, &Q);
    getchar();

    for(q = 0; q < Q; q++)
    {
        int valor;
        scanf(" %d", &valor);
        if(valor <= N)
        {
            int qntVals = VALS.size(), i;
            for(i = 0; i < qntVals; i++)
            {
                int soma = VALS[i] + valor;
                if (soma <= N) VALS.push_back(soma);
            }
        }
    }

    if(contains(VALS, N)) printf("SIM\n");
    else printf("NAO\n");

    return 0;
}
