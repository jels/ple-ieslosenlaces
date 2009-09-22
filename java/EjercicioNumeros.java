import java.util.ArrayList;
import java.util.Scanner;


public class EjercicioNumeros {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner entrada = new Scanner(System.in);
		entrada.useDelimiter("\n");
		ArrayList<Integer> lista = new ArrayList<Integer>();
		
		String numero = new String();
		System.out.println("Escribe numero: ");
		numero = entrada.next().trim();
		Integer num;
		
		while ( ! numero.equals("") ){
			lista.add(new Integer(numero));
			System.out.println("Escribe numero");
			numero = entrada.next().trim();
		}
		// Cálculo de total, mayor y menor
		int total = lista.get(0);
		int menor = total;
		int mayor = total;

		for (int i=1; i< lista.size(); i++){
			num = lista.get(i);
			total += num;
			if (num > mayor) mayor = num;
			if (num < menor) menor = num;
		}
		// Mostar datos:
		System.out.println("Números introducidos");
		for (Integer i: lista) System.out.print(i+",");
		System.out.println();
		System.out.printf("Mayor: %d\nMenor: %d\nTotal: %d\nMedia: %.2f",
				mayor, menor, total, total/(float)lista.size());		
	}

}






