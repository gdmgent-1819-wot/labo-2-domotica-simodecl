firebase.auth().onAuthStateChanged((user) => {

    const userEl = document.querySelector(".user");
    const loginEl = document.querySelector(".login");
    const userIntro = document.querySelector(".userIntro");

    if (user) {
        // User is signed in.

        userEl.style.display = "block";
        loginEl.style.display = "none";

        var user = firebase.auth().currentUser;

        if(user != null){

        var email_id = user.email;
        userIntro.innerHTML = "Welcome User : " + email_id;

        }

    } else {
        // No user is signed in.

        userEl.style.display = "none";
        loginEl.style.display = "block";

    }
});
  
  
const login = () => {

const userEmail = document.getElementById("email_field").value;
const userPass = document.getElementById("password_field").value;

firebase.auth().signInWithEmailAndPassword(userEmail, userPass).catch((error) => {
    // Handle Errors here.
    var errorCode = error.code;
    var errorMessage = error.message;

    window.alert("Error : " + errorMessage);

    // ...
});

}

const logout = () => {
firebase.auth().signOut();
}
