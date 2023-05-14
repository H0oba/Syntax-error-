
function validate()
{
    let email = document.getElementsByName('email');
    let password = document.getElementsByName('password');

    if (password != '12345')
    {
        alert('Please Enter The Password Correctly');
        return false;
    }
}

const form = document.querySelector('#login-form');
form.addEventListener('submit', (event) => {
  event.preventDefault();
  
  const email = form.elements.email.value;
  const password = form.elements.password.value;
  
  if (document.querySelector('#remember-password').checked) {
    localStorage.setItem(email, password);
  }
  
  // log the user in...
});