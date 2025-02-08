import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class simpleCalcGUI {
	private static Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize(); // found online
	private static JFrame frame = new JFrame("Simple 4 Function Calculator");
	private static int width = (int)screenSize.width;
	private static int height = (int)screenSize.height;
	private static JLabel status = new JLabel();
	private static JTextField input = new JTextField();

	public static void main(String[] args) {
		//swing();
		//input();
		//button();
		//frame.setVisible(true);
		System.out.println(add(1, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7)); // 1 + 2.1 + 3.2 + 4.3 + 5.4 + 6.5 + 7.6 + 8.7 = 38.8
		System.out.println(subtract(10.9, 9.8, 8.7)); // 10.9 - 9.8 - 8.7 = -7.6
		System.out.println(multiply(1, 2, 3, 4, 5)); // 5! = 120
		System.out.println(divide(120, 5, 4, 3, 2, 1)); // 120 / 5! = 1
	}

	public static void input() {
		input.setBounds((width-200)/2, (height-100)/2, 200, 25); //center but above button
		frame.add(input);
		// how to submit text and store in variable - later
	}

	public static void button() {
		JButton submit = new JButton("Submit");
		submit.setBounds((width-200)/2, (height-50)/2, 200, 50); // center
		frame.add(submit);

		status.setBounds((width-200)/2, (height+100)/2, 250, 25); // center but below button
		status.setFont(new Font("Calibri", Font.PLAIN, 32));
		status.setForeground(Color.BLACK); // why called foreground?
		frame.add(status);

		submit.addActionListener(new ActionListener() { // standard action listener
			public void actionPerformed(ActionEvent e) {
				status.setText("Submitted: " + input.getText());
			}
		} );

		// I think actionListener goes last from code that I saw
	}

	public static void swing() {
		frame.setSize(width, height);
		frame.setLocationRelativeTo(null); // center on screen
		frame.setLayout(null); // absolute location
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
