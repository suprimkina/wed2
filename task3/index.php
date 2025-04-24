<?php
header('Content-Type: text/html; charset=UTF-8');

if ($_SERVER['REQUEST_METHOD'] == 'GET') {
  if (!empty($_GET['save'])) {
    echo '<div class="success">Данные сохранены!</div>';
  }
  include('form.php');
  exit();
}

// Валидация
$errors = [];
$fields = [
  'fio' => '/^[А-Яа-яЁёA-Za-z\s]{1,150}$/u',
  'phone' => '/^[\+\d\s\-]{5,20}$/',
  'email' => '/^[^@\s]+@[^@\s]+\.[^@\s]+$/',
  'birth_date' => '/^\d{4}-\d{2}-\d{2}$/',
  'gender' => '/^(male|female|other)$/',
  'languages' => '', // Проверим отдельно
  'agree' => '/^on$/'
];

foreach ($fields as $field => $pattern) {
  if (empty($_POST[$field])) {
    $errors[] = "Поле $field обязательно для заполнения.";
  } elseif ($pattern && !preg_match($pattern, $_POST[$field])) {
    $errors[] = "Некорректное значение поля $field.";
  }
}

// Проверка языков
if (empty($_POST['languages']) || !is_array($_POST['languages'])) {
  $errors[] = "Выберите хотя бы один язык программирования.";
}

if ($errors) {
  echo '<div class="error">' . implode('<br>', $errors) . '</div>';
  include('form.php');
  exit();
}

// Подключение к БД
$user = 'u67443'; 
$pass = '3234547';
$db = new PDO('mysql:host=localhost;dbname=u67443', $user, $pass, [
  PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION
]);

try {
  // Сохраняем заявку
  $stmt = $db->prepare("
    INSERT INTO application (fio, phone, email, birth_date, gender, bio, agree)
    VALUES (:fio, :phone, :email, :birth_date, :gender, :bio, 1)
  ");
  $stmt->execute([
    'fio' => $_POST['fio'],
    'phone' => $_POST['phone'],
    'email' => $_POST['email'],
    'birth_date' => $_POST['birth_date'],
    'gender' => $_POST['gender'],
    'bio' => $_POST['bio']
  ]);

  // Сохраняем выбранные языки
  $app_id = $db->lastInsertId();
  $stmt = $db->prepare("INSERT INTO application_languages (app_id, lang_id) VALUES (?, ?)");

  foreach ($_POST['languages'] as $lang_id) {
    $stmt->execute([$app_id, $lang_id]);
  }

  header('Location: ?save=1');
} catch (PDOException $e) {
  echo '<div class="error">Ошибка базы данных: ' . $e->getMessage() . '</div>';
}