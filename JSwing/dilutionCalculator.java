import javax.swing.*;

public class dilutionCalculator {
    public static void main(String[] args) {
        JOptionPane.showMessageDialog(null, "Calculate the volume of a stock concentrate to get a specified volume or concentration using M1V1 = M2V2.");
        double stockConc = Double.parseDouble(JOptionPane.showInputDialog(null, "Stock concentration (M):"));
        double finalVol = Double.parseDouble(JOptionPane.showInputDialog(null, "Final volume (L):"));
        double finalConc = Double.parseDouble(JOptionPane.showInputDialog(null, "Final concentration (M):"));
        if (finalConc < stockConc && stockConc > 0) {
            double stockVol = finalConc * finalVol / stockConc;
            JOptionPane.showMessageDialog(null, "Required volume of stock solution = " + stockVol + " L");
        }
    }
}
