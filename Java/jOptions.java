import javax.swing.*;
import java.awt.*;

public class jOptions {
    public static void main(String[] args) {
        String inputPass = "";
        JOptionPane.showMessageDialog(null, "Admin privileges needed for action", "Warning", JOptionPane.WARNING_MESSAGE);
        do { inputPass = JOptionPane.showInputDialog("Enter sysadmin password: "); }
        while (!inputPass.equals("1a2b3c"));

        JOptionPane.showMessageDialog(null, "Your PC has been hacked.", "Fatal Error", JOptionPane.ERROR_MESSAGE);
    }
}