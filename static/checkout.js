// This is your test secret API key.
const stripe = Stripe("pk_test_51OlENfChg3YLxEh2vGpvHzEXWhxZMyXHCDf2cBvNIBIb4hcTHdO2KWgbiXKNyq2pEADb9NsA9jA05k8YhZEtmHjy00sAciTEhL");

// initialize();

// // Create a Checkout Session
// async function initialize() {
//   const fetchClientSecret = async () => {
//     const response = await fetch("/create-checkout-session", {
//       method: "POST",
//     });
//     const { clientSecret } = await response.json();
//     return clientSecret;
//   };

//   const checkout = await stripe.initEmbeddedCheckout({
//     fetchClientSecret,
//   });

//   // Mount Checkout
//   checkout.mount('#checkout');
// }

let buttons = document.querySelectorAll('.link-button')

buttons.forEach(button=> {button.addEventListener('click', function(e) {
    e.preventDefault(); fetchProduct();})
}) 

function fetchProduct(){

    let prods = document.getElementsByClassName('product')
    console.log(prods)
    prods.forEach(prod=> {console.log(prod); return prod.innerText()})


}