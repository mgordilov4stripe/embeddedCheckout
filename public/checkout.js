// This is your test secret API key.
const stripe = Stripe("pk_test_51OuCCXK0g9v1y00EJNABu8ve8eqZgjpoocl3aVQJJ2tKiSzrvo7jUWXPuZjKVekYDe7yIH5SWyTr1qF4vRkRQnxv00x3J6ZcLg");

initialize();

// Create a Checkout Session
async function initialize() {
  const fetchClientSecret = async () => {
    const response = await fetch("/create-checkout-session", {
      method: "POST",
    });
    const { clientSecret } = await response.json();
    return clientSecret;
  };

  const checkout = await stripe.initEmbeddedCheckout({
    fetchClientSecret,
  });

  // Mount Checkout
  checkout.mount('#checkout');
}