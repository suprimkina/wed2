<?php
$ed_login = $_GET['user'];
$_SESSION['ed_login'] = $ed_login;
$all_names = ["fio", "telephone", "email", "bday", "sex", "langs", "biography"];
$errors = [];
if (isset($_GET['errors_flag'])) {
    $errors = unserialize($_COOKIE['errors']);
    $fields_data = unserialize($_COOKIE['incor_data']);
} else {
    $fields_data = get_user_fields_data($ed_login);
}
if (isset($_GET['success_flag'])) {
    $success_flag = true;
}
foreach ($all_names as $name) {
    if (!isset($fields_data[$name])) {
        if ($name == "langs") {
            $fields_data['langs'] = [];
        } else {
            $fields_data[$name] = "";
        }
    }
}
?>


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <script src="../../jquery.js" defer></script>
    <script src="scripts.js" defer></script>
    <link rel="stylesheet" type="text/css" href="../../style.css">
    <link rel="stylesheet" type="text/css" href="style.css">
    <link rel="shortcut icon" href="../../logo.png"/>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@100;200;300;400;500;600;700;800&display=swap"
          rel="stylesheet">
    <title>Задание 6</title>
</head>

<body>
<header>
    <nav class="header-logo">
        <img class="header-logo" src="../../logo.png" alt="Logo">
    </nav>
    <nav class="header-info">
        <h2 class="header-title">$$$ website?</h2>
        <h3 class="header-task">Задание 6</h3>
    </nav>

</header>

<aside>
    <nav class="aside-link">
        <a href="index.php">Админ-панель</a>
    </nav>
</aside>

<main>
    <div class="tasks" id="div_form">
        <form method="post" id="form">
            <h2 id="h1-form" class="black">Редактировать форму</h2>
            <div class="div-input">
                Пользователь:
                <?php echo $ed_login ?>
            </div>
            <?php if (!empty($errors)): ?>
                <div class="div-result">
                    <?php foreach ($errors as $key => $val): ?>
                        <div class="error-color label-center">
                            <?php echo $val; ?>
                        </div>
                    <?php endforeach; ?>
                </div>
            <?php elseif (isset($success_flag)): ?>
                <div class="div-result">
                    <p class="success-color">Данные успешно изменены, спасибо!</p>
                </div>
            <?php endif; ?>
            <?php echo_form($all_names, $fields_data, $errors); ?>
            <div class="label-center">
                <input id="contract" type="checkbox" name="contract" value="1">
                <label id="for-contract" class="black" for="contract">С контрактом ознакомлен</label>
            </div>

            <div class="div-input">
                <button name="admin_edit_form" value="True">Отправить</button>
            </div>
            <div class="div-input">
                <button name="delete_user" value="True">Удалить пользователя</button>
            </div>
        </form>
    </div>
</main>

<footer>
    <p class=" text_in_footer">created by</p>
    <h3 class=" text_in_footer">Анна Супрун</h3>
</footer>
</body>

</html>
