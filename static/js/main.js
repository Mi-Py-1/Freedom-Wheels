document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('success') === 'true') {
        var successModal = new bootstrap.Modal(document.getElementById('successModal'));
        successModal.show();
    }
});