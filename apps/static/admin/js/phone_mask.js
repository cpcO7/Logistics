jQuery(document).ready(function ($) {
    console.log("Phone mask script loaded.");

    let phoneInput = $("#id_phone_number");

    if (phoneInput.length) {
        phoneInput.inputmask({
            mask: "+1 (999) 999-9999",
            showMaskOnHover: false,
            showMaskOnFocus: true
        });
        console.log("Mask applied successfully.");
    } else {
        console.error("Phone input field not found.");
    }
});

