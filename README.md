# 🧮 Hamming Code Simulator

This project is a Python-based simulation tool that demonstrates how **Hamming Code** works for **error detection and correction**. It provides a simple graphical user interface using `Tkinter`, allowing users to input binary data, generate Hamming codes, introduce bit errors, and detect/correct them using syndrome calculation.

---

## 🚀 Features

- Generate Hamming Code from 4, 8, or 16-bit binary data
- Simulate bit errors by flipping a selected bit
- Detect and correct single-bit errors
- Interactive GUI using Python's `tkinter`

---

## 📦 Requirements

- Python 3.x

> No external libraries required – only built-in `tkinter`.

---

## ▶️ How to Run

Clone the repository and run the main file:

```bash
git clone https://github.com/your-username/hamming-code-simulator.git
cd hamming-code-simulator
python hamming_gui.py
```

---

## 📸 GUI Screenshot (Optional)

You can add a screenshot like this:

```markdown
![App Screenshot](screenshot.png)
```

---

## 🧠 What is Hamming Code?

Hamming Code is an error-detection and correction method that uses parity bits at positions that are powers of two. It can detect and correct **single-bit errors**, making it highly efficient for data integrity in digital communication.

---


## 🛠️ Functions Overview

- `hammingkodhesapla(data, bit_uzunlugu)`: Generates the Hamming code
- `hata_ekleme(hamming_kod, hatali_indeks)`: Simulates a bit error
- `hata_tespit(hamming_kod)`: Calculates the syndrome
- `hata_duzeltme(hamming_kod, sendrom)`: Fixes the erroneous bit

---

## 👩‍💻 Author

**Zeynep Erarslan**  
Computer Engineering Student  
[GitHub Profile](https://github.com/zeyneperarslan)

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
