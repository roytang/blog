<?php
if(isset($_POST['submit'])):
    if(isset($_POST['h-captcha-response']) && !empty($_POST['h-captcha-response'])):
        // get verify response
        $data = array(
              'secret' => $_SERVER['RECAPTCHA_SECRET'],
              'response' => $_POST['h-captcha-response']
          );
        $verify = curl_init();
        curl_setopt($verify, CURLOPT_URL,   "https://hcaptcha.com/siteverify");
        curl_setopt($verify, CURLOPT_POST, true);
        curl_setopt($verify, CURLOPT_POSTFIELDS, http_build_query($data));
        curl_setopt($verify, CURLOPT_RETURNTRANSFER, true);
        $verifyResponse = curl_exec($verify);
        $responseData = json_decode($verifyResponse);
        if($responseData->success):
            $succMsg = 'Your contact request has been submitted successfully.';
        else:
            $errMsg = 'hCaptcha verification failed. Please try again.';
        endif;
    else:
        $errMsg = 'Please click on the hCaptcha button.';
    endif;

$email = $_POST["email"];
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
  $emailErr = "Invalid email format";
  echo $emailErr;
}


	   $new_message = array(
	      "content" => $_POST['content'],
	      "name" => $_POST['name'],
	      "url" => $_POST['url'],
	      "source_desc" => $_POST['source_desc'],
	      "post_path" => $_POST['post_path'],
	      "email" => $_POST['email']
	   );

     $filename = ".messages.json";

	   if(filesize($filename) == 0){
	      $first_record = array($new_message);
	      $data_to_save = $first_record;
	   }else{
	      $old_records = json_decode(file_get_contents($filename));
	      array_push($old_records, $new_message);
	      $data_to_save = $old_records;
	   }
	 
	   $encoded_data = json_encode($data_to_save, JSON_PRETTY_PRINT);
	 
	   if(!file_put_contents($filename, $encoded_data, LOCK_EX)){
	      $testmsg = "Error storing message, please try again";
        echo $testmsg;
	   }else{
	      $testmsg =  "Message is stored successfully";
        echo $testmsg;
	   }
endif;
?>
<html>
    <head>
      <title>Using hCaptcha with PHP</title>
       <script src="https://www.hCaptcha.com/1/api.js" async defer></script>
    </head>
    <body>
    <div>
    <h2>Contact Form</h2>
        <?php if(!empty($errMsg)): ?><div class="errMsg"><?php echo $errMsg; ?></div><?php endif; ?>
        <?php if(!empty($succMsg)): ?><div class="succMsg"><?php echo $succMsg; ?></div><?php endif; ?>
    <div class="clear"> </div>
  </div>

  <?php echo @$testmsg; ?>
  POST DUMP: <?php var_dump($_POST); ?>
  </body>
</html>