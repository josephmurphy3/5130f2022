<!DOCTYPE html PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html>
<body>
Facts Noted <br>
Your Current Location: <?php echo $_POST["name"]; ?> <br>
Your Hometown: <?php echo $_POST["name1"]; ?> <br>
Your Dream Location: <?php echo $_POST["name2"]; ?> <br>
Your Family is from: <?php echo $_POST["name3"]; ?> <br>
<h1>
I want to know more Facts about you!
</h1>
<form action="tab2.php" method="post">
                Your Place of Birth: <input type="text" name="name">
                Your Current Hometown: <input type="text" name="name1">
                Your Dream Hometown: <input type="text" name="name2">
                Your Significant Others Hometown: <input type="text" name="name3">
                <input type="submit">
        </form>
<br>
<a href="index.html">Home</a>
</body>
</html>

