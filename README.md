# Text-Editor-CLI: A Python Command-Line Editor with Word Analysis and Editing Features

Release assets are available at https://github.com/Selahaddin67/Text-Editor-CLI/releases

[![Release assets](https://img.shields.io/github/v/release/Selahaddin67/Text-Editor-CLI?style=for-the-badge)](https://github.com/Selahaddin67/Text-Editor-CLI/releases)

A lightweight, open-source command-line editor for text files. It combines fast editing with insightful word analysis. Designed for beginners and seasoned users alike, this tool helps you edit text efficiently, count words, analyze word usage, and process files directly from the terminal.

Emoji-friendly, beginner-friendly, and built for learning. It runs as a terminal app, supports multiple platforms, and integrates with common developer workflows. You can use it to draft notes, prepare documents, or analyze large text corpora right from your shell.

Table of contents
- Why use Text-Editor-CLI
- Features
- Quick start
- How it works
- Installation
- Basic usage
- Word analysis and editing commands
- File processing and formats
- Advanced editing features
- Customization and configuration
- Testing and quality
- Docker and virtualization
- Accessibility and usability
- Contributing
- Roadmap
- License and credits

Why use Text-Editor-CLI 🧭
Text-Editor-CLI gives you a straightforward way to work with text in the terminal. It focuses on clarity and speed. You can open a file, make edits, and run simple analyses without leaving the command line. The tool emphasizes readability and learnability, making it a good fit for coursework, coding boot camps, or solo projects.

Features ✨
- Lightweight command-line interface that runs in shells like Bash, Zsh, and PowerShell.
- Fast text editing: insert, delete, replace, copy, and paste in a linear, predictable way.
- Word analysis: word count, unique word tally, most frequent words, and basic readability metrics.
- Search and replace with case sensitivity options.
- Jump to specific lines and navigate by character, word, or line.
- File processing: read and write plain text files (.txt) and support simple document formats.
- Export and import options for basic interoperability with other tools.
- Interactive help and inline tips to guide new users.
- Configurable key bindings and simple preferences.
- Cross-platform support: Linux, macOS, Windows.

Quick start 🚀
- Install the release assets and run the program from your shell.
- Use the built-in help to learn commands quickly.
- Open a text file, edit, and analyze in a single session.

How it works 🔬
Text-Editor-CLI is built to be transparent. It stores edits in memory and writes changes back to disk when you save. Word analysis runs over the current buffer or the loaded file, giving you immediate feedback on word usage and structure. The design favors explicit actions over magic, which helps students and new developers learn how a text editor operates under the hood.

Installation and setup 🛠️
There are two common ways to get started. The recommended approach is to install via the official release assets, which provide a ready-to-run binary or installer for your platform. The releases page is the central source for stable builds, updates, and docs. See the releases page for the exact installer file names for your OS.

- Prerequisites
  - Python 3.8+ if you choose to install from source (or use a Python package in a virtual environment).
  - Git for cloning the repository if you want to build from source.
  - A POSIX-like shell for best experience on Linux/macOS; Windows users can use PowerShell or Windows Subsystem for Linux (WSL) for a smoother experience.

- Method 1: Install from releases (recommended)
  - Go to the official releases page: https://github.com/Selahaddin67/Text-Editor-CLI/releases
  - Download the installer or binary suitable for your platform.
  - Run the installer or execute the downloaded file according to your OS guidance.
  - After installation, run the command-line tool from your terminal as described in the quick start and help output.

- Method 2: Install from source (advanced)
  - Clone the repository:
    - git clone https://github.com/Selahaddin67/Text-Editor-CLI.git
  - Navigate to the project directory:
    - cd Text-Editor-CLI
  - Create a virtual environment (optional but recommended):
    - python3 -m venv venv
    - source venv/bin/activate  (Linux/macOS)
    - venv\Scripts\activate     (Windows)
  - Install dependencies:
    - pip install -r requirements.txt
  - Install the package in editable mode:
    - pip install -e .
  - Run the editor (depending on the packaging, you might use a command like text-editor-cli or python -m text_editor_cli)

- Method 3: Docker (optional)
  - Run the tool in a container to avoid local dependency setup:
    - docker run --rm -it text-editor-cli:latest
  - You can mount your local workspace into the container to edit real files.

- Environment and configuration
  - The tool looks for a simple config in your home directory or the project’s config path.
  - You can customize default behavior, such as enabling word frequency analysis on load, setting the default text encoding, or altering key bindings.

Basic usage 🧰
- Start the editor with a file:
  - text-editor-cli filename.txt
  - or python -m text_editor_cli filename.txt
- Basic navigation:
  - Move through the file using arrow keys or vim-like key bindings if enabled.
  - Jump to a line with a command like :<line-number> (or a similar supported syntax).
- Editing commands:
  - i to insert text
  - Esc to exit insert mode (if using modal editing)
  - x to delete a character
  - dd to delete a line (depending on configuration)
  - y to copy, p to paste
  - u to undo, Ctrl+r to redo
- Saving and exiting:
  - :w to save
  - :q to quit
  - :wq to save and quit
- Help and built-in guidance:
  - h or help Opens the help panel with a concise command reference.
  - i for insert mode (if using a modal approach)
- Quick edit flow:
  - Open a file
  - Edit lines or insert blocks
  - Save
  - Run a quick word analysis to understand word distribution
  - Apply editing commands to improve readability

Word analysis and editing commands 🧠
- Word count
  - Shows total word count, character count, and line count.
- Unique words
  - Lists how many distinct words appear in the current buffer.
- Top words
  - Displays the most frequent words with counts.
- Readability hints
  - Provides rough readability indicators based on sentence and word length.
- Frequency charts (text output)
  - Prints a simple frequency list suitable for quick inspection in the terminal.
- Search and replace
  - Replace all occurrences of a term with another, with an option to perform a case-insensitive search.
- Inline edits
  - Edit a specific line by number and replace a portion of text directly.
- Word-based editing tips
  - The editor can offer suggestions for common word replacements to improve clarity and tone.
- Batch edits
  - Apply a series of edits across multiple lines or the whole document, useful for quick formatting tasks.

File processing and formats 📄
- Supported formats
  - Plain text (.txt)
  - Markdown (.md)
  - Simple configuration-like text files (.ini, .cfg)
  - Other lightweight formats with simple line-based structure
- Encoding
  - UTF-8 by default; supports UTF-16 and other common encodings with explicit flags if needed.
- Line endings
  - Normalizes line endings on save to prevent cross-platform issues.
- Import/export
  - Import from or export to plain text with optional transformations (trim whitespace, normalize spaces).

Advanced editing features ⚙️
- Multiline editing
  - Edit blocks of text with line ranges, similar to editing a region in a traditional editor.
- Macro-like commands
  - Define a sequence of edits that you can replay across the document.
- Syntax awareness
  - Basic awareness for code blocks in Markdown files to avoid breaking code spans during edits.
- Auto-format hints
  - Suggests improvements for line length and indentation in code or prose sections.
- Undo/redo stack
  - Maintains a robust history to revert changes precisely.
- Session persistence
  - Save the current session state to resume work later.

Customization and configuration 🎛️
- Key bindings
  - Adjust common commands to match your preferred editing style.
- Theme and visuals
  - Change color schemes for syntax-like highlighting and readability cues.
- Plugins and extensions
  - Lightweight plugin system to add features like spell-check or code snippet insertion.
- Config file
  - A simple file stores defaults such as encoding, line endings, and analysis options.
- Environment variables
  - Override default paths, log levels, and tool behavior through environment settings.

Testing and quality assurance 🧪
- Unit tests
  - A suite verifies core editing operations, word counting, and file I/O.
- Integration tests
  - Tests cover end-to-end flows like opening a file, performing edits, and saving.
- Linting and style
  - The project follows a consistent style guide for Python.
- How to run tests
  - Follow the project’s test runner commands documented in the tests folder or test section of the docs.

Docker and virtualization 🐳
- Docker image
  - The Docker image runs Text-Editor-CLI in an isolated environment, ensuring consistent behavior across platforms.
- Local development with Docker
  - Mount your workspace to edit real files in a container, useful for CI pipelines and cross-platform testing.

Accessibility and usability ♿
- Keyboard-centric design
  - All common operations are reachable via the keyboard with minimal mouse interaction.
- Clear prompts
  - Messages are concise and actionable to reduce confusion during editing.
- Feedback and status
  - The editor shows status lines for mode, cursor position, and analysis results.

Contributing to Text-Editor-CLI 🤝
- How to contribute
  - Find an issue that interests you or propose a new feature.
  - Open a pull request with a clear description of changes and rationale.
  - Include tests or examples where possible.
- Code style
  - Adhere to the project’s coding standards and documentation guidelines.
- Documentation
  - Improve help texts, add examples, and expand the README with practical usage scenarios.
- Community guidelines
  - Be respectful, focused, and constructive in all discussions.

Roadmap and future work 🗺️
- Enhance word analysis
  - Add bigram and trigram statistics, lexical diversity metrics, and readability scoring enhancements.
- Improve editing workflows
  - Introduce more advanced editing modes, file diffs, and batch transformations.
- Cross-format support
  - Extend support to common office formats, like simple Markdown tables and code blocks without breaking formatting.
- Collaboration features
  - Add basic sharing and synchronization for teams working on text documents.

License and credits 🧾
- License
  - This project is open source and released under an OSI-approved license. See the LICENSE file in the repository for details.
- Acknowledgments
  - Thanks to the contributors and educators who helped shape this tool into a helpful learning resource.

Appendix: Frequently asked questions (quick hits) ❓
- Is Text-Editor-CLI suitable for Windows?
  - Yes. It supports Windows via native executables or WSL.
- Can I use this in teaching or coursework?
  - Yes. It’s designed for educational use and easy onboarding.
- How do I reset preferences?
  - The config file stores preferences; removing or resetting it restores defaults.
- How can I see the available commands?
  - Use the built-in help command, or run the editor with a --help flag if supported.

Appendix: Quick reference commands (sample)
- Open a file:
  - text-editor-cli filename.txt
- Show help:
  - text-editor-cli --help
- Count words and lines:
  - text-editor-cli filename.txt --stats
- Find and replace:
  - text-editor-cli filename.txt --find "old" --replace "new"
- Analyze word frequency:
  - text-editor-cli filename.txt --analyze
- Save and exit:
  - :wq (if using a modal editor) or the editor’s quit command
- Export to simple text:
  - text-editor-cli filename.txt --export plain.txt

Notes
- The primary distribution channel is the Releases page. Use that page to obtain stable builds and installers.
- If you prefer not to download binaries, you can build from source using the repository. Follow the installation steps above for that path.

This README focuses on making the project approachable, explaining how to get started, and outlining the core capabilities. The goal is to help beginners learn how a text editor can function in a terminal while offering practical features for real projects and coursework. The combination of editing and analysis tools aims to support both writing and study workflows in a single, lightweight package.