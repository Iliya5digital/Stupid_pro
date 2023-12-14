using System;
class MainClass
{

    public static void Main(string[] args)
    {
        Human oleg = new Human();
        Animal dog = new Animal();
        Phone iphoneX = new Phone();
        Computer macbookWindows = new Computer();

        oleg.maleOrfemale();
        int a = Convert.ToInt32(Console.ReadLine());
        string sex;
        sex = oleg.chooseSex(a);
        oleg.writeSex();
        Console.WriteLine(sex + " from main");
        Console.WriteLine(oleg.publichka);
        Console.WriteLine(oleg.getPrivate());
    }
}
class Human
{
    string sex = null;
    public string publichka = "asasa";
    private string priv = "das";
    public string getPrivate()
    {
        return priv;
    }
    public Human()
    {
        Console.WriteLine("Олег родился");
        intro();
    }
    void intro()
    {
        Console.WriteLine("Привет! Я - человек. Выбери мне имя, пол, возраст и научите ездить");
    }
    public void maleOrfemale()
    {
        Console.WriteLine("1 - male, 2 - female");
    }
    public string chooseSex (int decision){
        if (decision == 1) this.sex = "Male"; //this присваивает значение глобальной переменной класса
        if (decision == 2) this.sex = "Female";
        return sex;
    }
    public void writeSex()
    {
        Console.WriteLine(sex + "from object");
    }
}

class Animal
{
    public Animal()
    {
        Console.WriteLine("СОБАКА " + 12 + "лет!");
    }
}
class Phone
{
    public Phone()
    {
        Console.WriteLine("Apple Iphone");
    }
}
class Text
{

}
class Computer
{
    public Computer()
    {
        Console.WriteLine("Minecraft запустись");
    }
}