using System;

class Program
{
    static void Main()
    {
        // Initialize a jagged array
        int[][] jaggedArray = new int[6][];

        // Assign values for every array member
        for (int i = 0; i < jaggedArray.Length; i++)
        {
            jaggedArray[i] = new int[3];

            // Assign values to each inner array
            for (int j = 0; j < jaggedArray[i].Length; j++)
            {
                jaggedArray[i][j] = i * 10 + j; // Example assignment, you can replace this with your logic
            }
        }

        // Find the sum of all values in the array
        int sum = 0;
        foreach (var innerArray in jaggedArray)
        {
            foreach (var value in innerArray)
            {
                sum += value;
            }
        }

        // Display all members of the array
        Console.WriteLine("Array Members:");
        foreach (var innerArray in jaggedArray)
        {
            foreach (var value in innerArray)
            {
                Console.Write($"{value} ");
            }
            Console.WriteLine();
        }

        Console.WriteLine($"Sum of all values in the array: {sum}");
    }
}
