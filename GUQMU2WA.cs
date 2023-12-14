using System;
class HelloWorld
{
    public static void Main(string[] args)
    {
        string Name = Console.ReadLine();
        string Surname = Console.ReadLine();
        string Patronymic = Console.ReadLine();
        int age = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Name: " + Name + " Surname: " + Surname + " Patronymic: " + Patronymic);
        Console.WriteLine("Age: " + age);
    }
}
