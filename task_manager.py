import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        while (running) {

            System.out.print("Enter your name: ");
            String name = scanner.nextLine();

            System.out.print("Enter your age: ");
            int age = scanner.nextInt();
            scanner.nextLine(); // limpiar buffer

            if (age < 0) {
                System.out.println("Invalid age.");
            } else if (age >= 18) {
                System.out.println("You are an adult, " + name + ".");
            } else {
                System.out.println("You are a minor, " + name + ".");
            }

            System.out.println("\nDo you want to try again? (yes/no)");
            String answer = scanner.nextLine();

            if (!answer.equalsIgnoreCase("yes")) {
                running = false;
                System.out.println("Program finished.");
            }
        }

        scanner.close();
    }
}
