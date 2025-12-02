import javax.swing as swing
import java.awt as awt

def quit(e):
    sys.exit()

frame = JFrame("Sample Window")
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
frame.setLayout(FlowLayout())

heading = swing.JLabel('Sample heading')
quit = swing.JButton('Exit', actionPerformed=quit, background=Color.red, foreground=Color.white)

frame.add(heading)
frame.add(quit)

frame.setVisible(True)