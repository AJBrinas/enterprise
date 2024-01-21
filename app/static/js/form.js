
function showAdditionalFieldsOccupation() {
    var Occupation = document.getElementById("occupation").value;
    var additionalFieldsEmployed = document.getElementById("additionalFieldsEmployed");
    var additionalFieldsStudent = document.getElementById("additionalFieldsStudent");

    if (Occupation === "employed") {
        additionalFieldsEmployed.style.display = "block";
        additionalFieldsStudent.style.display = "none";
    } else if (Occupation === "student") {
        additionalFieldsStudent.style.display = "block";
        additionalFieldsEmployed.style.display = "none";
    } else {
        additionalFieldsEmployed.style.display = "none";
        additionalFieldsStudent.style.display = "none";
    }
}

function toggleFields() {
    var educationLevel = document.getElementById("educationLevel").value;
    if (educationLevel === "elementary") {
        document.getElementById("elementaryFields").style.display = "block";
        document.getElementById("highSchoolFields").style.display = "none";
        document.getElementById("seniorHighSchoolFields").style.display = "none";
        document.getElementById("CollegeFields").style.display = "none";
    } else if (educationLevel === "highSchool") {
        document.getElementById("elementaryFields").style.display = "none";
        document.getElementById("highSchoolFields").style.display = "block";
        document.getElementById("seniorHighSchoolFields").style.display = "none";
        document.getElementById("CollegeFields").style.display = "none";
    } else if (educationLevel === "seniorHighSchool") {
        document.getElementById("elementaryFields").style.display = "none";
        document.getElementById("highSchoolFields").style.display = "none";
        document.getElementById("seniorHighSchoolFields").style.display = "block";
        document.getElementById("CollegeFields").style.display = "none";
    } else if (educationLevel === "college") {
        document.getElementById("elementaryFields").style.display = "none";
        document.getElementById("highSchoolFields").style.display = "none";
        document.getElementById("seniorHighSchoolFields").style.display = "none";
        document.getElementById("CollegeFields").style.display = "block";
    } else {
        document.getElementById("elementaryFields").style.display = "none";
        document.getElementById("highSchoolFields").style.display = "none";
        document.getElementById("seniorHighSchoolFields").style.display = "none";
        document.getElementById("CollegeFields").style.display = "none";
    }
}

function Ethnicityfunction(){
    
    var indigenous = document.getElementById("is_indigenous").value;
    if (indigenous === "Yes") {
        document.getElementById("indigenousYes").style.display = "block";
    } else{
        document.getElementById("indigenousYes").style.display = "none";
    }
}


function RegisteredVoter(){
    
    var voter = document.getElementById("voter").value;
    if (voter === "Yes_registered") {
        document.getElementById("RegisteredYes").style.display = "block";
    } else{
        document.getElementById("RegisteredYes").style.display = "none";
    }
}

function Disabilityfunction(){
    
    var voter = document.getElementById("is_disability").value;
    if (voter === "disability_Yes") {
        document.getElementById("disabilityYes").style.display = "block";
    } else{
        document.getElementById("disabilityYes").style.display = "none";
    }
}