# 🗂️ File Organizer

A small Python utility that automatically organizes messy folders based on file extensions.

This is my **very first Python project** 🐍 — and I wanted to build something that solves a real problem I have on my own desktop:

> **Messy folders. 🤭**

My Downloads folder had become a beautiful disaster of PDFs, images, ZIP files, documents, videos, and random files all living together.

So instead of manually cleaning it up, I decided to make Python do the boring part for me.

And this is where **File Organizer** was born.

---

## ✨ What does it do?

You give the program a folder path, and it:

1. Looks at the files inside the folder.
2. Checks each file's extension.
3. Finds the appropriate category.
4. Creates the category folder if it doesn't already exist.
5. Moves the file into that folder.

For example:

```text
Before:

Downloads/
├── resume.pdf
├── vacation.jpg
├── project.zip
├── data.csv
├── song.mp3
├── movie.mp4
└── notes.txt
```

After running the organizer:

```text
Downloads/
├── PDFs/
│   └── resume.pdf
├── Images/
│   └── vacation.jpg
├── Archives/
│   └── project.zip
├── Data/
│   └── data.csv
├── Music/
│   └── song.mp3
├── Videos/
│   └── movie.mp4
└── Documents/
    └── notes.txt
```

Much less chaos. 😌

---

## 🚀 Getting Started

### Requirements

- Python 3
- No external Python packages are currently required.

The project uses Python's built-in modules:

- `sys`
- `pathlib`

### Clone the repository

```bash
git clone https://github.com/Farzane2630/file-organizer.git
cd file-organizer
```

### Run the program

Pass the folder you want to organize as a command-line argument:

```bash
python3 fileOrg.py /path/to/your/folder
```

For example:

```bash
python3 fileOrg.py ~/Downloads
```

On Windows, you can provide the appropriate folder path:

```bash
python fileOrg.py "C:\Users\YourName\Downloads"
```

The program will create the necessary category folders and move supported files into them.

---

## 📁 Supported File Types

The current version organizes files into these categories:

| Extension                               | Category    |
| --------------------------------------- | ----------- |
| `.pdf`                                  | PDFs        |
| `.png`, `.jpg`, `.jpeg`, `.gif`         | Images      |
| `.doc`, `.docx`, `.html`, `.txt`, `.md` | Documents   |
| `.csv`, `.xlsx`, `.iso`                 | Data        |
| `.zip`, `.rar`                          | Archives    |
| `.exe`                                  | Executables |
| `.mp3`, `.wav`                          | Music       |
| `.mp4`, `.avi`, `.flv`, `.wmv`          | Videos      |

The extension matching is case-insensitive, so `.JPG` and `.jpg` are treated the same way.

Files with extensions that aren't currently supported are left untouched.

---

## 🧠 Why I Built This

This project started as a Python learning exercise, but I wanted my first program to solve an actual problem rather than just print `"Hello World"` for the 47th time. 😅

I'm currently learning Python and exploring the world of AI and security, so I wanted to start building small practical tools along the way.

And honestly...

**My messy Downloads folder was becoming a security threat to my sanity. 🤭**

So I decided to automate it.

---

## 🛠️ Current Status

This is an early version and **actively evolving**.

The core functionality works, but there are plenty of things I'd like to improve.

Some ideas on the roadmap:

- [ ] Better command-line argument validation
- [ ] Handle duplicate filenames safely
- [ ] Add an `Others` category for unsupported file types
- [ ] Add a dry-run mode
- [ ] Add a confirmation option before moving files
- [ ] Add logging
- [ ] Add more file extensions
- [ ] Allow users to customize categories
- [ ] Improve error handling
- [ ] Add recursive folder organization
- [ ] Add configuration support
- [ ] Add tests
- [ ] Maybe build a simple GUI 👀

And probably many more ideas once I start using it more.

---

## 🤝 Contributions Welcome!

This project is intentionally open to improvements.

If you have an idea for a useful feature, a cleaner implementation, a bug fix, or just a cool idea for making file organization smarter, **I'd love to see it.** 🚀

### How to contribute

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature/my-cool-feature
```

3. Make your changes.
4. Test your changes.
5. Commit them:

```bash
git commit -m "Add my cool feature"
```

6. Push your branch:

```bash
git push origin feature/my-cool-feature
```

7. Open a Pull Request.

Beginner-friendly contributions are absolutely welcome. You don't need to build the next revolutionary file-management system. 😄

---

## 💡 Ideas for Contributors

Not sure where to start?

Here are some things you could work on:

- Add support for more file extensions
- Improve duplicate-file handling
- Add a `--dry-run` option
- Add colored terminal output
- Add better error messages
- Add tests
- Improve the CLI experience
- Add configurable folder categories
- Add support for more operating systems
- Build a GUI
- Suggest a completely different approach!

If you're learning Python too, feel free to use this project as a playground.

---

## ⚠️ A Small Warning

This program **moves files on your filesystem**.

Please test it on a temporary/test folder before pointing it at an important directory.

For example, create:

```text
test-organizer/
├── test.pdf
├── photo.jpg
└── example.zip
```

and run the program there first.

Because once Python starts moving your files around...

**Python does not care about your emotional attachment to that Downloads folder. 😂**

---

## 📚 What I Learned

Building this tiny project has already introduced me to several Python concepts:

- Command-line arguments
- Dictionaries
- `try` / `except`
- Loops
- Conditional logic
- Strings and string methods
- `pathlib`
- Working with files and directories
- File extensions
- Creating directories
- Moving files
- Thinking about edge cases

And that's exactly why I wanted to build something instead of only following tutorials.

There is still a lot to improve, and I'll be working on it soon. 🐍

---

## ⭐ If You Like It

If this little project helps you clean up your digital chaos, feel free to ⭐ the repository.

And if you have an idea for making it better, open an issue or submit a pull request.

Let's make messy folders a little less messy. 😅

---

**Built with Python 🐍 and a slightly chaotic Downloads folder.**
