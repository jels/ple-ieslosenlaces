import java.sql.*;
import java.util.Vector;

public class BDDJava {
	Connection con = null;
	boolean conectado = false;
	private Vector datos = new Vector();
	private Vector nombres = new Vector();
	
	
	public Vector getDatos() {
		return datos;
	}
	public Vector getNombres() {
		return nombres;
	}
	public String Conecta(String server, String user, String pass){
		Connection conexion = null;
		Statement sentencia = null;
		ResultSet resultados = null;
		ResultSetMetaData res = null;
		try {
			//String password = pass.toString();
			//System.out.println(password);
			Class.forName("oracle.jdbc.driver.OracleDriver");
			conexion = DriverManager.getConnection("jdbc:oracle:thin:@"+server, user, pass);
			con = conexion;
			return "";
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			return e.toString();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			return e.toString();
		
		}
	}
	public String SentenciaSQL(String sentence){
		Statement sentencia = null;
		ResultSet resultados = null;
		ResultSetMetaData res;
		Vector vectorNombres = new Vector();
		Vector vectorDatos = new Vector();
		Vector total;
		
		try{
			sentencia = con.createStatement();
			resultados = sentencia.executeQuery(sentence);
			res = resultados.getMetaData();
			for(Integer h = 1 ; h <= res.getColumnCount() ; h++)
				vectorNombres.add(res.getColumnName(h));
			//System.out.println(res.getColumnName(1));
			while(resultados.next()){
				Vector vectorDatosAuxiliar = new Vector();
				for(int r = 1 ; r <= res.getColumnCount() ; r++){
					vectorDatosAuxiliar.add(resultados.getString(r));
					//System.out.println(resultados.getString(r));
				}
				vectorDatos.add(vectorDatosAuxiliar);
			}
			//sentencia.executeUpdate("Create table em (id number(2), nombre varchar(50))");
			//conexion.close();
			nombres = vectorNombres;
			datos = vectorDatos;
			return "";
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			return e.toString();
		}
	}
	
	public String Desconexion(){
		try {
			con.close();
			return "";
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			return e.toString();
		}
	}
}
