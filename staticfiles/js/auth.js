const phoneNumberField = document.getElementById('phoneNumber');
const codeField = document.getElementById('code');
const getCodeButton = document.getElementById('getCode');
const signInWithPhoneButton = document.getElementById('signInWithPhone');

const auth = firebase.auth();

// Creates and render the captcha
window.recaptchaVerifier = new firebase.auth.RecaptchaVerifier('recaptcha-container');
recaptchaVerifier.render().then(widgetId => {
  window.recaptchaWidgetId = widgetId;
})

const sendVerificationCode = () => {
  const phoneNumber = phoneNumberField.value;
  const appVerifier = window.recaptchaVerifier;
  
  // Sends the 6 digit code to the user's phone
  auth.signInWithPhoneNumber(phoneNumber, appVerifier)
  .then(confirmationResult => {
    const sentCodeId = confirmationResult.verificationId;
    
    // Sign in if the verification code is set correctly
    signInWithPhoneButton.addEventListener('click', () => signInWithPhone(sentCodeId));
  })
}

const signInWithPhone = sentCodeId => {
  const code = codeField.value;
  // A credential object (contains user's data) is created after a comparison between the 6 digit code sent to the user's phone
  // and the code typed by the user in the code field on the html form.
  const credential = firebase.auth.PhoneAuthProvider.credential(sentCodeId, code);
  auth.signInWithCredential(credential)
  .then(() => {
    console.log('Signed in successfully !');
  })
  .catch(error => {
    console.error(error);
  })
}

getCodeButton.addEventListener('click', sendVerificationCode);