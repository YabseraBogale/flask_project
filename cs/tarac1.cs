using System;
//fix
class Program
{
    static void Main()
    {
        int[] array1 = { 11, 4, 20, 9, 2, 8 };
        int[] array2 = { 12, 11, 4, 9, 2, 3, 10 };

        int sum1;
        string result1;
        bool inertial1 = isInertial(array1, out sum1, ref result1);

        Console.WriteLine("Array 1 Elements:");
        DisplayArray(array1);
        Console.WriteLine($"Result: {result1}, Sum: {sum1}");
        Console.WriteLine();

        int sum2;
        string result2;
        bool inertial2 = isInertial(array2, out sum2, ref result2);

        Console.WriteLine("Array 2 Elements:");
        DisplayArray(array2);
        Console.WriteLine($"Result: {result2}, Sum: {sum2}");
    }

    static bool isInertial(int[] a, out int sum, ref string res)
    {
        Array.Sort(a);

        int largestOdd = 0;
        int largestEven = 0;

        foreach (var num in a)
        {
            if (num % 2 == 1 && num > largestOdd)
            {
                largestOdd = num;
            }
            else if (num % 2 == 0 && num > largestEven)
            {
                largestEven = num;
            }
        }

        if (largestOdd == 0  largestEven == 0  largestEven != a[a.Length - 1])
        {
            sum = 0;
            res = "Not Inertial";
            return false;
        }

        sum = largestOdd + largestEven;
        res = "Inertial";
        return true;
    }

    static void DisplayArray(int[] array)
    {
        Console.Write("Array Elements: ");
        foreach (var element in array)
        {
            Console.Write($"{element} ");
        }
        Console.WriteLine();
    }
}
