# Influencer Authenticity Decay Tracker

A Python CLI + ORM project that helps brands monitor and predict when an influencer’s perceived authenticity begins to decline over time.

## Features

- Manage influencers and their partnerships.
- Track authenticity scores over time.
- Analyze decay using time-series data.
- CLI interface for managing the data.

## Setup

```bash
pipenv install
pipenv shell
python scripts/setup_db.py
python main.py --run
