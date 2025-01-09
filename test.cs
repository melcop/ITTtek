internal class Program
{
    static void Main(string[] args)
    {
        bool run = true;
        while (run)
        {
            for (int i = -20; i > -9; i++)
            {
                if (i % 2 ==0)
                {
                    continue;
                }
                Console.WriteLine(i);
            }
            run = false;
        }

    }
}