<!-- =============================================================================
 mobileAlbumgen.php
 project: mobile_album_generator
 author: Zifan Yang
 date created: 2021-01-25
 last modified: 2021-01-25
============================================================================= -->

<!doctype html>
<html lang="en">
    <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Mobile Album</title>
    </head>
    <body>
        <?php
            //scan current directory for any picture folder and display a link to them
            $display = $_GET["display"];
            if($display == 'home'){
                $dir = './';
                $i = 1;
                foreach (scandir($dir) as $item) {
                    if ($item[0] === '.') continue;
                    if (!is_dir("./$item")) continue;

					echo "<label>$i. </label>";
                    echo "<a href='index.php?display=$item'>$item</a>";
                    echo "<br>";
				}
            }
            //reads the name of a sub-directory then display all the pictures in it.
            else{
                $dir = './' . $display . '/';
                foreach (scandir($dir) as $item) {
                    if ($item[0] === '.') continue;
                    if (is_dir("./$item")) continue;

                    echo '<img src="' . $dir . $item . '" width="100%" border="0" style="display:block;">';
                    echo "<br>";
				}
            }
        ?>
    </body>
</html>