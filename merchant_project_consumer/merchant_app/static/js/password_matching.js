function check() {
    if (document.getElementById('password1').value == document.getElementById('password2').value)
    {
        document.getElementById("message").style.color = 'green';
        document.getElementById("message").innerHTML = "Matching";
    }
    else {
        document.getElementById("message").style.color = 'red';
        document.getElementById("message").innerHTML = "Not Matching";
    }
}