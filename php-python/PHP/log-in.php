<?php
// Using Post Method For Data collecting From user



if (isset($_POST['submit'])) {
    $user=$_POST['username'];
    $pass=$_POST['password'];

// Checking if Username & Password are Match

    if ($user == "admin" and $pass== "patrol") {

        // Redirecting To Welcome Page If Username and Password is corecct
         header("Location: ./welcome.php");
        }
        else {
            
            // Redirecting To Error Page If Username and Password Is Incorecct
            
        header("Location: ./error.php");
    }
}
?>