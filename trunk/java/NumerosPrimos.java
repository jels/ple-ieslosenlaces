import java.util.Scanner;



public class NumerosPrimos {

	/**
	 * @param args
	 */
	public static boolean esPrimo(int n){
		// comprobar si i es primo
		for (int j=2; j<= Math.sqrt(n); j++){
			if (n % j == 0)
				return false;
		}
		return true;
	}
		
	public static void main(String[] args) {
		int i = 1, numero;
		Scanner entrada = new Scanner(System.in);
		
		System.out.println("Introduce un número: ");
		numero = entrada.nextInt();
		
		for (i=2;  i<= numero; i++){
					
			if (esPrimo(i))
				System.out.println(i);
		}
	}
	
	
}
