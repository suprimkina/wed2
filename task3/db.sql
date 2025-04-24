CREATE TABLE application (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  fio VARCHAR(150) NOT NULL,
  phone VARCHAR(20) NOT NULL,
  email VARCHAR(100) NOT NULL,
  birth_date DATE NOT NULL,
  gender ENUM('male', 'female', 'other') NOT NULL,
  bio TEXT,
  agree TINYINT(1) NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE programming_languages (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL UNIQUE,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE application_languages (
  app_id INT UNSIGNED NOT NULL,
  lang_id INT UNSIGNED NOT NULL,
  FOREIGN KEY (app_id) REFERENCES application(id) ON DELETE CASCADE,
  FOREIGN KEY (lang_id) REFERENCES programming_languages(id) ON DELETE CASCADE,
  PRIMARY KEY (app_id, lang_id)
);

INSERT INTO programming_languages (name) VALUES 
('Pascal'), ('C'), ('C++'), ('JavaScript'), ('PHP'),
('Python'), ('Java'), ('Haskell'), ('Clojure'), ('Prolog'),
('Scala'), ('Go');