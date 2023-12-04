#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

template <typename T>
void print_vector(T arr[], int n)
{
    std::cout << "(";
    for (int i{}; i < n; i++)
    {
        if (i == n - 1)
            std::cout << arr[i] << ")\n";
        else 
            std::cout << arr[i] << ", ";
    }
}

int get_length(int value) {
   if (value == 0) 
      return 1;
      
   int digits = 0;
   while (value != 0) {
      digits++;
      value /= 10;
   }
   return digits;
}

int max_length(int* numbers, int numbersSize) {
   int maxDigits = 0;
   for (int i = 0; i < numbersSize; i++) {
      int digitCount = get_length(numbers[i]);
      if (digitCount > maxDigits) {
         maxDigits = digitCount;
      }
   }
   return maxDigits;
}
   
void radix_sort(int* numbers, int numbersSize) {
   std::vector<std::vector<int>*> buckets;
   for (int i = 0; i < 10; i++) {
      std::vector<int>* bucket = new std::vector<int>();
      buckets.push_back(bucket);
   }
      
   int copyBackIndex = 0;
      
   int maxDigits = max_length(numbers, numbersSize);
      
   int pow10 = 1;
   for (int digitIndex = 0; digitIndex < maxDigits; digitIndex++) {
      for (int i = 0; i < numbersSize; i++) {
         int num = numbers[i];
         int bucketIndex = (abs(num) / pow10) % 10;
         buckets[bucketIndex]->push_back(num);
      }
         
      copyBackIndex = 0;
      for (int i = 0; i < 10; i++) {
         std::vector<int>& bucket = *buckets[i];
         for (int j = 0; j < bucket.size(); j++) {
            numbers[copyBackIndex] = bucket[j];
            copyBackIndex++;
         }
         bucket.clear();
      }
      
      pow10 *= 10;
   }
      
   std::vector<int> nonNegatives;
   for (int i = 0; i < numbersSize; i++) 
   {
      int num = numbers[i];
      nonNegatives.push_back(num);
   }
      
   copyBackIndex = 0;
   for (int i = 0; i < nonNegatives.size(); i++) {
      numbers[copyBackIndex] = nonNegatives[i];
      copyBackIndex++;
   }
   
   for (int i = 0; i < 10; i++) {
      delete buckets[i];
   }
}

int main()
{
    int a[] = {5,4,3,2,1};
    std::cout << "Input: "; print_vector(a, 5); std::cout << '\n';
    radix_sort(a, 5);
    std::cout << "Output: "; print_vector(a, 5); std::cout << '\n';
}