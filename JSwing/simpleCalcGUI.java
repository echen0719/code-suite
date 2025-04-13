import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class simpleCalcGUI {
	private static JFrame frame = new JFrame("Simple 4 Function Calculator");

	public static void main(String[] args) {
		frame.setSize(425, 650);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		JPanel background = new JPanel();
		background.setBackground(Color.black);
		frame.setContentPane(background);
		frame.setLayout(null);
		buttons();
		inputs();
		frame.setVisible(true);
		/* System.out.println(add(1, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7)); // 1 + 2.1 + 3.2 + 4.3 + 5.4 + 6.5 + 7.6 + 8.7 = 38.8
		System.out.println(subtract(10.9, 9.8, 8.7)); // 10.9 - 9.8 - 8.7 = -7.6
		System.out.println(multiply(1, 2, 3, 4, 5)); // 5! = 120
		System.out.println(divide(120, 5, 4, 3, 2, 1)); // 120 / 5! = 1 */
	}

	public static void buttons() {
		addButtons("AC", 25, 125, 75, 75, new Color(92, 92, 95));
		addButtons("%", 125, 125, 75, 75, new Color(92, 92, 95));
		addButtons("x²", 225, 125, 75, 75, new Color(92, 92, 95));
		addButtons("+/-", 25, 525, 75, 75, new Color(92, 92, 95));
		addButtons("1", 25, 425, 75, 75, new Color(42, 42, 44));
		addButtons("2", 125, 425, 75, 75, new Color(42, 42, 44));
		addButtons("3", 225, 425, 75, 75, new Color(42, 42, 44));
		addButtons("4", 25, 325, 75, 75, new Color(42, 42, 44));
		addButtons("5", 125, 325, 75, 75, new Color(42, 42, 44));
		addButtons("6", 225, 325, 75, 75, new Color(42, 42, 44));
		addButtons("7", 25, 225, 75, 75, new Color(42, 42, 44));
		addButtons("8", 125, 225, 75, 75, new Color(42, 42, 44));
		addButtons("9", 225, 225, 75, 75, new Color(42, 42, 44));
		addButtons("0", 125, 525, 75, 75, new Color(42, 42, 44));
		addButtons(".", 225, 525, 75, 75, new Color(42, 42, 44));
		addButtons("/", 325, 125, 75, 75, new Color(255, 159, 10));
		addButtons("×", 325, 225, 75, 75, new Color(255, 159, 10));
		addButtons("-", 325, 325, 75, 75, new Color(255, 159, 10));
		addButtons("+", 325, 425, 75, 75, new Color(255, 159, 10));
		addButtons("=", 325, 525, 75, 75, new Color(255, 159, 10));
	}

	public static void inputs() {
		JLabel box = new JLabel();
		box.setText("Lorem Ipsum ... Something ... Whatever");
		box.setBackground(new Color(50, 50, 50));
		box.setOpaque(true);
		box.setFont(new Font("Arial", Font.BOLD, 28));
		box.setForeground(Color.white);
		box.setBounds(25, 25, 375, 75);
		frame.add(box);
	}

	public static void addButtons(String symbol, int posX, int posY, int sizeX, int sizeY, Color color) {
		JButton button = new JButton(symbol);
		button.setBounds(posX, posY, sizeX, sizeY);
		button.setBackground(color);
		button.setForeground(Color.white);
		button.setFont(new Font("Arial", Font.BOLD, 28));
		frame.add(button);
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
