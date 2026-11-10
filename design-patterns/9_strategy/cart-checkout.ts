import { fileURLToPath } from "url";

abstract class PaymentStrategy {
  abstract pay(amount: number): void;
}

class CreditCardPayment extends PaymentStrategy {
  private card_number: string;
  private card_holder: string;
  private cvv: string;
  private expiry_date: string;

  constructor(
    card_number: string,
    card_holder: string,
    cvv: string,
    expiry_date: string,
  ) {
    super();
    this.card_number = card_number;
    this.card_holder = card_holder;
    this.cvv = cvv;
    this.expiry_date = expiry_date;
  }

  pay(amount: number) {
    console.log(
      `Paid ${amount} using Credit Card ending with ${this.card_number.slice(-4)} `,
    );
  }
}

class PayPalPayment extends PaymentStrategy {
  private email: string;

  constructor(email: string) {
    super();
    this.email = email;
  }

  pay(amount: number) {
    console.log(`Paid ${amount} using PayPal account ${this.email}`);
  }
}

class OrderService {
  private payment_strategy?: PaymentStrategy;

  constructor() {}

  set_payment_strategy(strategy: PaymentStrategy) {
    this.payment_strategy = strategy;
  }

  checkout(amount: number) {
    if (!this.payment_strategy) {
      console.error("Please select a payment method before checking out.");
      return;
    }

    this.payment_strategy.pay(amount);
  }
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const orderService = new OrderService();
  orderService.set_payment_strategy(
    new CreditCardPayment("1234567890123456", "John Doe", "123", "12/25"),
  );
  orderService.checkout(100.0);

  orderService.set_payment_strategy(new PayPalPayment("john.doe@example.com"));
  orderService.checkout(200.0);
}
