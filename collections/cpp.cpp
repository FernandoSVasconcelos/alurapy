using namespace std;
int* reverseArray(int *arr, int len){  
    int i, temp;
    int originalLen = len -1;
    int *arr2 = arr;
    for(i=0;i<len -1;i++){
       temp = arr[originalLen];
       arr2[i] = temp;
       originalLen -= 1;
    }
    return arr2;
}     