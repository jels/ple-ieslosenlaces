import java.awt.*;
import java.sql.*;

import javax.swing.JOptionPane;

public class ConexionBD {
	static Connection conexion = null;
	static Statement cursor = null;
	public static boolean conectar(String ip, String port,String bd,String user,String pass,Container contenedor){
		boolean b = false;
		try {
			//Cargamos el driver
			Class.forName("oracle.jdbc.driver.OracleDriver");
			//Conexión
			conexion = DriverManager.getConnection("jdbc:oracle:thin:@"+ip+":"+port+":"+bd, user, pass);
			//Creamos el cursor
			cursor = conexion.createStatement();
			b = true;
		}
		catch (ClassNotFoundException e1){
			JOptionPane.showMessageDialog(contenedor, "Error al cargar el driver OJDBC.", "ERROR", JOptionPane.ERROR_MESSAGE);
			//e1.printStackTrace();
		} 
		catch (SQLException e2){
			JOptionPane.showMessageDialog(contenedor, "Error en la conexión.", "ERROR", JOptionPane.ERROR_MESSAGE);
			//e2.printStackTrace();
		}
		return b;
	}
	public static boolean desconectar(Container contenedor){
		boolean b = false;
		try {
			cursor.close();
			conexion.close();
			b = true;
		} catch (SQLException e1){
			JOptionPane.showMessageDialog(contenedor, "Error en la desconexión.", "ERROR", JOptionPane.ERROR_MESSAGE);
			//e1.printStackTrace();
		}
		return b;
	}
	public static ResultSet ejecutar(String sentencia,Container contenedor){
		ResultSet resultados1 = null;
		try {
			//Ejecutamos la sentencia y recogemos los resultados
			resultados1 = cursor.executeQuery(sentencia);
		} 
		catch (SQLException e1) {
			JOptionPane.showMessageDialog(contenedor, "Error en la sentencia SQL.", "ERROR", JOptionPane.ERROR_MESSAGE);
			//e1.printStackTrace();
		}
		return resultados1;
	}
}
