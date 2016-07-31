#include <stdio.h>
#include <stdbool.h>

int w[100][100];


bool searchMatrix(int matrix[100][100], int matrixRowSize, int matrixColSize, int target) {

   int i = 0, j = matrixColSize-1, l, r, mid;
   while(i<matrixRowSize && j >= 0){
       if(i == matrixRowSize-1 && j == 0) if (matrix[i][j] == target ) return true;
       else return false;
       //printf("%d %d\n",i,j);
       l = 0; r = j; mid = (l+r) >> 1;
       if(matrix[i][l] > target) return false;
       while(r > l){
            //printf("# %d %d\n",l,r);
            if(matrix[i][mid] <= target) l = mid;
            else r = mid-1;
            mid = (l+r+1)>>1;
       }
       //printf("# %d %d\n",l,r);
       if(matrix[i][mid] == target) return true;
       else j = mid;

       //printf("%d %d\n",i,j);
       l = i; r = matrixRowSize-1; mid = (l+r) >> 1;
       if(matrix[r][j] < target) return false;
       while(r > l){
            //printf("# %d %d\n",l,r);
           if(matrix[mid][j] >= target) r = mid;
           else l = mid+1;
           mid = (l+r)>>1;
       }

            //printf("# %d %d\n",l,r);
       if(matrix[mid][j] == target) return true;
       else i = mid;
   }
   return false;
}

int main(){
    int n,m;
    int t;
    scanf("%d%d",&n,&m);
    for(int i = 0 ; i < n ; i ++){
        for (int j = 0 ; j < m; j ++){
            scanf("%d",&w[i][j]);
        }
    }
    scanf("%d",&t);
    if(searchMatrix(w,n,m,t)) printf("True");
    else printf("False");
    return 0;
}
