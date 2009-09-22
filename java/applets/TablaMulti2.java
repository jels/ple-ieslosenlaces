
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;


public class TablaMulti2 extends JApplet {
	
	private JTextField tnum = new JTextField("");
	private JLabel miTabla;
	
  public static void main(String[] args) {
    new TablaMulti2();
  }

  public TablaMulti2() {
    //super("Tabla de Multiplicar");
    Container content = getContentPane();
    //setSize(600, 800);
    Font font = new Font("Serif", Font.PLAIN, 30);
    content.setFont(font);
    String labelText = "Tabla de Multiplicar";
    
    JLabel titulo = new JLabel(labelText, JLabel.CENTER);
    //titulo.setBorder (BorderFactory.createTitledBorder("Titulo"));
    content.add(titulo, BorderLayout.NORTH);
    
    
    JLabel labelNumero =  new JLabel( "Número", JLabel.CENTER);
    //labelNumero.setBorder (BorderFactory.createTitledBorder("Numero"));
    content.add(labelNumero, BorderLayout.WEST);
    
    content.add(tnum, BorderLayout.CENTER);
    
    JButton bt = new JButton("OK");
    content.add(bt, BorderLayout.EAST);
    bt.addActionListener(new EventoBotonTabla());
           
    labelText = creaTabla();
    miTabla = new JLabel(labelText, JLabel.CENTER);
    
    //miTabla.setBorder (BorderFactory.createTitledBorder("Multi-line HTML"));
    content.add(miTabla, BorderLayout.SOUTH);
    //pack();
    setVisible(true);
    
  }
  public static String creaTabla(int num){
	  String res = new String("<html>");
	  for(int i=1; i<=10; i++){
		  String linea = new String("<br><pre>");
		  linea =  linea  + String.format("%2d x %2d = %3d", num, i, num*i);
		  //linea = linea + "</pre>";
		  res = res + linea;
	  }
	  //res = res + "<br>" + num + " x " + i + " = " +i*num;
	  return res;
  }
  public static String creaTabla(){
	  String res = new String("<html>");
	  for(int i=1; i<=10; i++){
		  String linea = new String("<br><pre>");
		  linea =  linea  + String.format("%2d x    = ", i );
		  res = res + linea;
	  }
	  //res = res + "<br>" + num + " x " + i + " = " +i*num;
	  return res;
  }
  
  class  EventoBotonTabla implements ActionListener{
		
		public void actionPerformed(ActionEvent arg0) {
			try {	
				Integer numero = Integer.parseInt(tnum.getText());
				miTabla.setText(creaTabla(numero));
			}
			catch (NumberFormatException e){
				;
				
			}
			
			}
		}
  
}

		