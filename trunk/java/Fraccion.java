
public class Fraccion {
	// Atributos de la clase
	private Integer numerador;
	private Integer denominador;
	
	public Fraccion(Integer numerador, Integer denominador){
		this.numerador = numerador;
		this.denominador = denominador;
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
		Integer nuevoNumerador = this.numerador * otra.getDenominador();
		Integer nuevoDenominador = this.denominador * otra.getNumerador();
		return new Fraccion(nuevoNumerador + nuevoDenominador,
				this.denominador * otra.getDenominador());
	}
	
	public static void main(String[] args){
		Fraccion f1 = new Fraccion(5, 3);
		Fraccion f2 = new Fraccion(2, 8);
		System.out.println("Fraccion f1: "  + f1);
		System.out.println("Fraccion f2: "  + f2);
		System.out.println("Suma: " + f1.add(f2));
		
	}
}
