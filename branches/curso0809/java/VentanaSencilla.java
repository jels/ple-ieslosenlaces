import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;


public class VentanaSencilla extends JFrame {
	JButton bb = new JButton("Borrar");
	JButton bs = new JButton("Salir");
	JButton bc = new JButton("Modificar");
	JTextField t = new JTextField("Pulse el botón para salir");
	JTextField tc = new JTextField("Pulse el botón para salir");
	JLabel eti = new JLabel("Introduce texto");

	// clase para implementar acción de botón salir
	class  EventoBotonSalir implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent arg0) {
			// TODO Auto-generated method stub
			System.exit(0);
		}
	}
	
	class  EventoBotonBorrar implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent arg0) {
			// TODO Auto-generated method stub
			t.setText("");
		}
	}
	
	class  EventoBotonModificar implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent arg0) {
			// TODO Auto-generated method stub
			String texto = new String(""); 
			texto = t.getText();
			tc.setText(texto.toUpperCase());
		}
	}
	

	public VentanaSencilla(){
		// Título de la ventana
		super ("Ventana sencilla");
		setLayout( new FlowLayout());
		setSize(200, 300);
		bs.addActionListener(new EventoBotonSalir());
		bb.addActionListener(new EventoBotonBorrar());
		bc.addActionListener(new EventoBotonModificar());
		// objetos gráficos
		add(eti);
		add(bb);
		add(t);
		add(bc);
		add(tc);
		add(bs);
	}

	public static void main(String []arg){
		VentanaSencilla ventana = new VentanaSencilla();
		ventana.setVisible(true);
	}
}
