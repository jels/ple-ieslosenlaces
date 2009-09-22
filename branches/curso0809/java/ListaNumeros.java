import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

public class ListaNumeros {

	/**
	 * @param args
	 */
	
	public static void main(String[] args) {
		// Ejercicios con listas de números
		// 1. vector
		int [] vector = new int[10];
		Scanner entrada = new Scanner(System.in);
		
		for (int i=0; i<10; i++){
			vector[i] = entrada.nextInt();
		}
		
		for (int i=0; i<10; i++){
			System.out.println("Número " + (i+1) + ": " + vector[i]);
		}
		

		// 2. ArrayList
		ArrayList<Integer> lista = new ArrayList();
		for (int i=0; i<10; i++){
		lista.add(entrada.nextInt());
		}
		// recorrido con for
		for (int j: lista)
			System.out.println(j);
		// recorrido con iterador
		Iterator it = lista.iterator();
		while (it.hasNext())
			System.out.println(it.next());
	}

}
