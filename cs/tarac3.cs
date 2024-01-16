Tare Man, [1/16/24 9:25 AM]
using System;

class Program
{
    static void Main()
    {
        int[] comArray = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

        int oddCount = 0;
        int evenSum = 0;

        foreach (var num in comArray)
        {
            if (num % 2 != 0)
            {
                oddCount++;
            }
            else
            {
                evenSum += num;
            }
        }

        var evenFact = Factorial(evenSum);

        Console.WriteLine($"Number of all odd numbers in the array: {oddCount}");
        Console.WriteLine($"Factorial of the sum of even numbers in hexadecimal: {evenFact.ToString("X")}");
    }

    static int Factorial(int n)
    {
        if (n == 0 || n == 1)
            return 1;
        else
            return n * Factorial(n - 1);
    }
}
