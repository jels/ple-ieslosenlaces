import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.util.Vector;

import javax.swing.*;

import layout.TableLayout;

public class Interfaz extends JFrame{
	//Declaracion de variables para la interfaz y layouts
	Container contenedor = getContentPane(); //Crea contenedor
	/*JPanel panelConsulta = new JPanel(); //crea 
	JPanel panelBotones = new JPanel();
	JPanel panelResultado = new JPanel();*/
	JTable tabla = new JTable(); //crea una tabla para mostrar resultados
	JScrollPane scrollPane = new JScrollPane(); //crea un scroll para insertar dentro la tabla
	GridLayout layoutConexion = new GridLayout(0,2); //Layout para la ventana de conexion
	JLabel labelServidor = new JLabel("Servidor"); //Label
	static JTextField tFieldServidor = new JTextField("172.30.6.190"); //Espacio para escribir el servidor/ip
	JLabel labelUsuario = new JLabel("Usuario"); //Label
	static JTextField tFieldUsuario = new JTextField("dai2"); //Espacio para escribir el usuario
	JLabel labelPassword = new JLabel("Contraseña"); //Label
	static JPasswordField tFieldPassword = new JPasswordField(""); //Espacio para escribir el password
	JButton botonConectar = new JButton("Conectar"); //Boton para conectar
	JButton botonLimpiar = new JButton("Limpiar datos"); //Boton para limpiar los formularios d la ventana de conexion
	JButton botonSalir = new JButton("Salir"); //Boton para salir
	JLabel labelConsulta = new JLabel("Escriba su consulta SQL"); //label
	static JTextArea tFieldConsulta = new JTextArea("Escriba su consulta SQL"); //Area de texto para escribir la consulta SQL
	JButton botonConsulta = new JButton("Lanzar consulta"); //Boton para Lanzar la consulta
	JButton botonLimpiar2 = new JButton("Limpiar datos"); //Boton para limpiar datos de la ventana de consulta
	JButton botonDesconectar = new JButton("Desconectar"); //Boton para desconectar del servidor
	TableLayout layoutConsultaTabla; //Layout para la ventana de consulta
	
	//Preparacion de ventanas
	public void winConexion(){
		//Crea la ventana d conexion para la primera vez que arranca el programa
		//Añade los elementos a mostrar y hace que la ventana sea de tamaño fijo
		contenedor.add(labelServidor);
		contenedor.add(tFieldServidor);
		contenedor.add(labelUsuario);
		contenedor.add(tFieldUsuario);
		contenedor.add(labelPassword);
		contenedor.add(tFieldPassword);
		contenedor.add(botonConectar);
		contenedor.add(botonLimpiar);
		contenedor.add(botonSalir);
		contenedor.validate();
		pack();
	}
	public void conexionAconsulta(){
		//Cambio de la ventana de conexion a la ventana de consulta
		//Quita lo de conexion, permite redimensionar la ventana, pone nuevo layout y añade los elementos
		contenedor.invalidate();
		contenedor.remove(labelServidor);
		contenedor.remove(tFieldServidor);
		contenedor.remove(labelUsuario);
		contenedor.remove(tFieldUsuario);
		contenedor.remove(labelPassword);
		contenedor.remove(tFieldPassword);
		contenedor.remove(botonConectar);
		contenedor.remove(botonLimpiar);
		contenedor.remove(botonSalir);
		setResizable(true);
		contenedor.setSize(1000, 600);
		double sizes [][] = {{0.25,0.25,0.25,0.25/*, TableLayout.FILL*/}, {150,50,/*250, */TableLayout.FILL}};
		layoutConsultaTabla = new TableLayout(sizes);
		contenedor.setLayout(layoutConsultaTabla);
		contenedor.add(tFieldConsulta,"0,0,3,0");
		contenedor.add(botonConsulta,"0,1");
		contenedor.add(botonLimpiar2,"1,1");
		contenedor.add(botonDesconectar,"2,1");
		contenedor.add(botonSalir,"3,1");
		contenedor.add(scrollPane,"0,2,3,2");
		contenedor.validate();
		pack();
	}
	public void consultaAconexion(){
		//Cambio de la ventana de consulta a la ventana de conexion
		//Quita lo de consulta, no permite redimensionar la ventana, pone nuevo layout y añade los elementos
		contenedor.invalidate();
		contenedor.remove(tFieldConsulta);
		contenedor.remove(botonConsulta);
		contenedor.remove(botonLimpiar2);
		contenedor.remove(botonDesconectar);
		contenedor.remove(botonSalir);
		contenedor.remove(scrollPane);
		contenedor.remove(scrollPane);
		contenedor.setLayout(layoutConexion);
		contenedor.add(labelServidor);
		contenedor.add(tFieldServidor);
		contenedor.add(labelUsuario);
		contenedor.add(tFieldUsuario);
		contenedor.add(labelPassword);
		contenedor.add(tFieldPassword);
		contenedor.add(botonConectar);
		contenedor.add(botonLimpiar);
		contenedor.add(botonSalir);
		contenedor.validate();
		pack();
		setResizable(false);
	}
	
