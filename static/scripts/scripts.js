document.addEventListener('DOMContentLoaded', function () {
    const sellerPhoneButton = document.getElementById('seller-phone-button')
    const sellerEmailButton = document.getElementById('seller-email-button')
    const sellerPhoneNumber = document.getElementById('seller-phone-number')
    const sellerEmail = document.getElementById('seller-email')
    
    sellerPhoneButton.addEventListener('click', e => {
        displayPhoneNumber();
    });

    sellerEmailButton.addEventListener('click', e => {
        displayEmail();
    });

    function displayPhoneNumber() {
        sellerPhoneButton.classList.add('d-none');
        sellerPhoneNumber.classList.remove('d-none');
    }

    function displayEmail() {
        sellerEmailButton.classList.add('d-none');
        sellerEmail.classList.remove('d-none');
    }
});