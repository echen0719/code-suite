import java.util.*;

public class IdealGasLaw {
	private static Scanner silverNitrate = new Scanner(System.in);
	private static String pressureUnit;
	public static void main(String[] args) {
		double[] otherTerms = new double[4];
		System.out.println("Ideal Gas Law Calculator");

		System.out.println("\nGeneral Equation: PV = nRT");
		System.out.print("What do you want to solve for? ");
		String option = silverNitrate.nextLine();

		if (option.equalsIgnoreCase("Pressure") || option.equalsIgnoreCase("P")) {
			double pressure = solveForP();
			System.out.printf("\nPressure (" + pressureUnit + "): " + "%.2f", pressure);
		}
		else if (option.equalsIgnoreCase("Volume") || option.equalsIgnoreCase("V")) {
			System.out.printf("\nVolume (Liters): %.2f", solveForV());
		}
		else if (option.equalsIgnoreCase("Amount") || option.equalsIgnoreCase("n") || option.equalsIgnoreCase("Moles")) {
			System.out.printf("\nAmount (Moles): %.2f", solveForN());
		}
		else if (option.equalsIgnoreCase("Temperature") || option.equalsIgnoreCase("T")) {
			System.out.printf("\nTemperature (Kelvin): %.2f", solveForT());
		}
		else {
			System.out.println("Invalid value. Try again");
			System.exit(0);
		}
	}

	public static double solveForP() {
		System.out.println("\nEnter prompted values below");

		System.out.print("Constant (atm, kPa, torr, mmHg): ");
		String constant = silverNitrate.nextLine();

		System.out.print("\nVolume (in liters): ");
		double volume = silverNitrate.nextDouble();

		System.out.print("Amount (in moles): ");
		double amount = silverNitrate.nextDouble();

		System.out.print("Temperature (in kelvin): ");
		double temperature = silverNitrate.nextDouble();

		pressureUnit = whichConstant(constant);

		if (pressureUnit.equals("atm")) {
			return (amount*0.08205734*temperature)/volume;
		}
		else if (pressureUnit.equals("kPa")) {
			return (amount*8.3144598*temperature)/volume;
		}
		else if (pressureUnit.equals("torr/mmHg")) {
			return (amount*62.36358*temperature)/volume;
		}
		return 0;
	}

	public static double solveForV() {
		System.out.println("\nEnter prompted values below");

		System.out.print("Constant (atm, kPa, torr, mmHg): ");
		String constant = silverNitrate.nextLine();

		System.out.print("\nPressure (same as constant): ");
		double pressure = silverNitrate.nextDouble();

		System.out.print("Amount (in moles): ");
		double amount = silverNitrate.nextDouble();

		System.out.print("Temperature (in kelvin): ");
		double temperature = silverNitrate.nextDouble();

		pressureUnit = whichConstant(constant);

		if (pressureUnit.equals("atm")) {
			return (amount*0.08205734*temperature)/pressure;
		}
		else if (pressureUnit.equals("kPa")) {
			return (amount*8.3144598*temperature)/pressure;
		}
		else if (pressureUnit.equals("torr/mmHg")) {
			return (amount*62.36358*temperature)/pressure;
		}
		return 0;
	}

	public static double solveForN() {
		System.out.println("\nEnter prompted values below");

		System.out.print("Constant (atm, kPa, torr, mmHg): ");
		String constant = silverNitrate.nextLine();

		System.out.print("\nPressure (same as constant): ");
		double pressure = silverNitrate.nextDouble();

		System.out.print("Volume (in moles): ");
		double volume = silverNitrate.nextDouble();

		System.out.print("Temperature (in kelvin): ");
		double temperature = silverNitrate.nextDouble();

		pressureUnit = whichConstant(constant);

		if (pressureUnit.equals("atm")) {
			return (pressure*volume)/(0.08205734*temperature);
		}
		else if (pressureUnit.equals("kPa")) {
			return (pressure*volume)/(8.3144598*temperature);
		}
		else if (pressureUnit.equals("torr/mmHg")) {
			return (pressure*volume)/(62.36358*temperature);
		}
		return 0;
	}

	public static double solveForT() {
		System.out.println("\nEnter prompted values below");

		System.out.print("Constant (atm, kPa, torr, mmHg): ");
		String constant = silverNitrate.nextLine();

		System.out.print("\nPressure (same as constant): ");
		double pressure = silverNitrate.nextDouble();

		System.out.print("Volume (in moles): ");
		double volume = silverNitrate.nextDouble();

		System.out.print("Amount (in moles): ");
		double amount = silverNitrate.nextDouble();

		pressureUnit = whichConstant(constant);

		if (pressureUnit.equals("atm")) {
			return (pressure*volume)/(0.08205734*amount);
		}
		else if (pressureUnit.equals("kPa")) {
			return (pressure*volume)/(8.3144598*amount);
		}
		else if (pressureUnit.equals("torr/mmHg")) {
			return (pressure*volume)/(62.36358*amount);
		}
		return 0;
	}

	public static String whichConstant(String constant) {
		if (constant.equalsIgnoreCase("atm") || constant.equalsIgnoreCase("atmospheres") || constant.equalsIgnoreCase("atmosphere")) {
			return "atm";
		}
		else if (constant.equalsIgnoreCase("kPa") || constant.equalsIgnoreCase("kilopascals") || constant.equalsIgnoreCase("kilopascal")) {
			return "kPa";
		}
		else if (constant.equalsIgnoreCase("torr") || constant.equalsIgnoreCase("Torricelli") || constant.equalsIgnoreCase("mmHg") || constant.equalsIgnoreCase("Millimeters of mercury")) {
			return "torr/mmHg";
		}
		else {
			System.out.println("Invalid value. Try again.");
			System.exit(0);
		}
		return "";
	}
}
