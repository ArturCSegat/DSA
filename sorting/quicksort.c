// Online C compiler to run C program online
#include <stdio.h>

void swap(int *x, int* y){
    int t = *x;
    *x = *y;
    *y = t;
}

void printArr(int *arr, int s){
    
    for (int i = 0; i<s; i++){
        printf("%d ", arr[i]);
    }
    
}

int partition(int *arr, int low, int high){
    
    int pivot = arr[high];
    
    int i = low;
    
    for (int j = low; j<high; j++){
        if (arr[j] < pivot){
            swap(&arr[j], &arr[i]);
            i++;
        }
    }
    
    swap(&arr[i], &arr[high]);
    return i;
    
}

void quickSort(int *arr, int low, int high){
    
    if (low<high){
        
        int pi = partition(arr, low, high);
        
        quickSort(arr, pi+1, high);
        quickSort(arr, low, pi-1);
        
    }
}




int main() {
      int array[10] = {10, 9 ,8, 1, 7 ,6, 5, 4, 3, 2};
      
      
     printf("Unsorted: \n");
     printArr(array, 10);
     quickSort(array, 0, 10);
     printf("\nSorted: \n");
     printArr(array, 10);

    return 0;
}
