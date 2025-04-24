<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>Анкета разработчика</title>
  <style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #f5f7fa;
        margin: 0;
        padding: 20px;
        color: #333;
    }

    .container {
        max-width: 600px;
        margin: 0 auto;
        background: white;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    h1 {
        text-align: center;
        color: #2c3e50;
        margin-bottom: 20px;
    }
    label {
        display: block;
        margin: 15px 0 5px;
        font-weight: bold;
        color: #34495e;
    }

    input[type="text"],
    input[type="tel"],
    input[type="email"],
    input[type="date"],
    select,
    textarea {
        width: 100%;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 5px;
        font-size: 16px;
        box-sizing: border-box;
    }

    select[multiple] {
        height: 120px;
    }
    
    .radio-group, .checkbox-group {
        margin: 10px 0;
    }

    .radio-group label, .checkbox-group label {
  
        display: inline-block;
  
        margin-right: 15px;
  
        font-weight: normal;

    }

    button {
        background: #3498db;
        color: white;
        border: none;
        padding: 12px 20px;
        font-size: 16px;
        border-radius: 5px;
        cursor: pointer;
        width: 100%;
        margin-top: 20px;
        transition: background 0.3s;
    }

    button:hover {
        background: #2980b9;
    }

    .error {
        color: #e74c3c;
        margin: 5px 0;
        font-size: 14px;
    }

    .success {
        color: #27ae60;
        text-align: center;
        margin: 20px 0;
        font-weight: bold;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Анкета разработчика</h1>
    
    <?php if (!empty($_GET['save'])): ?>
      <div class="success">Ваши данные успешно сохранены!</div>
    <?php endif; ?>

    <form action="index.php" method="POST">
    <label>ФИО*:</label>
    <input type="text" name="fio" required pattern="[А-Яа-яЁёA-Za-z\s]+" maxlength="150">

    <label>Телефон*:</label>
    <input type="tel" name="phone" required pattern="[\+\d\s\-]+">

    <label>Email*:</label>
    <input type="email" name="email" required>

    <label>Дата рождения*:</label>
    <input type="date" name="birth_date" required>

    <label>Пол*:</label>
    <label><input type="radio" name="gender" value="male" required> Мужской</label>
    <label><input type="radio" name="gender" value="female"> Женский</label>
    <label><input type="radio" name="gender" value="other"> Другой</label>

    <label>Любимый язык программирования* (выберите один или несколько):</label>
    <select name="languages[]" multiple="multiple" required>
      <option value="1">Pascal</option>
      <option value="2">C</option>
      <option value="3">C++</option>
      <option value="4">JavaScript</option>
      <option value="5">PHP</option>
      <option value="6">Python</option>
      <option value="7">Java</option>
      <option value="8">Haskell</option>
      <option value="9">Clojure</option>
      <option value="10">Prolog</option>
      <option value="11">Scala</option>
      <option value="12">Go</option>
    </select>

    <label>Биография:</label>
    <textarea name="bio" rows="5"></textarea>

    <label>
      <input type="checkbox" name="agree" required>
      С контрактом ознакомлен(а)*
    </label>

    <button type="submit">Сохранить</button>
    </form>
  </div>
</body>
</html>