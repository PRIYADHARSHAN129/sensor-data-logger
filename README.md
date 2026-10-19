
# Sensor Data Logger

A Python program that simulates a distance sensor, logs readings to a CSV file, and prints basic statistics. Built for the Applied Robotics and AI Project (University of Hertfordshire).

## How to run

```bash
python main.py
```

Output: the number of readings saved, then the min, max and average distance in cm.

## Project structure

- `sensor.py` – generates simulated distance readings
- `logger.py` – saves readings to `readings.csv`
- `main.py` – runs everything and prints min, max and average
- `.gitignore` – keeps `readings.csv` and `__pycache__/` out of the repo

## Git workflow

- `main` holds stable, working code.
- New features are built on `feature/...` branches (e.g. `feature/stats`), then merged into `main` through a Pull Request.

## Key commands

| Command | Purpose |
|---|---|
| `git clone url` | Copy a repo to your machine |
| `git status` | Show what has changed |
| `git diff` | Show exact edits |
| `git add` | Stage changes for the next commit |
| `git commit -m "msg"` | Save staged changes to local history |
| `git push` | Upload local commits to GitHub |
| `git pull` | Download new commits from GitHub |
| `git checkout -b name` | Create and switch to a new branch |

## Add vs Commit vs Push

- **Add** stages the changes you want in the next snapshot.
- **Commit** saves that snapshot to your local history with a message.
- **Push** uploads your local commits to GitHub for backup and sharing.

## Screenshots

(Add screenshots of the commit history and the merged pull request here)