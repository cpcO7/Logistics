document.addEventListener("DOMContentLoaded", function () {
    let phoneInput = document.querySelector("#id_phone_number");
    if (phoneInput) {
        $(phoneInput).inputmask({
            mask: "+\\9\\98(99) 999-99-99",
            showMaskOnHover: false,
            showMaskOnFocus: true
        });
    }
});
