const form = document.querySelector('.form');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('pass');
const emailError = document.querySelector('.valid.error');

// Function to validate email address
function validateEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
}

// Function to validate form data
function validateForm() {
  let isValid = true;

  if (!validateEmail(emailInput.value)) {
    emailInput.classList.add('error');
    emailError.style.display = 'block';
    isValid = false;
  } else {
    emailInput.classList.remove('error');
    emailError.style.display = 'none';
  }

  if (passwordInput.value === '') {
    passwordInput.classList.add('error');
    isValid = false;
  } else {
    passwordInput.classList.remove('error');
  }

  return isValid;
}

// Function to handle form submission
function handleSubmit(event) {
  event.preventDefault();

  if (validateForm()) {
    form.submit();
  }
}

// Attach event listener to form submit button
form.addEventListener('submit', handleSubmit);
