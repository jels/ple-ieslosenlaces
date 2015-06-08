
```
import java.util.Scanner;
import java.util.TreeMap;
import java.io.File;
import java.io.IOException;

/*
 * El programa cuenta el número de veces que aparece
 * una serie de enteros en un fichero.
 * La estructura del fichero (datos.txt) es de un número
 * por línea.
 * Utilizamos un TreeMap con clave entero y valor entero.
 */

public class EjemploTreeMap {
	public static void main(String[] args) {
		Scanner data = null;
		TreeMap <Integer, Integer> contador;
		Integer idx;
		try {
			data = new Scanner(new File("datos.txt"));
		}
		catch ( IOException e) {
			System.out.println("No se puede abrir el fichero");
			e.printStackTrace();
			System.exit(0);
		}
		contador = new TreeMap<Integer, Integer>();
		
		while(data.hasNextInt()) {
			idx = data.nextInt();
			if (contador.containsKey(idx))
				contador.put(idx, contador.get(idx)+1);
			else
				contador.put(idx, 1);
                }
		
        for(Integer i : contador.keySet()) {
                    System.out.println(i + " aparece " + contador.get(i) + " vez/veces.");
                }
	}
}
```