import java.util.ArrayList;
import java.util.Collections;


public class Fraccion extends Number implements Comparable<Fraccion> {
	// Atributos de la clase
	private Integer numerador;
	private Integer denominador;
	
	public Fraccion(Integer numerador, Integer denominador){
		this.numerador = numerador;
		this.denominador = denominador;
	}
	
	public Fraccion(Integer numerador){
		this.numerador = numerador;
		this.denominador = 1;
	}
	
	public String toString(){
		return numerador.toString() + "/" + denominador.toString();	
	}
	
	public Integer getNumerador() {
		return numerador;
	}

	public Integer getDenominador() {
		return denominador;
	}

	public Fraccion add(Fraccion otra){
		Integer nuevoNumerador = this.numerador * otra.getDenominador() 
			+ 	 this.denominador * otra.getNumerador();
		Integer nuevoDenominador = this.denominador * otra.getDenominador();
		Integer comun = mcd(nuevoNumerador, nuevoDenominador);
		
		return new Fraccion(
				nuevoNumerador/comun,
				nuevoDenominador/comun
				);
	}
	public static Integer mcd(Integer m, Integer n){
		while ( m % n != 0){
			Integer oldm = m;
			Integer oldn = n;
			m = oldn;
			n = oldm % oldn;
		}
		return n;
	}
	
	public Fraccion add(Integer n){
		return add(new Fraccion(n, 1));
		
	}
	public boolean equals(Fraccion otra){
		if (this.numerador == otra.getNumerador() &&
				this.denominador == otra.getDenominador())
			return true;
		else
			return false;
	}
	
	public static void ordenarFracciones(){
		Fraccion f1 = new Fraccion(21,4);
		Fraccion f2 = new Fraccion(17,4);
		Fraccion f3 = new Fraccion(1,4);
		
		ArrayList<Fraccion>lista = new ArrayList<Fraccion>();
		lista.add(f1);
		lista.add(f3);
		lista.add(f2);
		for (Fraccion f: lista)
			System.out.println(f);
		// ordenar
		Collections.sort(lista);
		
		for (Fraccion f: lista)
			System.out.println(f);
		
		
		
		
	}
	public static void main(String[] args){
		Integer n = 5;
		Fraccion f1 = new Fraccion(2, 4);
		Fraccion f2 = new Fraccion(2, 4);
		String nombre1 = new String("Pepe");
		String nombre2 = new String("Pepe");
		System.out.println("Fraccion f1: "  + f1);
		System.out.println("Fraccion f2: "  + f2);
		System.out.println("Suma: " + f1.add(f2));
		System.out.println("Suma: " + f1.add(1));
		if (f1.equals(f2))
			System.out.println( f1+ " " +  f2 +  " son iguales");
		else
			System.out.println( f1+ " y " +  f2 +  " NO  son iguales");
		System.out.println( 4.5 + f1.floatValue());
		
		ordenarFracciones();
	}

	@Override
	public double doubleValue() {
		return this.numerador.doubleValue() / 
			this.denominador.doubleValue();
	}

	@Override
	public float floatValue() {
		// TODO Auto-generated method stub
		return numerador.floatValue() / 
			denominador.floatValue();
	}

	@Override
	public int intValue() {
		// TODO Auto-generated method stub
		return numerador.intValue() / 
			denominador.intValue();
	}

	@Override
	public long longValue() {
		// TODO Auto-generated method stub
		return numerador.longValue() / 
			denominador.longValue();
	}

	@Override
	public int compareTo(Fraccion otra) {
		// devuelve -1, 0 ó 1
		Integer num1 = this.numerador * otra.getDenominador();
		Integer num2 = this.denominador * otra.getNumerador();
		return (num1 - num2) * -1;
	}
}
