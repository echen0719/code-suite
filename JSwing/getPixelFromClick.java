import javax.swing.*;
import java.awt.event.*;

public class getPixelFromClick {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Mouse Position");
        JPanel panel = new JPanel();
        frame.add(panel);

        // https://stackoverflow.com/questions/16431455
        panel.addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                int x = e.getX();
                int y = e.getY();
                System.out.println("Mouse clicked at X: " + x + ", Y: " + y);
            }
        });

        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setUndecorated(true);
        frame.setVisible(true);
    }
}
