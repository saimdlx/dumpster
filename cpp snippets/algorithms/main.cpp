#include <iostream>
#include <utility>
#include <iterator>


void selectionSort();
void linearSearch();
int binarySearch();


int main(){
    selectionSort();
    linearSearch();
    std::cout << "Binary search target found at: " << binarySearch() << std::endl;
    return 0;
}

void selectionSort(){
    int arr[] = {1,3,7,5,8,6,3,7};
    int n = sizeof(arr) / sizeof(arr[0]);
    for (int i = 0 ; i < n - 1; i++){
        int min = i;
        for (int j = i + 1 ; j < n ; j++) {
            if (arr[j] < arr[min]){
                min = j;
            }
        }
        if (i != min){
            std::swap(arr[i], arr[min]);
        }
    }

    for (int x = 0 ; x < n ; x++){
        std::cout << arr[x] << " ";
    }
    std::cout << std::endl;
}

void linearSearch(){
    int arr[] = {1,5,2,6,9,8,7,0};
    int target = 8;
    for (int i = 0 ; i < sizeof(arr)/sizeof(arr[0]) ; i++){
        if (arr[i] == target){
            std::cout << "Target found at index: " << i << std::endl;
        }
    }
}

int binarySearch(){
    int arr[] = {1,3,5,7,9,11,13,15,17,19,21};
    int left = 0;
    int right = sizeof(arr)/sizeof(arr[0]);
    int mid = 0;
    int target = 17;
    while (left <= right){
        // fuck up: didn't reinit mid value after entering while loop, ran infinitely before i asked google.
        int mid = left + (right - left) / 2;
        if (arr[mid] == target){
            return mid;
        }
        if (arr[mid] < target){
            left = mid + 1;
        }
        else{
            right = mid - 1;
        }
    }
    return -1;
}