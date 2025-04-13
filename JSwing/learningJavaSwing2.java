import javax.swing.*;
import java.awt.*;
import java.net.*;

public class learningJavaSwing2 {
	public static void main(String[] args) {
		JFrame frame = new JFrame("Windows Name");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // closing window actually terminates program
		frame.setSize(500, 500);
		frame.setBackground(Color.white);

		JLabel label = new JLabel();
		label.setText("<html>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eu tempor tortor. Aenean accumsan nunc quis scelerisque ullamcorper. Proin vel quam nec mauris volutpat dapibus. Sed sit amet ipsum at ex dapibus varius. Fusce ullamcorper odio facilisis, sodales lorem non, facilisis ipsum.</html>"); // html formats it, I guess?
		label.setFont(new Font("Calibri", Font.PLAIN, 20)); // Font("Font", Font.PLAIN, size)
		label.setBackground(Color.black);
		label.setOpaque(true);
		label.setForeground(Color.white);
		label.setVerticalAlignment(JLabel.TOP); // start at top instead of center
		//label.setPreferredSize(new Dimension(250, 250)); // so pack will choose this size instead of auto
		label.setBounds(0, 0, 250, 250);

		frame.add(label);
		frame.setLayout(null);
		//frame.pack(); // just pack
		frame.setVisible(true);
	}
}
