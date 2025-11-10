# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Environment Setup
```bash
uv install                    # Install all dependencies including dev tools
```

### Development Server
```bash
uv run python app.py          # Start Flask development server (http://127.0.0.1:5000)
```

### Code Quality & Testing
```bash
uv run ruff check .           # Run linting checks
uv run ruff check . --fix     # Auto-fix linting issues
uv run ruff format .          # Format code
uv run ruff format --check .  # Check formatting without making changes

# Manual TodoManager testing
uv run python -c "
from todo_manager import TodoManager
import tempfile, os
with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
    temp_file = f.name
try:
    tm = TodoManager(temp_file)
    # Test add_todo, get_all_todos, update_todo, delete_todo
    print('TodoManager tests passed')
finally:
    os.unlink(temp_file)
"
```

### Syntax Validation
```bash
find . -name "*.py" -not -path "./.venv/*" | xargs python -m py_compile
```

## Architecture Overview

### Core Components

**Flask Application (`app.py`)**
- Single-file Flask application with clean route organization
- Provides both web UI and RESTful API endpoints
- Uses TodoManager for data persistence abstraction
- All API endpoints return JSON responses with proper HTTP status codes

**Data Layer (`todo_manager.py`)**
- JSON file-based persistence with automatic file creation
- Complete CRUD operations with timestamp management
- UTF-8 encoding support for international content
- Type hints throughout for better code clarity

**Frontend (`templates/index.html`)**
- Modern responsive design with gradient styling
- AJAX-based interactions for seamless user experience
- Real-time statistics and task management
- Mobile-optimized interface

### Data Model

Todo items stored in JSON with this structure:
```json
{
  "id": 1,
  "title": "Task title",
  "description": "Task description",
  "completed": false,
  "created_at": "2025-11-10T10:37:36.463504",
  "completed_at": null
}
```

### API Endpoints

- `GET /` - Web interface
- `GET /api/todos` - List all todos
- `POST /api/todos` - Create todo (requires title, optional description)
- `PUT /api/todos/<id>` - Update todo (supports any todo field)
- `DELETE /api/todos/<id>` - Delete todo
- `POST /api/todos/<id>/toggle` - Toggle completion status

## Code Quality Standards

**Ruff Configuration (`ruff.toml`)**
- Target: Python 3.12, line length: 88
- Enabled rules: E, F, UP, B, SIM, I, C4
- Formatting: Double quotes, space indentation
- Google docstring style (when docstrings are present)
- Missing docstrings tolerated for non-public methods

**CI/CD Pipeline**
- Automatic runs on push to main/develop and pull requests
- Ruff linting and formatting checks
- Bandit security scanning
- TodoManager functionality tests
- Auto-deployment and release creation for main branch

## Key Implementation Details

**Data Persistence**
- Uses `todos.json` for storage (created automatically)
- File operations include proper error handling for missing/corrupted files
- JSON operations use `ensure_ascii=False` for international character support

**Error Handling**
- API endpoints return proper HTTP status codes (400 for bad input, 404 for not found)
- Input validation requires non-empty titles for new todos
- Graceful handling of JSON decode errors and file not found

**Internationalization**
- User interface fully localized in Chinese
- UTF-8 encoding throughout the stack
- JSON storage supports international characters

## Development Workflow

1. Make code changes
2. Run `uv run ruff check . --fix` and `uv run ruff format .`
3. Test manually with `uv run python app.py`
4. Commit changes (CI will run full quality checks)
5. Push to trigger CI/CD pipeline

The project prioritizes simplicity and code quality over complex features, making it an excellent example of modern Python web development practices.