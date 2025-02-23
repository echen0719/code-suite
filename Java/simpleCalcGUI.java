import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class simpleCalcGUI {
	private static JFrame frame = new JFrame("Simple 4 Function Calculator");

	public static void main(String[] args) {
		swing();
		buttons();
		frame.setVisible(true);
		/* System.out.println(add(1, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7)); // 1 + 2.1 + 3.2 + 4.3 + 5.4 + 6.5 + 7.6 + 8.7 = 38.8
		System.out.println(subtract(10.9, 9.8, 8.7)); // 10.9 - 9.8 - 8.7 = -7.6
		System.out.println(multiply(1, 2, 3, 4, 5)); // 5! = 120
		System.out.println(divide(120, 5, 4, 3, 2, 1)); // 120 / 5! = 1 */
	}

	public static void buttons() {
		JButton ac = new JButton("AC");
		ac.setBounds(25, 25, 75, 75);
		ac.setBackground(new Color(92, 92, 95));
		ac.setForeground(Color.white);
		ac.setBorder(new RoundedBorder(10));
		frame.add(ac);

		JButton percent = new JButton("%");
		percent.setBounds(125, 25, 75, 75);
		percent.setBackground(new Color(92, 92, 95));
		percent.setForeground(Color.white);
		frame.add(percent);

		JButton square = new JButton("x²");
		square.setBounds(225, 25, 75, 75);
		square.setBackground(new Color(92, 92, 95));
		square.setForeground(Color.white);
		frame.add(square);

		JButton one = new JButton("1");
		one.setBounds(25, 325, 75, 75);
		one.setBackground(new Color(42, 42, 44));
		one.setForeground(Color.white);
		frame.add(one);

		JButton two = new JButton("2");
		two.setBounds(125, 325, 75, 75);
		two.setBackground(new Color(42, 42, 44));
		two.setForeground(Color.white);
		frame.add(two);

		JButton three = new JButton("3");
		three.setBounds(225, 325, 75, 75);
		three.setBackground(new Color(42, 42, 44));
		three.setForeground(Color.white);
		frame.add(three);

		JButton four = new JButton("4");
		four.setBounds(25, 225, 75, 75);
		four.setBackground(new Color(42, 42, 44));
		four.setForeground(Color.white);
		frame.add(four);

		JButton five = new JButton("5");
		five.setBounds(125, 225, 75, 75);
		five.setBackground(new Color(42, 42, 44));
		five.setForeground(Color.white);
		frame.add(five);

		JButton six = new JButton("6");
		six.setBounds(225, 225, 75, 75);
		six.setBackground(new Color(42, 42, 44));
		six.setForeground(Color.white);
		frame.add(six);

		JButton seven = new JButton("7");
		seven.setBounds(25, 125, 75, 75);
		seven.setBackground(new Color(42, 42, 44));
		seven.setForeground(Color.white);
		frame.add(seven);

		JButton eight = new JButton("8");
		eight.setBounds(125, 125, 75, 75);
		eight.setBackground(new Color(42, 42, 44));
		eight.setForeground(Color.white);
		frame.add(eight);

		JButton nine = new JButton("9");
		nine.setBounds(225, 125, 75, 75);
		nine.setBackground(new Color(42, 42, 44));
		nine.setForeground(Color.white);
		frame.add(nine);

		JButton zero = new JButton("0");
		zero.setBounds(25, 425, 75, 75);
		zero.setBackground(new Color(42, 42, 44));
		zero.setForeground(Color.white);
		frame.add(zero);

		JButton dot = new JButton(".");
		dot.setBounds(125, 425, 75, 75);
		dot.setBackground(new Color(42, 42, 44));
		dot.setForeground(Color.white);
		frame.add(dot);

		JButton divide = new JButton("/");
		divide.setBounds(325, 25, 75, 75);
		divide.setBackground(new Color(255, 159, 10));
		divide.setForeground(Color.white);
		frame.add(divide);

		JButton multiply = new JButton("×");
		multiply.setBounds(325, 125, 75, 75);
		multiply.setBackground(new Color(255, 159, 10));
		multiply.setForeground(Color.white);
		frame.add(multiply);

		JButton minus = new JButton("-");
		minus.setBounds(325, 225, 75, 75);
		minus.setBackground(new Color(255, 159, 10));
		minus.setForeground(Color.white);
		frame.add(minus);

		JButton plus = new JButton("+");
		plus.setBounds(325, 325, 75, 75);
		plus.setBackground(new Color(255, 159, 10));
		plus.setForeground(Color.white);
		frame.add(plus);

		JButton plusminus = new JButton("+/-");
		plusminus.setBounds(225, 425, 75, 75);
		plusminus.setBackground(new Color(92, 92, 95));
		plusminus.setForeground(Color.white);
		frame.add(plusminus);

		JButton equal = new JButton("=");
		equal.setBounds(325, 425, 75, 75);
		equal.setBackground(new Color(255, 159, 10));
		equal.setForeground(Color.white);
		frame.add(equal);
	}

	public static void swing() {
		frame.setSize(425, 550);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		JPanel panel = new JPanel();
        panel.setBackground(Color.black);
        frame.setContentPane(panel);

		frame.setLayout(null);
	}

	public static void addButtons(String symbol, int posX, int posY, int sizeX, int sizeY, Color color) {
		s
	}

	public static double add(double ... nums) {
		double total = nums[0];
		for (int i = 1; i < nums.length; i++) {
			total += nums[i];
		}
		return total;
	}

	public static double subtract(double ... nums) {
		double total = nums[0];
		for (int i = 1; i < nums.length; i++) {
			total -= nums[i];
		}
		return total;
	}

	public static double multiply(double ... nums) {
		double total = nums[0];
		for (int i = 1; i < nums.length; i++) {
			total *= nums[i];
		}
		return total;
	}

	public static double divide(double ... nums) {
		double total = nums[0];
		for (int i = 1; i < nums.length; i++) {
			total /= nums[i];
		}
		return total;
	}
}
