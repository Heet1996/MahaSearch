<!-- mysql://b60ceb6df78c8a:de3eae1e@us-cdbr-iron-east-05.cleardb.net/heroku_a2e30006a7c23e2?reconnect=true -->
<?php
    $host = 'us-cdbr-iron-east-05.cleardb.net';
    $dbname = 'heroku_a2e30006a7c23e2';
    $username = 'b60ceb6df78c8a';
    $password = 'de3eae1e';
    
 
try {
    $conn = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    echo "Connected to $dbname at $host successfully.";
} catch (PDOException $pe) {
    die("Could not connect to the database $dbname :" . $pe->getMessage());
}
?>