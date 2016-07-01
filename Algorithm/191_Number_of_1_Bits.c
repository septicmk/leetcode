int hammingWeight(uint32_t n) {
   int cnt = 0;
   do{
       cnt += (n&1);
       n >>= 1;
   }while(n!=0);
   return cnt;
}
