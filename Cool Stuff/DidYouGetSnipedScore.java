// Translation in Java

import java.util.*; //imports java utility class for Scanner and Random classes
import java.io.*; //imports java i/o class for opening website

public class DidYouGetSnipedScore {
	
	static class ReferenceScore {
        public String reference_players; // Create a field for reference_players
        public double reference_scores;   // Create a field for reference_scores

        public ReferenceScore(String player, double score) {
            reference_players = player;
            reference_scores = score;
        }
    }
	
  public static void main(String[] args) {
    
    Scanner keyboard = new Scanner(System.in); //imports Scanner class for user input
    
    //ReferenceScore[] references = new ReferenceScore[3];
    ArrayList<ReferenceScore> references = new ArrayList<ReferenceScore>();
    
    //Defines reference scores
    references.add(new ReferenceScore("Did You Get Sniped?", 775));
    references.add(new ReferenceScore("SAUNA MAKKARA", 1984));
    references.add(new ReferenceScore("Walrus", 1311));
	references.add(new ReferenceScore("Zaxianthom", 556));
    //Add more references if needed
    
    System.out.println("DYGS Score Python Program v0.5"); //Display program information
    
    int restart_option = 2; //automatically performs do loop
    
    do {
      System.out.println("\nCreated By: Did You Get Sniped?"); //Display program creator's name
      System.out.println("This DYGS Score calculator for War Brokers is not an official" + 
                         "\nprogram or calculation and is made only for fun.");
      
      //Get user input for the selected option      
      System.out.println("\n1. Calculate DYGS Score");
      System.out.println("2. Explain the Process");
      System.out.println("3. View Reference Scores");
      System.out.println("4. Visit DYGS Score GitHub Releases");
      System.out.println("5. List of Statistics Websites");
      System.out.print("\nSelect an option (1, 2, 3, 4, or 5): ");
      int option = keyboard.nextInt();
      
      	if (option == 1) {
          double score = calculator(); //Directs to calculator class
          System.out.println("\nThe DYGS Score is: " + score + " (can be biased towards people" + 
                             " who have played longer, but it's better than inflated elo).");
        }
      
      	else if (option == 2) {
          explaination(); //Directs to explainations
        }
      
      	else if (option == 3) {
          System.out.println(); //Directs to reference scores
          referenceScores(references);
        }
      
      	else if (option == 4) {
          github(); //Directs to DYGS releases
          
        }
          
        else if (option == 5) {
          websitesList(); //Directs to websites to find player stats
        }
          
      	else {
          System.out.print("\nInvalid option. Please select the integers 1, 2, 3, 4, or 5.");
        }
      
      System.out.print("\nPress 1 to exit or 2 to restart the program: ");
      restart_option = keyboard.nextInt();
      
      if (restart_option == 2) {
      
      Random rng = new Random(); //import Random class to generate random numbers
      int rnd = rng.nextInt(9)+2; //Generates random number between 2 and 10.
      
      //Display the calculated wait time
      System.out.println("\nCalculating...Please wait about " + rnd + " seconds.");
      
      System.out.print("[");
	  for (int i = 0; i < 50; i++) {
            try {
                Thread.sleep(rnd * 1000 / 50); // Calculate the sleep time based on the number of seconds
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.print("=");
      }

      System.out.print("]");
      System.out.println();
        
      }
    }
    
    while (restart_option == 2);
    
  }
  
  public static double calculator() {
    Scanner keyboard = new Scanner(System.in);
    
    //Get user input for Level, K/D ratio, and ELO
	System.out.print("\nEnter the player's Level: ");
    int level = keyboard.nextInt();
    System.out.print("Enter the player's Kills/Deaths ratio: ");
    double kd_ratio = keyboard.nextDouble();
    System.out.print("Enter the player's ELO: ");
    double elo = keyboard.nextDouble();
    
    double dygs_score = (0.45 * level) + (0.35 * kd_ratio) * 100 + (0.20 * elo);
    dygs_score = Math.round(dygs_score * 10.0) / 10.0;
    
    return dygs_score;
  }
  
  public static void explaination() {
    
    //Explains the process of calculating the score
    //This section provides a step-by-step breakdown of how the DYGS Score is calculated:
          
    System.out.println("\nExplanation of the DYGS Score Calculation Process: ");
    
    //Step 1: Level Contribution
    System.out.println("\n1. We take the player's level and multiply it by 0.45.");
    System.out.println("   This accounts for the player's experience and progression in the game." + 
                       "\n   A higher level means a higher contribution to the DYGS Score, as it" + 
                       "\n   reflects more experience and skill.");
    
    //Step 2: Kills/Death (K/D) Ratio Contribution
    System.out.println("\n2. We take the player's K/D ratio, multiply it by 100, and multiply it by 0.35.");
    System.out.println("   The K/D ratio is a crucial indicator of a player's performance. This step" + 
                       "\n   rewards players with a high K/D ratio, indicating their proficiency in" + 
                       "\n   eliminating opponents while minimizing deaths.");
    
    //Step 3: ELO Contribution
    System.out.println("\n3. We take the player's ELO and multiply it by 0.20.");
    System.out.println("   ELO is a common rating system in competitive games, representing a" + 
                       "\n   player's skill level. A higher ELO rating positively impacts the DYGS" + 
                       "\n   Score, highlighting the player's competitiveness in ranked matches.");
    
    //Step 4: Calculate the Final DYGS Score
    System.out.println("\n4. Finally, we add the results of the three steps to get the DYGS Score.");
    System.out.println("   The final DYGS Score is a comprehensive assessment of a player's performance," + 
                       "\n   experience, and competitive abilities in War Brokers.");
  }
  
  public static void referenceScores(ArrayList<ReferenceScore> references) {
    for(ReferenceScore reference : references) {
        System.out.println(reference.reference_players + "'s score is: " + reference.reference_scores + ".");
    }
    System.out.println("\nCan be biased towards people who have played longer, but" + 
                       "\nit's better than inflated elo");
  }
  
  public static void github() {
    Object obj = new Object();
    
    //Opens the GitHub releases page with a countdown
    System.out.println("You are about to be redirected to the DYGS Score GitHub Releases page.");
    System.out.println("Please wait for a 3-second countdown.\n");
    
    for (int time = 3; time > 0; time--) {
      System.out.println(time + "...");
      try {Thread.sleep(1000);}
      catch (InterruptedException ex) {}
    }
    
    try {
        String github = "https://github.com/DidYouGetSniped/DYGS-Score/releases"; //open DYGS's releases
        java.awt.Desktop.getDesktop().browse(java.net.URI.create(github));
    } catch (IOException e) {
        System.out.println("Error opening the URL: " + e.getMessage());
    }
  }
  
  public static void websitesList() {
    System.out.println("\nPomp's WB Stats: https://stats.wbpjs.com/");
    System.out.println("Official WB Stats: https://stats.warbrokers.io");
    System.out.println("Copy and paste these into your browser.");
  } 
}

// Read ME:

/*
The idea for this code comes from Did You Get Sniped?'s Github. He deserves all credit for this project. Check him
at https://github.com/DidYouGetSniped. Thanks for the idea, DYGS.
*/
