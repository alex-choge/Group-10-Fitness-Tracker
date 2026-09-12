# FitTrack

## Group 10 — Fitness Tracker (Python OOP Course Project)

A command-line fitness tracker where users register, log in, and
work toward fitness goals with the help of assigned trainers.

## Core features

- User registration and login with hashed passwords (`utils/auth.py`)
- Role-based access via `@login_required` / `@admin_required`
  decorators (`utils/decorator.py`)
- `Admin` role (`models/admin.py`) for managing users, goals, and
  trainers
- Set and track fitness goals (`models/goal.py`)
- Trainer records that can guide or be assigned to a goal
  (`models/trainer.py`)
- Input validation for user-entered data (`utils/validation.py`)
- JSON file persistence, one file per entity type
  (`utils/storage.py`)

## Data storage

Unlike a single combined data file, this version keeps each entity
in its own JSON file under `data/`:

| File | Holds |
|---|---|
| `user.json` | Registered users and admins |
| `goal.json` | Fitness goals |
| `trainers.json` | Trainer records |

`utils/storage.py` centralizes reading and writing these files so
no other module touches JSON directly.

## Project structure

```
Group-10-Fitness-Tracker/
├── data/
│   ├── goal.json
│   ├── trainers.json
│   └── user.json
├── models/
│   ├── __init__.py
│   ├── admin.py
│   ├── goal.py
│   ├── trainer.py
│   └── user.py
├── utils/
│   ├── __init__.py
│   ├── auth.py
│   ├── decorator.py
│   ├── storage.py
│   └── validation.py
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_goal.py
│   └── test_user.py
├── main.py
├── .gitignore
└── README.md
```

## Running the application

```
python main.py
```

## Running the tests

```
python -m unittest discover -s tests -v
```

## Contributors

Group 10.

