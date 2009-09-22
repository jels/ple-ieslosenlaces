import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Vector;

import javax.swing.*;

public class InterfazBDDJava extends JFrame{
	Container contenedor = getContentPane();
	JLabel eti1 = new JLabel("Servidor+Puerto+BDD(0.0.0.0:0000:miBDD)");
	JTextField servidor = new JTextField("");
	JLabel eti2 = new JLabel("Usuario");
	JLabel eti3 = new JLabel("Password");
	JTextField usuario = new JTextField("");
	JPasswordField pass = new JPasswordField(10);
	JTextField p = new JTextField("Contraseña");
	JButton conectar = new JButton("Conectar");
	JButton lanzar = new JButton("Lanzar Consulta");
	JPanel panel1 = new JPanel();
	JPanel panel3 = new JPanel();
	JTextArea area = new JTextArea("");
	JButton descon = new JButton("Desconectar");
	static JPanel panel2 = new JPanel();
	static boolean conectado = false;
	JLabel consul = new JLabel("Introduzca consulta");
	JButton limpiar = new JButton("Limpiar");
	JScrollPane scroll = new JScrollPane();
	JTable tabla = new JTable();
	JPanel panel4 = new JPanel();
	JButton salir = new JButton("Salir");
	JLabel relleno = new JLabel();
	Dimension tam = new Dimension(800, 200);
	
	BDDJava bddjava;
	
	public static void main(String [] args){
		InterfazBDDJava i = new InterfazBDDJava();
	}
	
	public InterfazBDDJava(){
		//super("BDDJava");
		bddjava = new BDDJava();
		setSize(300, 400);
		contenedor.setLayout(new GridLayout(0, 1));
		panel1.setLayout(new GridLayout(0, 1));
		add(panel1);
		panel1.add(eti1);
		panel1.add(servidor);
		panel1.add(eti2);
		panel1.add(usuario);
		panel1.add(eti3);
		panel1.add(pass);
		panel1.add(conectar);
		conectar.addActionListener(new EventoBotonConectar());
		pack();
		setVisible(true);
	}
	
	class EventoBotonConectar implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			String user;
			String server;
			char[] password;
			String cadena = new String();
			if (! bddjava.conectado) {
			server = servidor.getText();
			user = usuario.getText();
			password =  pass.getPassword();
			cadena = new String(password);
			String error;
			//cadena = String.valueOf(password);
			/*
			System.out.println(server+":"+user+":"+cadena+":");
			for(int i= 0 ; i<password.length; i++)
				System.out.println(password[i]);
				*/
			error = bddjava.Conecta(server, user, cadena);
			//"jdbc:oracle:thin:@172.30.6.190:1521:enlaces5"
			if(error != ""){
				JOptionPane.showMessageDialog(contenedor, error, "Error", JOptionPane.ERROR_MESSAGE);
				System.exit(0);
			}
			else
				bddjava.conectado = true;
			pass.setText("");
			panel3.setLayout(new GridLayout(4, 4));
			//panel2.remove(area);
			//remove(panel2);
			//panel2 = new JPanel();
			add(panel2);
			add(panel3);
			panel2.setLayout(new GridLayout(0, 1));
			//area = new JTextArea("");
			panel2.add(area);
			contenedor.setMaximumSize(tam);
			panel3.add(lanzar);
			panel3.add(descon);
			panel3.add(limpiar);
			panel3.add(salir);
			panel3.add(relleno);
			panel3.add(relleno);
			panel3.add(relleno);
			panel3.add(relleno);
			salir.addActionListener(new EventoBotonSalir());
			limpiar.addActionListener(new EventoBotonLimpiar());
			lanzar.addActionListener(new EventoBotonLanzar());
			descon.addActionListener(new EventoBotonDesconectar());
			panel1.add(consul);
			panel1.remove(conectar);
			pack();
			
			
			}
		}
	}
	class EventoBotonLanzar implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent e){
			String consulta = new String();
			String error;
			panel4.setLayout(new GridLayout(1, 1));
			add(panel4);
			
			//tabla.removeAll();
			panel4.remove(scroll);
			consulta = area.getText();
			error = bddjava.SentenciaSQL(consulta);
			tabla = new JTable(bddjava.getDatos(), bddjava.getNombres());
			tabla.setEnabled(false);
			for(int i=1 ; i <= tabla.getRowCount() ; i+=2)
				tabla.addRowSelectionInterval(i, i);
			scroll = new JScrollPane(tabla);
			scroll.setPreferredSize(tam);
			panel4.add(scroll);
			//tabla.setFillsViewportHeight(true);
			//System.out.println(consulta);
			pack();
			if(error != "")
				JOptionPane.showMessageDialog(contenedor, error, "Error", JOptionPane.ERROR_MESSAGE);
			
			
		}
	}
	
	class EventoBotonLimpiar implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent e){
			area.setText("");
			//tabla.removeAll();
			panel4.remove(scroll);
			pack();
		}
	}
	
	class EventoBotonSalir implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent e){
			bddjava.Desconexion();
			System.exit(0);
		}
	}
	
	class EventoBotonDesconectar implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent e){
			String error;
			error = bddjava.Desconexion();
			panel1.add(conectar);
			bddjava.conectado = false;
			area.setText("");
			//panel2.remove(area);
			remove(panel2);
			remove(panel3);
			remove(panel4);
			//panel2 = null;
			panel1.remove(consul);
			//tabla.removeAll();
			panel4.remove(scroll);
			pack();
			if(error != "")
				JOptionPane.showMessageDialog(contenedor, error, "Error", JOptionPane.ERROR_MESSAGE);
		}
	}
}

