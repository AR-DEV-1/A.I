import java.util.Scanner;

public class AI {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String response;
        
        System.out.println("Hello, I am an AI. How can I assist you today?");
        response = scanner.nextLine();
        
        // Decision tree
        if (response.contains("weather")) {
            System.out.println("The weather is currently sunny and 25°C.");
        } else if (response.contains("news")) {
            System.out.println("The latest news is that a new scientific discovery has been made in the field of astrophysics.");
        } else if (response.contains("joke")) {
            System.out.println("Why did the tomato turn red? Because it saw the salad dressing!");
        } else {
            System.out.println("I'm sorry, I don't understand. Can you please be more specific?");
        }
    }
}
