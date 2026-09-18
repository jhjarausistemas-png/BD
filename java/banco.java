import java.util.scanner;
public  static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

        CuentaBancaria cuenta = new CuentaBancaria();

    System.out.println("valor a depositar");
    double deposito = scanner.nextDouble();
    cuenta.depositar(deposito);

    System.out.println("valor a retirar");
    double retiro = scanner.nextDouble();
    cuenta.retirar(retiro);

    cuenta.mostrarSaldo();
    scanner.close();
    }
}