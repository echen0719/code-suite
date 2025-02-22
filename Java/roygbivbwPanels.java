import javax.swing.*;
import java.awt.*;

public class roygbivbwPanels {
    public static void main(String[] args) {
        JFrame frame = new JFrame("ROYGBIV + BW Panels!");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(600, 600);

		JPanel red = new JPanel();
		red.setBackground(new Color(255, 0, 0));
		red.setBounds(0, 0, 200, 200);

		JPanel orange = new JPanel();
		orange.setBackground(new Color(255, 165, 0));
		orange.setBounds(200, 0, 200, 200);

		JPanel yellow = new JPanel();
		yellow.setBackground(new Color(255, 255, 0));
		yellow.setBounds(400, 0, 200, 200);

		JPanel green = new JPanel();
		green.setBackground(new Color(0, 255, 0));
		green.setBounds(0, 200, 200, 200);

		JPanel blue = new JPanel();
		blue.setBackground(new Color(0, 0, 255));
		blue.setBounds(200, 200, 200, 200);

		JPanel indigo = new JPanel();
		indigo.setBackground(new Color(75, 0, 130));
		indigo.setBounds(400, 200, 200, 200);

		JPanel violet = new JPanel();
		violet.setBackground(new Color(238, 130, 238));
		violet.setBounds(0, 400, 200, 200);

		JPanel black = new JPanel();
		black.setBackground(new Color(0, 0, 0));
		black.setBounds(200, 400, 200, 200);

		JPanel white = new JPanel();
		white.setBackground(new Color(255, 255, 255));
		white.setBounds(400, 400, 200, 200);

		frame.add(red);
		frame.add(orange);
		frame.add(yellow);
		frame.add(green);
		frame.add(blue);
		frame.add(indigo);
		frame.add(violet);
		frame.add(black);
		frame.add(white);

		frame.setLayout(null);
		frame.setVisible(true);
    }
}