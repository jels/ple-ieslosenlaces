import java.sql.*;
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import layout.TableLayout;
import java.util.Vector;

//CLASE PRINCIPAL
public class Gui_SQL extends JFrame {
	//VARIABLES GLOBALES
	Container contenedor = getContentPane();
	JLabel eti1 = new JLabel("SERVIDOR:");
	JLabel eti2 = new JLabel("PUERTO:");
	JLabel eti3 = new JLabel("BD:");
	JLabel eti4 = new JLabel("USUARIO:");
	JLabel eti5 = new JLabel("PASSWORD:");
	JTextField texto1 = new JTextField("servidororacleg");
	JTextField texto2 = new JTextField("1521");
	JTextField texto3 = new JTextField("enlaces5");
	JTextField texto4 = new JTextField("dai5");
	JPasswordField password = new JPasswordField(10);
	JLabel titulo = new JLabel("Introduce una sentencia SQL: ");
	JButton b_conectar = new JButton("CONECTAR");
	JButton aplicar = new JButton("APLICAR");
	JButton limpiar = new JButton("LIMPIAR");
	JButton b_desconectar = new JButton("DESCONECTAR");
	JTextArea t_area = new JTextArea(10,35);	
	JTable tabla = new JTable();
	JScrollPane scroll = new JScrollPane();
	JLabel vacio = new JLabel("");
	//CONSTRUCTOR
	public Gui_SQL(){
		super("Cliente SQL-Oracle");
		setSize(800,500);
		contenedor.setBounds(100, 100, 300, 300);
		//filas 10,25,1,25,10,25,10,25,10,100,10,30,10,175,34
        double tam[][] =
            { {0.0625, 0.125, 0.0625, 0.09375, 0.0625, 0.09375, 0.0625, 0.125, 0.0625, 0.125, 0.0625, 0.0625},
        		{10,25,1,25,10,25,10,25,10,100,10,30,20,175,24}};
        contenedor.setLayout (new TableLayout(tam));
        contenedor.add (eti1, "1,1");
        contenedor.add (eti2, "3,1");
        contenedor.add (eti3, "5,1");
        contenedor.add (eti4, "7,1");
        contenedor.add (eti5, "9,1");
        contenedor.add (texto1, "1,3");
        contenedor.add (texto2, "3,3");
        contenedor.add (texto3, "5,3");
        contenedor.add (texto4, "7,3");
        contenedor.add (password, "9,3");
        contenedor.add(b_conectar,"4,5,6,5");
		b_conectar.addActionListener(new EventoBotonConectar());
		pack();
		setResizable(false);
		//validate();
		setVisible(true);
	}
	//ACCIONES DE LOS BOTONES
	class EventoBotonConectar implements ActionListener{
		public void actionPerformed(ActionEvent e){
			String ip = new String();
			String port = new String();
			String bd = new String();
			String user = new String();
			String pass = new String();
			ip = texto1.getText();
			port = texto2.getText();
			bd = texto3.getText();
			user = texto4.getText();
			pass = new String(password.getPassword());
			if (ConexionBD.conectar(ip,port,bd,user,pass,contenedor)){
				b_conectar.setText("¡¡ CONECTADO !!");
				contenedor.add(titulo, "1,7,3,7");
				contenedor.add(t_area, "1,9,10,9");
				contenedor.add(aplicar, "1,11,2,11");
				contenedor.add(limpiar, "4,11,5,11");
				contenedor.add(b_desconectar, "7,11,8,11");
				setVisible(true);
				aplicar.addActionListener(new EventoBotonAplicar());
				limpiar.addActionListener(new EventoBotonLimpiar());
				b_desconectar.addActionListener(new EventoBotonDesconectar());
			}
		}
	}
	class EventoBotonAplicar implements ActionListener{
		public void actionPerformed(ActionEvent e){
			Vector columnNames = new Vector();
			Vector vectorDatos = new Vector();
			String sentencia = t_area.getText();
			ResultSet resultados1 = ConexionBD.ejecutar(sentencia, contenedor);
			ResultSetMetaData resultados2;
			if (resultados1 != null){
				try {
					resultados2 = resultados1.getMetaData();
					//Mostramos los resultados
					for(int r=1; r<=resultados2.getColumnCount(); r++)
						columnNames.add(resultados2.getColumnName(r));
					while(resultados1.next()){
						Vector vectorAux = new Vector();
						for(int x=1; x <= resultados2.getColumnCount(); x++ ){
							vectorAux.add(resultados1.getString(x));
						}
						vectorDatos.add(vectorAux);
					}
				} catch (SQLException e1){
					JOptionPane.showMessageDialog(contenedor, "Error SQL.", "ERROR", JOptionPane.ERROR_MESSAGE);
					//e1.printStackTrace();
				}
				tabla = new JTable(vectorDatos, columnNames);
				scroll = new JScrollPane(tabla);
				contenedor.add(scroll, "1,13,10,13");
				pack();
				setVisible(true);
			}
		}
	}
	class EventoBotonLimpiar implements ActionListener{
		public void actionPerformed(ActionEvent e){
			t_area.setText("");
			contenedor.remove(scroll);
			contenedor.validate();
			//pack();
			setVisible(true);
		}
	}
	class EventoBotonDesconectar implements ActionListener{
		public void actionPerformed(ActionEvent e){ 
			if (ConexionBD.desconectar(contenedor))
				b_conectar.setText("CONECTAR");
				//contenedor.validate();
		}
	}
	//Método PRINCIPAL
	public static void main(String[] args) {
		Gui_SQL ventana = new Gui_SQL();
	}
}
