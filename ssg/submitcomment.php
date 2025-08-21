<?php
if (isset($_POST['submit'])) {
    $has_errors = false;
    $errors = array();
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
          $has_errors = true;
          array_push($errors, $errMsg);
        endif;
    else:
        $errMsg = 'Please click on the hCaptcha button.';
        $has_errors = true;
        array_push($errors, $errMsg);
    endif;

$url = $_POST["url"];
if (isset($url) && strlen($url) > 0) {
    if (!filter_var($url, FILTER_VALIDATE_URL)) {
    $urlErr = "Invalid URL format";
    $has_errors = true;
    array_push($errors, $urlErr);
    }
}

if ($has_errors) {
  // generate the output HTML
?>
<html>
    <head>
      <title>Comment Submission</title>
    </head>
<body>
  Errors were encountered when processing your comment submission:

  <ul>
<?php
foreach ($errors as $err) {
  echo "<li>" . $err . "</li>\n";
}
?>  
  </ul>
  <p>You can click "Back" to return to the comment form and try again.</p>
  <p>Why yes, this page IS super bare-bones!</p>
</body>
</html>
<?php
} else {

    // no errors, process the submission

    $newDate = date("D M d, Y G:i", $timeStamp);
    $new_message = array(
        "content" => $_POST['content'],
        "name" => $_POST['name'],
        "url" => $_POST['url'],
        "source_desc" => $_POST['source_desc'],
        "post_path" => $_POST['post_path'],
        "email" => $_POST['email'],
        "date" => $newDate
    );

    $filename = ".comments.json";

    if (filesize($filename) == 0) {
        $first_record = array($new_message);
        $data_to_save = $first_record;
    } else {
        $old_records = json_decode(file_get_contents($filename));
        array_push($old_records, $new_message);
        $data_to_save = $old_records;
    }
    
    $encoded_data = json_encode($data_to_save, JSON_PRETTY_PRINT);
    
    if (!file_put_contents($filename, $encoded_data, LOCK_EX)) {
        $testmsg = "Error storing message, please try again";
        echo $testmsg;
    } else {
        $testmsg =  "Message is stored successfully";
        header('Location: ' . $_POST['post_path'] . '#comment_success');
    }
}
}
?>
