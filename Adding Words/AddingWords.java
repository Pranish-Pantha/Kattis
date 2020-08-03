import java.util.*;
public class AddingWords 
{
public static List<Integer> listNum;
public static List<String> listStr;
    public static void main(String[] args) 
    {
      Scanner in = new Scanner(System.in);
      listNum = new ArrayList<Integer>();
      listStr = new ArrayList<String>();
      while(in.hasNext())
         {
            String temp = in.nextLine();
            if(temp.substring(0, 1).equals("d"))
               {
                  define(temp.substring(4, temp.indexOf(" ", 4)), Integer.parseInt((temp.substring(temp.indexOf(" ", 4)+1))));
               }
            else if(temp.substring(0, 2).equals("ca"))
               {
                  temp = temp.substring(5);
                  String[] tempArr = temp.split(" ");
                  int number = operation(tempArr);
                     if(number == -1001 || !(listNum.contains(number)))
                        {
                           System.out.println(temp + " unknown");
                        }
                     else
                        {
                           int index = listNum.indexOf(number);
                           System.out.println(temp + " " + listStr.get(index));
                        }
               }
            else if(temp.substring(0, 2).equals("cl"))
               {
                  clear();
               }
         }
      
    }
    public static void clear()
      {
         while(listStr.size()>0)
            {
               listStr.remove(0);
            }
          while(listNum.size()>0)
            {
               listNum.remove(0);
            }
      }
    public static void define(String input, int num)
    {
      if(listStr.contains(input))
         {
            int temp = listStr.indexOf(input);
            listNum.set(temp, num);
         }
      else{
      listNum.add(num);
      listStr.add(input);
      }
    }
    public static int operation(String[] arr)
    {
      int i = 0;
      int temp1 = -1001;
      int temp2 = -1001;
      int opera = -1001;
      int sum = -1001;
      while(!(arr[i].equals("=")))
         {
            if(arr[i].equals("+"))
               {
                  opera = 1;
               }
            else if(arr[i].equals("-"))
               {
                  opera = 2;
               }
            else if(listStr.contains(arr[i]))
               {
                  if(temp1 == -1001)
                     {
                     temp1 = listNum.get(listStr.indexOf(arr[i]));
                     sum = temp1;
                     }
                  else
                     {
                        temp2 = listNum.get(listStr.indexOf(arr[i]));
                        if(opera == 1)
                           {
                              sum += temp2;
                           }
                         else
                           {
                              sum -= temp2;
                           }
                        temp2 = -1;
                     }
               }
           else
            {
               return -1001;
            }
           i++;
         }
        return sum;
    }
}
       
