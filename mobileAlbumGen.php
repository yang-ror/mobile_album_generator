<!-- =============================================================================
 mobileAlbumgen.php
 project: mobile_album_generator
 author: Zifan Yang
 date created: 2021-01-25
 last modified: 2021-03-04
 change log:
    2021-02-14
        1. no longer need to set the get variable to display the home menu
        2. fix index number not incrementing
    2021-03-04
        1. optimized for desktop view
============================================================================= -->

<!doctype html>
<html lang="en">
    <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Mobile Album</title>
        <style>
            html{
                width: 100%;
            }

            body{
                margin-left: auto;
                margin-right: auto;
                max-width: 800px;
            }
        </style>
    </head>
    <body>
        <?php
            //scan current directory for any picture folder and display a link to them
            $display = $_GET["display"];
            if(!isset($display)){
                $dir = './';
                $i = 1;
                foreach (scandir($dir) as $item) {
                    if ($item[0] === '.') continue;
                    if (!is_dir("./$item")) continue;

					echo "<label>$i. </label>";
                    echo "<a href='index.php?display=$item'>$item</a>";
                    echo "<br>";
                    $i++;
				}
            }
            //reads the name of a sub-directory then display all the pictures in it.
            else{
                $dir = './' . $display . '/';
                foreach (scandir($dir) as $item) {
                    if ($item[0] === '.') continue;
                    if (is_dir("./$item")) continue;

                    echo '<img src="' . $dir . $item . '" width="100%" border="0" style="display:block;">';
                    // echo "<br>";
				}
            }
        ?>
    </body>
</html>
