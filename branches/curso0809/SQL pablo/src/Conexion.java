/* @author PABLO MARTIN
 * @version 1.0
 */

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Vector;

import javax.swing.*;


public class Conexion {
	private Connection conexion;
	private String usuario;
	private String password;
	private String servidor;
	private String puerto;
	private String bd;
	
	//@return Devuelve 0 si todo es correcto, 1 si hay error de driver, o 2 si hay error de conexion
	//@throws Lanza 2 posibles excepciones, ClassNotFoundException si no carga el driver, SQLException si hay error en los datos
	public int conectar(){	
		//Crear conexion y conectar
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");//intenta leer el driver para conectar a la bd
			conexion = DriverManager.getConnection("jdbc:oracle:thin:@"+servidor+":"+puerto+":"+bd, usuario, password);
			Interfaz.tFieldPassword.setText("");
			//Cambio de ventana
			return 0;
		} catch (ClassNotFoundException e1) {
			// Si no conseguimos cargar el driver
			return 1; // error de driver 
		} catch (SQLException e1) {
			// Si no consigue crear la conexion
			return 2; // error de conexion
		}
	}
	//Getters y Setters
	public String getBd() {
		return bd;
	}
	public String getPuerto() {
		return puerto;
	}
	public void setPuerto(String puerto) {
		this.puerto = puerto;
	}
	public void setBd(String bd) {
		this.bd = bd;
	}
	public Connection getConexion() {
		return conexion;
	}
	public void setConexion(Connection conexion) {
		this.conexion = conexion;
	}
	public String getUsuario() {
		return usuario;
	}
	public void setUsuario(String usuario) {
		this.usuario = usuario;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	public String getServidor() {
		return servidor;
	}
	public void setServidor(String servidor) {
		this.servidor = servidor;
	}
	//@return Devuelve 0 si ha podido desconectar del servidor, y 1 si no lo ha conseguido
	//@throws Lanza 1 excepcion SQLException si no ha conseguido desconectar
	public int desconectar(){
		try {
			conexion.close();
			return 0;
		} catch (SQLException e) {
			return 1;
		}
	}
	//@return devuelve un objeto ResultSet a la interfaz con los datos de la consulta
	//@throws Lanza 1 excepcion para ser tratada por la interfaz si no ha conseguido ejecutar la sentencia SQLException
	public ResultSet consultaResultSet() throws SQLException{
		String consulta = Interfaz.tFieldConsulta.getText(); //captura la cadena de la consulta
		Statement sentencia = conexion.createStatement(); //crea un objeto sentencia
		ResultSet resultados = sentencia.executeQuery(consulta); //ejecuta la sentencia y almacena el resultado
		return resultados;
	}
}