import java.util.*;
import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) {
        Socket socket = null;
        java.io.InputStreamReader insr = null;
        java.io.OutputStreamWriter oswr = null;
        java.io.BufferedReader br = null;
        java.io.BufferedWriter bw = null;
        try {
            socket = new Socket("localhost", 8081);
            insr = new InputStreamReader(socket.getInputStream());
            oswr = new OutputStreamWriter(socket.getOutputStream());
            br = new BufferedReader(insr);
            bw = new BufferedWriter(oswr);
            Scanner sc = new Scanner(System.in);
            System.out.println("Send Message to server:");
            while (true) {
                String msgtosend = sc.nextLine();
                bw.write(msgtosend);
                bw.newLine();
                bw.flush();
                if (msgtosend.equalsIgnoreCase("BYE")) {
                    break;
                }
            }
            bw.close();
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
