
    function redirectToMainPage() {
        // Get the URL from the hidden input field and use it to redirect.
        const servicesUrl = document.getElementById('services-url').value;
        window.location.href = servicesUrl;
    }

