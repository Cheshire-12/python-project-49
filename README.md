# Brain Games 🧠

**Brain Games** is a collection of simple command-line mathematical games designed as an educational project. The project is structured as a highly modular Python package, featuring a universal game engine that powers all five available games.

---

## ✨ Games and Rules

The project includes five brain-training games.

**Rules:** To win, you must provide **three** correct answers in a row. An incorrect answer will immediately end the game.

| Game | Description | Launch Command |
| :--- | :--- | :--- |
| **Welcome** | User greeting and introduction. | `brain-games` |
| **Parity Check** | Guess whether the number is even (`yes` or `no`). | `brain-even` |
| **Calculator** | Calculate the result of a random mathematical expression. | `brain-calc` |
| **GCD** | Find the greatest common divisor of two numbers. | `brain-gcd` |
| **Progression** | Identify the missing number in an arithmetic progression. | `brain-progression` |
| **Is Prime?** | Guess whether the number is prime (`yes` or `no`). | `brain-prime` |

---

## 🛠️ Installation and Setup

The project requires **Python 3.12 or newer** and the **`uv`** package manager/build tool for correct installation.

### 1. Installation

To install the package as a command-line tool, you must complete the full cycle: dependency synchronization, **wheel file creation**, and final installation. These steps are automated by the `make install-games` command:

```bash
# Clone the repository
git clone [https://github.com/Cheshire-12/python-project-49.git](https://github.com/Cheshire-12/python-project-49.git)
cd python-project-49

# Executes: uv sync, uv build, uv tool install dist/*.whl
make install-games
```
 ### 2. Running a Game
You can start any game by typing its corresponding command.
```bash
brain-calc
```

### Game: "Parity Check"
[![asciicast](https://asciinema.org/a/IlTxJPW7mvdKo2OIxgMhK3woq.svg)](https://asciinema.org/a/IlTxJPW7mvdKo2OIxgMhK3woq)

### Game: "Calculator"
[![asciicast](https://asciinema.org/a/Fv5uA4ZJx22ZXqjgTMLObpDGq.svg)](https://asciinema.org/a/Fv5uA4ZJx22ZXqjgTMLObpDGq)

### Game: "Greatest Common Divisor (GCD)"
[![asciicast](https://asciinema.org/a/ZgzszcouUeXlFZvpmR4rsugLm.svg)](https://asciinema.org/a/ZgzszcouUeXlFZvpmR4rsugLm)

### Game: "Arithmetic Progression"
[![asciicast](https://asciinema.org/a/5xNE302Kgqa2D6VYizzAr0asK.svg)](https://asciinema.org/a/5xNE302Kgqa2D6VYizzAr0asK)

### Game: "Is a number prime?"
[![asciicast](https://asciinema.org/a/QT7OfDWcYaG7Htl7gYAS54t8X.svg)](https://asciinema.org/a/QT7OfDWcYaG7Htl7gYAS54t8X)

## 📊 Project Status

| Tool | Status |
| :--- | :--- |
| **Hexlet Tests** | [![Actions Status](https://github.com/Cheshire-12/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Cheshire-12/python-project-49/actions) |
| **SonarCloud Quality Gate** | [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Cheshire-12_python-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Cheshire-12_python-project-49) |
| **Code Smells** | [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Cheshire-12_python-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Cheshire-12_python-project-49) |
| **Maintainability Rating** | [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Cheshire-12_python-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Cheshire-12_python-project-49) |
| **Vulnerabilities** | [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Cheshire-12_python-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Cheshire-12_python-project-49) |