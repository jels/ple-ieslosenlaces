
# Ejercicios Jython #

Traduce a Jython los siguientes ejemplos en Java
## Conversión temperatura ##
```
import java.util.Scanner; 
 
public class TempConv { 
    public static void main(String[] args) { 
        Double fahr; 
        Double cel; 
        Scanner in; 
 
        in = new Scanner(System.in); 
        System.out.println("Enter the temperature in F: "); 
        fahr = in.nextDouble(); 
 
        cel = (fahr - 32) * 5.0/9.0; 
        System.out.println("The temperature in C is: " + cel); 
 
        System.exit(0); 
    } 
}
```

## Conversión temperatura swing ##
```
import javax.swing.*; 
 
public class TempConvGUI { 
 
    public static void main(String[] args) { 
        String fahrString; 
        Double fahr, cel; 
 
        fahrString = JOptionPane.showInputDialog("Enter the temperature in F"); 
        fahr = new Double(fahrString); 
        cel = (fahr - 32) * 5.0/9.0; 
 
        JOptionPane.showMessageDialog(null,"The temperature in C is, " + cel); 
    }  
}
```

## Histograma ##
```
import java.util.Scanner; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.IOException; 
 
public class Histo { 
 
    public static void main(String[] args) { 
        Scanner data = null; 
        ArrayList<Integer> count; 
        Integer idx; 
 
        try { 
                data = new Scanner(new File("test.dat")); 
        } 
        catch ( IOException e) { 
            System.out.println("Sorry but I was unable to open your data file"); 
            e.printStackTrace(); 
           System.exit(0); 
        } 
 
        count = new ArrayList<Integer>(10); 
        for (Integer i =0; i<10;i++) { 
            count.add(i,0); 
        } 
 
        while(data.hasNextInt()) { 
            idx = data.nextInt(); 
            count.set(idx,count.get(idx)+1); 
        } 
 
        idx = 0; 
        for(Integer i : count) { 
            System.out.println(idx + " occured " + i + " times."); 
            idx++; 
        } 
    } 
}
```


## Histograma con Array ##
```
import java.util.Scanner; 
import java.io.File; 
import java.io.IOException; 
 
public class HistoArray { 
    public static void main(String[] args) { 
        Scanner data = null; 
        Integer[] count = {0,0,0,0,0,0,0,0,0,0}; 
        Integer idx; 
 
 
 
        try { 
                data = new Scanner(new File("test.dat")); 
        } 
        catch ( IOException e) { 
           System.out.println("Sorry but I was unable to open your data file"); 
            e.printStackTrace(); 
            System.exit(0); 
        } 
 
        while(data.hasNextInt()) { 
           idx = data.nextInt(); 
            count[idx] = count[idx] + 1; 
        } 
 
       idx = 0; 
        for(Integer i : count) { 
            System.out.println(idx + " occured " + i + " times."); 
           idx++; 
        } 
    } 
}
```