function showGrades() {
document.getElementById("grades").style.display = "block";
document.getElementById("attendance").style.display = "none";
document.getElementById("complaint").style.display = "none";
document.getElementById("schedule").style.display = "none";
document.getElementById("student").style.display = "none";

}

function showAttendance() {
document.getElementById("grades").style.display = "none";
document.getElementById("attendance").style.display = "block";
document.getElementById("complaint").style.display = "none";
document.getElementById("schedule").style.display = "none";
document.getElementById("student").style.display = "none";

}

function showComplaint() {
document.getElementById("grades").style.display = "none";
document.getElementById("attendance").style.display = "none";
document.getElementById("complaint").style.display = "block";
document.getElementById("schedule").style.display = "none";
document.getElementById("student").style.display = "none";

}

function showSchedule() {
document.getElementById("grades").style.display = "none";
document.getElementById("attendance").style.display = "none";
document.getElementById("complaint").style.display = "none";
document.getElementById("schedule").style.display = "block";
document.getElementById("student").style.display = "none";

}

function showStudent() {
document.getElementById("grades").style.display = "none";
document.getElementById("attendance").style.display = "none";
document.getElementById("complaint").style.display = "none";
document.getElementById("contact").style.display = "none";
document.getElementById("schedule").style.display = "none";
document.getElementById("student").style.display = "block";
}