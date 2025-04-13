import javax.swing.*;
import java.awt.*;
import java.util.*;

public class roygbivbwPanels {
    public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		System.out.println("ROYGBIVBW Display Test?");
		System.out.print("To change color, you can shift by decimal (+/-): ");
		int chn = kb.nextInt();

        JFrame frame = new JFrame("ROYGBIV + BW Panels!");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(600, 600);

		JPanel red = new JPanel();
		red.setBackground(new Color(checkValue(255, chn), checkValue(0, chn), checkValue(0, chn)));
		red.setBounds(0, 0, 200, 200);

		JPanel orange = new JPanel();
		orange.setBackground(new Color(checkValue(255, chn), checkValue(165, chn), checkValue(0, chn)));
		orange.setBounds(200, 0, 200, 200);

		JPanel yellow = new JPanel();
		yellow.setBackground(new Color(checkValue(255, chn), checkValue(255, chn), checkValue(0, chn)));
		yellow.setBounds(400, 0, 200, 200);

		JPanel green = new JPanel();
		green.setBackground(new Color(checkValue(0, chn), checkValue(255, chn), checkValue(0, chn)));
		green.setBounds(0, 200, 200, 200);

		JPanel blue = new JPanel();
		blue.setBackground(new Color(checkValue(0, chn), checkValue(0, chn), checkValue(255, chn)));
		blue.setBounds(200, 200, 200, 200);

		JPanel indigo = new JPanel();
		indigo.setBackground(new Color(checkValue(75, chn), checkValue(0, chn), checkValue(130, chn)));
		indigo.setBounds(400, 200, 200, 200);

		JPanel violet = new JPanel();
		violet.setBackground(new Color(checkValue(238, chn), checkValue(130, chn), checkValue(238, chn)));
		violet.setBounds(0, 400, 200, 200);

		JPanel black = new JPanel();
		black.setBackground(new Color(checkValue(0, chn), checkValue(0, chn), checkValue(0, chn)));
		black.setBounds(200, 400, 200, 200);

		JPanel white = new JPanel();
		white.setBackground(new Color(checkValue(255, chn), checkValue(255, chn), checkValue(255, chn)));
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

    public static int checkValue(int inp, int chn) {
		inp += chn;
		if (inp > 255) {
			inp = 255;
		}
		else if (inp < 0) {
			inp = 0;
		}
		return inp;
    }
}