<!DOCTYPE html>


<html lang="en">
<head>
    <!-- add external php -->
    <?php

    // redirecting to login page

        include 'log-in.php';

    ?>

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brute Test</title>
</head>
<style>
    body{
        text-align: center;
        margin-top: 113px;
    }
    .sb{
        margin-right: 270px;
    }
    .as{
    margin-top: 360px;
        }
    a{
    margin: 30px;
    text-decoration: none;
    }
</style>
<body>
    <div class="Container">

        <!-- simple Form With Username && Password Parameters -->

        <form  name="login" method="post">
            <label for="uname">Enter your User Name : </label>
            <input type="text" name="username" id="username"><br><br>
            <label for="password">Enter Your Password : </label>
            <input type="password" name="password"><br><br>
            <div class="sb">
            <input type="submit" value="login" name="submit">
            </div>
        </form>
    </div>
    <div class="as">
    <a href="https://github.com/alisharifyy">Github : alisharifi</a>
    <a href="https://github.com/Ali-Moattarirad">Github : ali Moatttari rad</a>
    </div>
</body>
</html>