	//Constructor
	public Interfaz(){
		//Caracteristicas del contenedor
		super ("Consultas SQL"); //Pone nombre a la ventana
		contenedor.setLayout(layoutConexion); //Aplica el layout que hemos definido al contenedor
		winConexion(); //Añadimos los elementos de la ventana de conexion
		setVisible(true); //Hace visible el JFrame
		setResizable(false);
		
		//Eventos de los botones
		class EventoBotonLimpiar implements ActionListener{
			public void actionPerformed(ActionEvent e) {
				//Borra las casillas escritas en la ventana de conexion
				tFieldServidor.setText("");
				tFieldUsuario.setText("");
				tFieldPassword.setText("");
			}
		}
		class EventoBotonLimpiar2 implements ActionListener{
			@Override
			public void actionPerformed(ActionEvent arg0) {
				//Borra la casilla para escribir la consulta y pone en blanco la tabla
				contenedor.invalidate();
				tFieldConsulta.setText("");
				tabla = new JTable();
				contenedor.remove(scrollPane);
				contenedor.validate();
				pack();
			}
		}
		class EventoBotonSalir implements ActionListener{
			//Sale completamente de la aplicacion sin cerrar conexion en caso de estar abierta
			@Override
			public void actionPerformed(ActionEvent arg0) {
				System.exit(0);
			}		
		}
		class EventoBotonConexion implements ActionListener{
			@Override
			public void actionPerformed(ActionEvent e) {
				if (Conexion.conectar() == 0){//LLama a conexion.conectar para conectar, si tiene exito
					JOptionPane.showMessageDialog(contenedor, "Conexion realizada con exito","EXITO", JOptionPane.PLAIN_MESSAGE); //Dialogo de exito
					conexionAconsulta(); //Cambia la ventana
				}
				else if (Conexion.conectar() == 1)JOptionPane.showMessageDialog(contenedor, "No ha sido posible encontrar el driver necesario","ERROR", JOptionPane.ERROR_MESSAGE); // Si no encuentra driver
				else if (Conexion.conectar() == 2)JOptionPane.showMessageDialog(contenedor, "Datos incorrectos \n No ha sido posible realizar la conexion con el servidor","ERROR", JOptionPane.ERROR_MESSAGE); //Si tiene datos incorrectos
			}
		}
		class EventoBotonDesconectar implements ActionListener{
			@Override
			public void actionPerformed(ActionEvent arg0) {
				if (Conexion.desconectar() == 0){//LLama a conexion.desconectar y si tiene exito
					JOptionPane.showMessageDialog(contenedor, "Desconectado del servidor","EXITO", JOptionPane.PLAIN_MESSAGE); //Mensaje d exito
					tFieldConsulta.setText("");//Borra la consulta escrita
					tabla = new JTable(); //Borra la tabla
					contenedor.remove(scrollPane); //Quita el scroll
					scrollPane = new JScrollPane(); //Resetea el scroll
					consultaAconexion(); //Cambia la ventana
				}
				if (Conexion.desconectar() == 1)JOptionPane.showMessageDialog(contenedor, "No ha sido posible desconectar del servidor","ERROR", JOptionPane.ERROR_MESSAGE); //Si falla la desconexion
			}
		}
		class EventoBotonConsulta implements ActionListener{
			@Override
			public void actionPerformed(ActionEvent arg0) {
				contenedor.invalidate();
				tabla = new JTable(); //Resetea la tabla por si quedara alguna de una consulta anterior
				contenedor.remove(scrollPane); //Quita el scroll de la pantalla para asegurar que no quedan restos
				try {
					ResultSet resultados = Conexion.consultaResultSet(); //LLama a la funcion que le devuelve un resultset con lo que ha devuelto la base de datos
					ResultSetMetaData resultadosMetadata = resultados.getMetaData(); //Extrae los metadatos de lo devuelo por la BD
					Vector columnNames = new Vector(); //crea e inicializa un array para los nombres de las columnas
					for(int c=1; c<=resultadosMetadata.getColumnCount(); c++){//Recorre el metadata cogiendo los nombres de las columnas
						columnNames.add(resultadosMetadata.getColumnName(c)); //añade a columnames el nombre de las columnas
					}
					Vector vectorDatos = new Vector(); //Crea un vector
					while(resultados.next()){ //mientras haya filas en los resultados
						Vector vectorAux = new Vector(); //crea un vector auxiliar
						for(int r=1; r <=resultadosMetadata.getColumnCount(); r++){ //Recorre las columnas
							vectorAux.add(resultados.getString(r)); //añade la string de los datos de las filas al vector auxiliar
						}
						vectorDatos.add(vectorAux); //añade el vector auxiliar al vector principal
					}
					tabla = new JTable(vectorDatos, columnNames); //Crea una JTable con los datos devueltos por la BD
					scrollPane = new JScrollPane(tabla); //Añade la tabla al scroll
					contenedor.add(scrollPane,"0,2,3,2"); //Coloca el scroll en su lugar en la ventana
					contenedor.validate();
					pack();
				} catch (SQLException e) {
					// Si no se ha podido crear la sentencia
					JOptionPane.showMessageDialog(contenedor, "No ha sido posible ejecutar la sentencia SQL. \n Revise la sintaxis \n"+e.toString(),"ERROR", JOptionPane.ERROR_MESSAGE); //Si no ha podido realizar la consulta...
				}
			}
		}
		
		//Listener de botones
		botonLimpiar.addActionListener(new EventoBotonLimpiar());
		botonSalir.addActionListener(new EventoBotonSalir());
		botonConectar.addActionListener(new EventoBotonConexion());
		botonLimpiar2.addActionListener(new EventoBotonLimpiar2());
		botonDesconectar.addActionListener(new EventoBotonDesconectar());
		botonConsulta.addActionListener(new EventoBotonConsulta());
	}
}