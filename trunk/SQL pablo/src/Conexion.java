import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Vector;

import javax.swing.*;


public class Conexion {
	static String usuario = "";
	static String password = "";
	static String servidor = "";
	static Connection conexion;
	public static int conectar(){
		//recoger los datos del usuario
		servidor = Interfaz.tFieldServidor.getText();
		usuario = Interfaz.tFieldUsuario.getText();
		password = String.valueOf(Interfaz.tFieldPassword.getPassword());
		
		//Crear conexion y conectar
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");//intenta leer el driver para conectar a la bd
			conexion = DriverManager.getConnection("jdbc:oracle:thin:@"+servidor+":1521:ENLACES5", usuario, password);
			Interfaz.tFieldPassword.setText("");
			
			//Cambio de ventana
			return 0; // todo bien
			
		} catch (ClassNotFoundException e1) {
			// Si no conseguimos cargar el driver
			return 1; // error de driver 
		} catch (SQLException e1) {
			// Si no consigue crear la conexion
			return 2; // error de conexion
		}
	}
	public static int desconectar(){
		try {
			conexion.close();
			return 0;
		} catch (SQLException e) {
			return 1;
		}
	}
	public static ResultSet consultaResultSet() throws SQLException{
		String consulta = Interfaz.tFieldConsulta.getText(); //captura la cadena de la consulta
		Statement sentencia = conexion.createStatement(); //crea un objeto sentencia
		ResultSet resultados = sentencia.executeQuery(consulta); //ejecuta la sentencia y almacena el resultado
		return resultados;
	}
}