<!-- mysql://b60ceb6df78c8a:de3eae1e@us-cdbr-iron-east-05.cleardb.net/heroku_a2e30006a7c23e2?reconnect=true -->
<!-- mysql://b26e5c3445f854:92546290@us-cdbr-iron-east-05.cleardb.net/heroku_a2db3d44f93534b?reconnect=true -->
<?php
    $host = 'us-cdbr-iron-east-05.cleardb.net';
    $dbname = 'heroku_a2db3d44f93534b';
    $username = 'b26e5c3445f854';
    $password = '92546290';
    
 
try {
    $conn = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    echo "Connected to $dbname at $host successfully.";
} catch (PDOException $pe) {
    die("Could not connect to the database $dbname :" . $pe->getMessage());
}
?>