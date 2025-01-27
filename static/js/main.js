document.addEventListener('DOMContentLoaded', function() {
    const usernameField = document.getElementById('username');
    const passwordField = document.getElementById('password');
    const loginButton = document.getElementById('login-button');

    function validateForm() {
        const username = usernameField.value.trim();
        const password = passwordField.value.trim();
        loginButton.disabled = !username || !password;
    }

    usernameField.addEventListener('input', validateForm);
    passwordField.addEventListener('input', validateForm);
});