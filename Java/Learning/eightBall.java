import java.util.Scanner; // added to allow keyboard input
public class eightBall {
    public static void main(String[]args) {
        // Tell the user to enter a question
        Scanner scan = new Scanner(System.in);
        System.out.println("Welcome to the Magic 8 Ball!");
        System.out.print("Enter your question and I will answer it: ");
        String question = scan.nextLine();

        int random = (int)(Math.random() * 8 + 1);

        long startIfElseIf = System.nanoTime();
        ifElseIfStatements(random);
        double endIfElseIf = System.nanoTime();
        double durationIfElseIf = endIfElseIf - startIfElseIf;

        double startSwitchCase = System.nanoTime();
        switchCaseStatements(random);
        double endSwitchCase = System.nanoTime();
        double durationSwitchCase = endSwitchCase - startSwitchCase;

        System.out.println("\n\nJava Switch statements are " + ((durationIfElseIf - durationSwitchCase) * 100 / durationIfElseIf) +
            "% faster than If-ElseIf-Else statements. " + (int)durationIfElseIf + "ns vs " + (int)durationSwitchCase + "ns.");

        System.out.println("\nThis is not definitive as the speed of these statements vary widely on use.");

        scan.close();
    }

    public static void ifElseIfStatements(int random) {

        System.out.print("\nIf-ElseIf-Else: ");

        if (random == 1) {
            System.out.print("It is certain");
        } else if (random == 2) {
            System.out.print("Most likely");
        } else if (random == 3) {
            System.out.print("Ask again later");
        } else if (random == 4) {
            System.out.print("Don't count on it");
        } else if (random == 5) {
            System.out.print("Yes");
        } else if (random == 6) {
            System.out.print("Very doubtful");
        } else if (random == 7) {
            System.out.print("You may rely on it");
        } else if (random == 8) {
            System.out.print("Outlook is not good");
        }
    }

    public static void switchCaseStatements(int random) {

        System.out.print("\nSwitch: ");

        switch (random) {
        case 1:
            System.out.print("It is certain");
            break;

        case 2:
            System.out.print("Most likely");
            break;

        case 3:
            System.out.print("Ask again later");
            break;

        case 4:
            System.out.print("Don't count on it");
            break;

        case 5:
            System.out.print("Yes");
            break;

        case 6:
            System.out.print("Very doubtful");
            break;

        case 7:
            System.out.print("You may rely on it");
            break;

        case 8:
            System.out.print("Outlook is not good");
            break;

        default:
            System.out.print("Invalid input");
            break;
        }
    }
}
