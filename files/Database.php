<?php
/** <Author> Joshua Standiford </Author>
 ** <Date Modified> 7/27/2016 </Date Modified>
 ** <Description>
 ** Database.php acts as a class file used for database functions. 
 ** Collection of connection methods and helper functions populate this 
 ** file
 ** </Description>
 */
class DB {

	/* Constructor for Database class
	 *
	 *
	 */
    function __construct() {

    }


    /**
     * Desc: This function connects to the database
     * Called on creation of the database class
     * Preconditions: None
     * Postconditions: Either a new PDO connection is returned or null
     * @return null|PDO
     */
    private function connect(){
        $cred = parse_ini_file(dirname(__FILE__) . "/../db_key.ini");

        try{
		    $conn = new PDO("mysql:host=$cred[servername];dbname=$cred[dbname]", $cred['username'], $cred['password']);

		    // set the PDO error mode to exception
		    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		    return $conn;
        }
		catch(PDOException $e){
		   	echo "Connection failed: " . $e->getMessage();
        }
		return null;
	}

    /**
     * @return bool
     * @desc
     * Return a test to see if you're able to connect to the function above
     */
    public function testConnection(){
        return !is_null($this->connect());
    }

    public function registerUser($data){
        $table = "account";

        try {
            $conn = $this->connect();

            $stmt = $conn->prepare("INSERT INTO $table (username, password, email)
                                VALUES (:username, :password, :email)");
            $stmt->bindParam(':username', $username);
            $stmt->bindParam(':password', $password);
            $stmt->bindParam(':email', $email);

            $username = $data["username"];
            $password = $data["password"];
            $email = $data["email"];

            $stmt->execute();

            $conn = null;
            return true;
        }
        catch(PDOException $e){
            echo $e;
            return false;
        }

    }

    public function checkAccountExists($id){
        $table = "account";

        try {
            $conn = $this->connect();
            $stmt = $conn->prepare("SELECT 1 FROM $table WHERE username = '" . $id . "'");
            $stmt->execute();
            $result = $stmt->setFetchMode(PDO::FETCH_ASSOC);
            $result = $stmt->fetchAll();
            $conn = null;

            return $result;
        }
        catch(PDOException $e){
            echo $e;
            return null;
        }
    }

    /**
     * @param $user
     * @param $pass
     * @return array|bool
     */
    public function authorize($ID, $pass){
        $table = "account";
        try {
            $conn = $this->connect();
            $stmt = $conn->prepare("select password from $table WHERE username = '" . $ID . "'");
            $stmt->execute();
            $result = $stmt->setFetchMode(PDO::FETCH_ASSOC);

            $result = $stmt->fetchAll();

            $conn = null;

            return $result[0]["password"];
        }
        catch(PDOException $e){
            echo $e;
            return false;
        }
    }

    public function isOnline(){
        $table = "account_online";

        try {
            $conn = $this->connect();
            $stmt = $conn->prepare("SELECT timestamp FROM $table WHERE username = 'asd'");
            $stmt->execute();
            $result = $stmt->setFetchMode(PDO::FETCH_ASSOC);
            $result = $stmt->fetchAll();
            $conn = null;

            $seconds = strtotime(date("Y-m-d H:i:s")) - strtotime($result[0]['timestamp']);
            if($seconds >= 11){
                return 0;
            }
            return 1;
        }
        catch(PDOException $e){
            echo $e;
            return null;
        }
    }

    public function userOnline($user){
        $table = "account_online";
        $time = date("Y-m-d H:i:s");
        echo $time;
        try {
            $conn = $this->connect();

            $stmt = $conn->prepare("INSERT INTO $table (username, timestamp)
                                VALUES (:username, :timestamp)
                                ON DUPLICATE KEY UPDATE timestamp=:timestamp ");
            $stmt->bindParam(':username', $username);
            $stmt->bindParam(':timestamp', $timestamp);

            $username = $user;
            $timestamp = $time;

            $stmt->execute();

            $conn = null;
            return true;
        }
        catch(PDOException $e){
            echo $e;
            return false;
        }
    }

}