# 🐍 Python Patterns & DSA Practice

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Stars](https://img.shields.io/github/stars/Vigilante120/Python_Patterns?style=social)
![Last Commit](https://img.shields.io/github/last-commit/Vigilante120/Python_Patterns)

**Master Python Programming Through Pattern Recognition, Data Structures, and Algorithmic Problem Solving**

[📚 Explore Repository](#-repository-structure) • [🚀 Getting Started](#-getting-started) • [💡 Features](#-features) • [🤝 Contributing](#-contributing)

</div>

---

## 🎯 About This Repository

Welcome to **Python_Patterns** — a comprehensive collection of Python implementations focusing on:
- **Pattern Printing**: Master loop logic through visual pattern recognition
- **Data Structures**: From basics to advanced structures (Linked Lists, Trees, HashMaps)
- **Algorithms**: Sorting, searching, recursion, and dynamic programming
- **Problem Solving**: LeetCode problems and competitive programming exercises

Whether you're a beginner learning Python fundamentals or an intermediate developer sharpening your DSA skills, this repository offers well-documented, practical examples to accelerate your learning journey.

---

## ✨ Features

- 📝 **Clean, Well-Documented Code** — Every file includes inline comments explaining the logic
- 🎓 **Beginner-Friendly** — Concepts explained from the ground up
- 🔄 **Regular Updates** — New patterns, problems, and solutions added frequently
- 🎨 **Pattern Recognition** — Visual learning through pattern printing exercises
- 💾 **Data Structures** — Complete implementations with examples
- 🧮 **Algorithm Practice** — Sorting algorithms, recursion, and more
- 🏆 **LeetCode Solutions** — Real interview questions solved

---

## 📂 Repository Structure

```
Python_Patterns/
│
├── 📁 patterns/              # Pattern printing exercises (triangles, diamonds, etc.)
├── 📁 arrays/                # Array manipulation and problems
├── 📁 linked_list/           # Singly Linked List implementations
├── 📁 doubly_linked_list/    # Doubly Linked List with various operations
├── 📁 hashing/               # Hashing concepts and implementations
├── 📁 hashmap/               # HashMap/Dictionary problems and solutions
├── 📁 recursion/             # Recursive problem solving
├── 📁 sorting_algo/          # Sorting algorithms (Bubble, Merge, Quick, etc.)
├── 📁 basic_math_py/         # Mathematical algorithms and number theory
├── 📁 leetcode/              # LeetCode problem solutions
├── 📁 json_intro/            # JSON handling in Python
└── 📁 slicing basic/         # Python slicing techniques
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.x** installed on your system
- A code editor (VS Code, PyCharm, Sublime Text, etc.)
- Basic understanding of Python syntax (variables, loops, functions)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vigilante120/Python_Patterns.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Python_Patterns
   ```

3. **Choose a topic and explore:**
   ```bash
   cd patterns
   python pattern_name.py
   ```

### Running Examples

Each folder contains standalone Python files. Simply run any file:

```bash
python filename.py
```

**Example:**
```bash
cd recursion
python factorial.py
```

---

## 📚 What You'll Learn

### 🔹 Pattern Printing
Build strong loop logic by creating:
- Stars, numbers, and character patterns
- Triangles, pyramids, and diamonds
- Hollow and solid shapes
- Complex nested loop patterns

### 🔹 Data Structures
- **Linked Lists**: Singly, doubly, circular implementations
- **Arrays**: Manipulation, searching, sorting
- **Hash Maps**: Frequency counting, two-sum problems
- **Trees & Graphs**: Coming soon!

### 🔹 Algorithms
- **Sorting**: Bubble, Selection, Insertion, Merge, Quick Sort
- **Searching**: Binary Search, Linear Search
- **Recursion**: Base cases, recursive thinking, backtracking
- **Mathematical**: GCD, LCM, Prime numbers, Palindromes

### 🔹 Problem Solving
- LeetCode easy to medium problems
- Array manipulation challenges
- String processing
- Two-pointer techniques

---

## 🎓 How to Use This Repository

### For Beginners:
1. Start with **patterns/** folder to understand loops
2. Move to **basic_math_py/** for algorithmic thinking
3. Progress to **arrays/** and **recursion/**
4. Practice with **leetcode/** problems

### For Intermediate Learners:
1. Jump to **linked_list/** or **doubly_linked_list/**
2. Explore **sorting_algo/** implementations
3. Challenge yourself with **leetcode/** solutions
4. Study **hashing/** and **hashmap/** techniques

### For Instructors:
- Use examples as teaching material
- Share specific files with students
- Fork and customize for your curriculum

---

## 💻 Example Code

### Pattern Printing
```python
# Right-angled triangle pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
```

### Linked List Implementation
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
```

---

## 🌟 Recent Updates

- ✅ Added Doubly Linked List palindrome checker
- ✅ Merge Sort implementation in sorting algorithms
- ✅ New pattern problems from Striver's A2Z DSA sheet
- ✅ JSON handling examples
- ✅ Enhanced recursion exercises

---

## 🤝 Contributing

Contributions are welcome! If you'd like to add new patterns, algorithms, or improvements:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📖 Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Striver's A2Z DSA Course](https://takeuforward.org/strivers-a2z-dsa-course/)
- [LeetCode](https://leetcode.com/)
- [GeeksforGeeks](https://www.geeksforgeeks.org/)

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Nishant Bhandari** ([@Vigilante120](https://github.com/Vigilante120))

- 🎓 Full-Stack Developer & Programming Instructor
- 💡 Passionate about teaching and problem-solving
- 🌱 Continuously learning and sharing knowledge

---

## ⭐ Show Your Support

If you find this repository helpful, please consider giving it a ⭐️!

**Happy Coding! 🚀**

---

<div align="center">

**[⬆ Back to Top](#-python-patterns--dsa-practice)**

</div>
