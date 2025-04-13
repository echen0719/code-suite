import javax.swing.*;
import java.awt.*;

public class learningJavaSwing {
	private static Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize(); // found online
	private static JFrame frame = new JFrame("Name of Window - I think - yeah, it is");
	private static int width = (int)screenSize.width;
	private static int height = (int)screenSize.height;

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
		JButton helloWorld = new JButton("Hello World!");
		helloWorld.setBounds((width-200)/2, (height-50)/2, 200, 50); //center
		frame.add(helloWorld);
	}

	public static void swing() {
		frame.setSize(width, height);
		frame.setLocationRelativeTo(null); // center on screen
		frame.setLayout(null); // absolute location
	}
}
