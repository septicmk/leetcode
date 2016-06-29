#include <stdio.h>
void moveZeroes(int* nums, int numsSize) {
   int i,j=0;
   for(i = 0 ; i < numsSize; ++i){
       if(nums[i]) if(i != j ){
           int tmp = nums[i];
           nums[i] = nums[j];
           nums[j] = tmp;
           j++;
       }else{
           j++;
       }
   }
}

int main(){
    int x[6] = {0,0,3,0,5,6};
    moveZeroes(x, 6);
    int i;
    for (i = 0 ; i < 6 ; i ++)
        printf("%d ",x[i]);
    return 0;
}
