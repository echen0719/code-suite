import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class simpleCalcGUI {
	private static Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize(); // found online
	private static JFrame frame = new JFrame("Simple 4 Function Calculator");
	private static int width = (int)screenSize.width;
	private static int height = (int)screenSize.height;
	private static JLabel status = new JLabel("");

	public static void main(String[] args) {
		swing();
		input();
		button();
		frame.setVisible(true);
	}

	public static void input() {
		JTextField input = new JTextField();
		input.setBounds((width-200)/2, (height-100)/2, 200, 25); //center but above button
		frame.add(input);
		// how to submit text and store in variable - later
	}

	public static void button() {
		JButton submit = new JButton("Submit");
		submit.setBounds((width-200)/2, (height-50)/2, 200, 50); // center

		submit.addActionListener(new ActionListener() { // standard action listener
			public void actionPerformed(ActionEvent event) {
				status.setText("Submitted");
			}
		} );

		frame.add(submit);
		frame.add(status);
	}

	public static void swing() {
		frame.setSize(width, height);
		frame.setLocationRelativeTo(null); // center on screen
		frame.setLayout(null); // absolute location
	}
}
