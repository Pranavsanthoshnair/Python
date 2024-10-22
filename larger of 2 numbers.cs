using System;
using System.IO;
using System.Text;

namespace larger of 2 numbers
{
   public class main_class
   {
      static System.Random random_generator = new System.Random();
      public static void Main(string[] args)
      {
         string raptor_prompt_variable_zzyz;
         ?? num1;
         ?? num2;
      
         raptor_prompt_variable_zzyz ="Enter first number";
         Console.WriteLine(raptor_prompt_variable_zzyz);
         num1= Double.Parse(Console.ReadLine());
         raptor_prompt_variable_zzyz ="Enter second number";
         Console.WriteLine(raptor_prompt_variable_zzyz);
         num2= Double.Parse(Console.ReadLine());
         if (num1>num2)
         {
            Console.WriteLine("Biggest number is "+(num1));
         }
         else
         {
            if (num2>num1)
            {
               Console.WriteLine("Biggest numer is"+(num2));
            }
            else
            {
               Console.WriteLine("both are equal");
            }
         }
      }
   }
}
