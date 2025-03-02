import javax.swing.*;

public class eightBallGUI {
    public static void main(String[]args) {
        String answer = JOptionPane.showInputDialog("Magic Eight Ball\nEnter your question: ");
        if (answer != null && answer.length() > 0)
            JOptionPane.showMessageDialog(null, eightBall((int)(Math.random() * 8 + 1)), "Your answer:", JOptionPane.INFORMATION_MESSAGE);
        else
            System.exit(0);
    }

    // I'll probably add a eightBall image with text later on
    public static String eightBall(int random) {
        switch (random) {
        case 1:
            return "It is certain";
        case 2:
            return "Most likely";
        case 3:
            return "Ask again later";
        case 4:
            return "Don't count on it";
        case 5:
            return "Yes";
        case 6:
            return "Very doubtful";
        case 7:
            return "You may rely on it";
        case 8:
            return "Outlook is not good";
        default:
            return "";
        }
    }
}
