function showAdditionalFields() {
    var maritalStatus = document.getElementById("maritalStatus").value;
    var additionalFieldsMarried = document.getElementById("additionalFieldsMarried");
    var additionalFieldsWidowed = document.getElementById("additionalFieldsWidowed");

    if (maritalStatus === "married") {
        additionalFieldsMarried.style.display = "block";
        additionalFieldsWidowed.style.display = "none";
    } else if (maritalStatus === "widowed") {
        additionalFieldsWidowed.style.display = "block";
        additionalFieldsMarried.style.display = "none";
    } else {
        additionalFieldsMarried.style.display = "none";
        additionalFieldsWidowed.style.display = "none";
    }
}
