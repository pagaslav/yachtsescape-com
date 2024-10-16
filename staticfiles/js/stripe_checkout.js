// static / js / stripe_checkout.js

// Load Stripe public key from the template
const stripe = Stripe(stripePublicKey)

// Define an async function to initialize the checkout session
async function initialize() {
  // Function to fetch the client secret from the server
  const fetchClientSecret = async () => {
    const response = await fetch("/create-checkout-session", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken(), // Include CSRF token for security
      },
    })
    // Extract the clientSecret from the server's response
    const { clientSecret } = await response.json()
    return clientSecret
  }

  // Initialize the embedded checkout with the client secret
  const checkout = await stripe.initEmbeddedCheckout({
    fetchClientSecret, // Use the function defined above
  })

  // Mount Checkout to the specified div
  checkout.mount("#checkout")
}

// Function to retrieve CSRF token from cookies for security
function getCSRFToken() {
  let cookieValue = null
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";")
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim()
      if (cookie.startsWith("csrftoken=")) {
        cookieValue = decodeURIComponent(cookie.substring("csrftoken=".length))
        break
      }
    }
  }
  return cookieValue
}

// Call the initialize function to set up the checkout
initialize()
