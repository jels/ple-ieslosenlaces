import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;


public class TablaMulti extends JFrame {
	private JLabel titulo = new JLabel("Tabla multiplicar");
	private JButton bs, bt;
	private JTextField num = new JTextField("Número");
	
	class  EventoBotonSalir implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent arg0) {
			// TODO Auto-generated method stub
			System.exit(0);
		}
	}
	class  EventoBotonTabla implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent arg0) {
			// TODO Auto-generated method stub
			System.exit(0);
		}
	}
	public TablaMulti(){
		super("Tabla multiplicar");
		setLayout(new FlowLayout());
		add(titulo);
		add(num);
		bt = new JButton("Tabla");
		bs.addActionListener(new EventoBotonTabla());
		add(bt);
		
		
		bs = new JButton("Salir");
		bs.addActionListener(new EventoBotonSalir());
		add(bs);
		
		
		
		
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
