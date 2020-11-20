
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.border.Border;
import javax.swing.border.TitledBorder;
import javax.swing.border.EtchedBorder; 
public class SampGUI implements ActionListener  {

   private JTextArea status; // text area to print game status
   //Menu
   private JFrame frame = new JFrame();
   private JMenuBar menuBar;
   private JMenu menu,subMenu;
   private JMenuItem menuItem;
   private TitledBorder midLabel;
   private Border loweredetched;
   private JPanel midPanel,panel2,midProg1;
   private JTextField jTextField;
   private JProgressBar jpBar ;
   private Container contentPane;
   //TicTacToe Buttons
   private static JButton start,end,reset,single, multi;
   public final int frameWidth= 375;
   public final int frameHeight= 200;
   //private int set = 1;
   
   // Labels
   //private JLabel currentTurn = new JLabel("WELCOME TO REACTEN!WHAT MODE OF GAME WOULD YOU LIKE TO PLAY?"+mode);
   private JLabel Player1Wins, Player2Wins,playerTies,Welcome,jlabel;
   private int Player1score,Player2score,tieScore=0;
   

   //In-game Variables
   private String player1="P1";
   private String player2="P2";
   private int initgameState=0;
   private String currentPlayer;
   private  String defaultplayer=player1;
public SampGUI() {
		// the clickable button
         start = new JButton("START");
         end = new JButton("QUIT");
         reset = new JButton("RESET");
         single = new JButton("Single Player");
         multi = new JButton("Multi Player");
        start.addActionListener(this);
        end.addActionListener(this);
         reset.addActionListener(this);
         single.addActionListener(this);
         multi.addActionListener(this);
         Welcome = new JLabel("WELCOME TO REACTEN!WHAT MODE OF GAME WOULD YOU LIKE TO PLAY?PLEASE CLICK START FIRST");

        // the panel with the button and text
         loweredetched = BorderFactory.createEtchedBorder(EtchedBorder.LOWERED);
        JPanel panel = new JPanel();
        JPanel messagepanel = new JPanel();
        panel.setBorder(BorderFactory.createEmptyBorder(30, 30, 10, 30));
        panel.setLayout(new GridLayout(0, 10));
        panel.add(start);
        panel.add(end);
        panel.add(reset);
        messagepanel.setLayout(new FlowLayout());
        messagepanel.add(Welcome);


     //panel for Labels and Text Entry section
      midPanel = new JPanel();
      panel2 = new JPanel();
      midProg1 = new JPanel();
      jpBar = new JProgressBar(0,100);
      contentPane = frame.getContentPane();
      midPanel.setLayout(new GridLayout(1,2));
      jlabel = new JLabel("A message ");
      jTextField = new JTextField("You can type in this field");
      midLabel = BorderFactory.createTitledBorder(loweredetched, "MESSAGE BLOCK");
      midPanel.add(jlabel);
      midPanel.add(jTextField);
      midPanel.setBorder(midLabel);

      //panel2.add(midPanel);
      panel2.add(midProg1);
      contentPane.add(panel2,BorderLayout.SOUTH);


        panel.add(single);
        panel.add(multi);
        panel2.add(midPanel);
        //jlabel = new JLabel("MESSAGE BLOCK ");
        //messagepanel.add(jlabel);
        // set up the frame and display it
        frame.add(panel, BorderLayout.CENTER);

        frame.add(messagepanel, BorderLayout.NORTH);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setTitle("NewGUI");
        frame.pack();
        frame.setVisible(true);

    
     
    }
public void GameMode1() {

                System.out.println("You have chose singleplayermode!");
}
public void GameMode2() {

                System.out.println("You have chose multiplayermode!");
}
public void StartGame() {

    System.out.println("Game start.What mode will you play in?");
}
public void QuitGame() {

    System.out.println("Player has quit game");
    System.exit(0);
}
public void resetGame() {
    System.out.println("Game reset.You can click start?");
}
    // process the button clicks
public void actionPerformed(ActionEvent e) {
        String cmd = e.getActionCommand();
        Object src = e.getSource();
        if (initgameState == 0){
            //System.out.println("WELCOME TO REACTEN!WHAT MODE OF GAME WOULD YOU LIKE TO PLAY?"+mode);
            if (cmd.equals("Single Player")){
                GameMode1();
                multi.setEnabled(false);
                //start.setEnabled(true);
                single.setEnabled(false);
                System.out.println("Game has officially begun in 3..2..1");
                start.setEnabled(false);
            }
            else if (cmd.equals("Multi Player")){
                GameMode2();
                single.setEnabled(false);
                //start.setEnabled(true);
                multi.setEnabled(false);
                System.out.println("Game has officially begun in 3..2..1");
                start.setEnabled(false);
            }
             if(cmd.equals("START"))
            {
            	end.setEnabled(false);
               reset.setEnabled(false);
                StartGame();
                //throw new IllegalArgumentException("Game has already started");
            }

            else if (cmd.equals("QUIT")){
            	start.setEnabled(false);
               end.setEnabled(false);
               reset.setEnabled(false);
               multi.setEnabled(false);
               single.setEnabled(false);
                    QuitGame();
                }


            else if (cmd.equals("RESET")){
            	
               end.setEnabled(false); 
               reset.setEnabled(false);
               multi.setEnabled(false);
               single.setEnabled(false);
                    resetGame();
                

                }
        }
    }

    // create one Frame
public static void main(String[] args) {
	          //start.setEnabled(false);
               //end.setEnabled(false);
               //reset.setEnabled(false);
               new SampGUI();
        //new actionPerformed()
    }
    }