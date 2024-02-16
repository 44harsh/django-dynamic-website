function valid() {
    console.log("hello again")
    var nam = document.f1.nam.value;
    var mother = document.f1.mother.value;
    var mobile = document.f1.mobile.value;
    var mobile1 = parseInt(mobile);
    var email = document.f1.email.value;
    var pass = document.f1.pass.value;
    var pass2 = document.f1.pass2.value;
    var letter = document.getElementById("letter");
    var capital = document.getElementById("capital");
    var number = document.getElementById("number");
    var length = document.getElementById("length");


    if (nam == "") {
        alert("enter name");
        document.f1.nam.focus();
        return false;
    }
    if (mother == "") {
        alert("enter mother's name");
        document.f1.mother.focus();
        return false;
    }
    if (mobile == "") {
        alert("enter mobile number");
        document.f1.mobile.focus();
        return false;
    }
    if (email == "") {
        alert("enter email");
        document.f1.email.focus();
        return false;
    }
    if (pass == "") {
        alert("enter password");
        document.f1.pass.focus();
        return false;
    }
    if (pass2 == "") {
        alert("enter re-enter password");
        document.f1.pass2.focus();
        return false;
    }
    if (isNaN(mobile1)) {
        alert("enter valid number")
        document.f1.mobile.focus();
        document.f1.mobile.value = "";
        return false;
    }
    if (pass != pass2) {
        alert("password is not same")
        document.f1.pass.value = "";
        document.f1.pass2.value = "";
        document.f1.pass.focus();
        return false;
    }
    pass.onfocus = function() {
        document.getElementById("message").style.display = "block";
    }
    pass.onblur = function() {
        document.getElementById("message").style.display = "none";
    }

    // When the user starts to type something inside the password field
    pass.onkeyup = function() {
        // Validate lowercase letters
        var lowerCaseLetters = /[a-z]/g;
        if (pass.value.match(lowerCaseLetters)) {
            letter.classList.remove("invalid");
            letter.classList.add("valid");
        } else {
            letter.classList.remove("valid");
            letter.classList.add("invalid");
        }

        // Validate capital letters
        var upperCaseLetters = /[A-Z]/g;
        if (pass.value.match(upperCaseLetters)) {
            capital.classList.remove("invalid");
            capital.classList.add("valid");
        } else {
            capital.classList.remove("valid");
            capital.classList.add("invalid");
        }

        // Validate numbers
        var numbers = /[0-9]/g;
        if (pass.value.match(numbers)) {
            number.classList.remove("invalid");
            number.classList.add("valid");
        } else {
            number.classList.remove("valid");
            number.classList.add("invalid");
        }

        // Validate length
        if (pass.value.length >= 8) {
            length.classList.remove("invalid");
            length.classList.add("valid");
        } else {
            length.classList.remove("valid");
            length.classList.add("invalid");
        }
    }
}