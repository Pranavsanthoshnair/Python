#include <iostream>
#include <string>

using namespace std;
int main()
{
   string raptor_prompt_variable_zzyz;
   ?? num1;
   ?? num2;

   raptor_prompt_variable_zzyz ="Enter first number";
   cout << raptor_prompt_variable_zzyz << endl;
   cin >> num1;
   raptor_prompt_variable_zzyz ="Enter second number";
   cout << raptor_prompt_variable_zzyz << endl;
   cin >> num2;
   if (num1>num2)
   {
      cout << "Biggest number is "+(num1) << endl;   }
   else
   {
      if (num2>num1)
      {
         cout << "Biggest numer is"+(num2) << endl;      }
      else
      {
         cout << "both are equal" << endl;      }
   }

   return 0;
}
