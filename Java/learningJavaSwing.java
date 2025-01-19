import javax.swing.*;
import java.awt.*;

public class learningJavaSwing {
	public static void main(String[] args) {
		JFrame frame = new JFrame("Name of Window - I think - yeah, it is");
		Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize(); // found online

		int width = (int)screenSize.width;
		int height = (int)screenSize.height;

		frame.setSize(width, height);
		frame.setLocationRelativeTo(null); // center on screen
		frame.setLayout(null); // absolute location

		JButton helloWorld = new JButton("Hello World!");
		helloWorld.setBounds((width-200)/2, (height-50)/2, 200, 50);

		frame.add(helloWorld);
		frame.setVisible(true);
	}
}
