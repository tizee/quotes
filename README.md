# quotes

A collection of quotes or excerpts that I found from this lovely world.

- quotes are in `json` format using schema defined in `schema.json`.

## Available Quote Collections

- ✅ KK's 99 advice
- ✅ Naval Ravikant on Wealth
- ✅ Naval Ravikant on Happiness
- ✅ Steve Jobs
- ✅ quotes on learning
- quote on style
- quote from tweet
- quote on unix
- quote from Alan Kay
- quote from songs

## Motivation

- I'd like to understand some quotes I like from reading. And through increasing the frequency of their appearance via `fortune` in terminal environment can remind me to apply the ideas I learn from them.

## Quick Start

### Prerequisites

- Python 3
- fortune (optional, for terminal integration)
  ```bash
  brew install fortune  # macOS
  ```

### Using Makefile

The repository includes a Makefile for common tasks:

```bash
# Validate JSON files, format code, and install fortune data
make all

# Validate all quote JSON files
make check-json

# Format and lint Python code with ruff
make style

# Install quotes into fortune data directory
make fortune

# Clean output directory
make clean

# Clean all generated files (output + fortune)
make mrproper
```

## Fortune

### Manual Installation

If you prefer manual installation:

```bash
python3 generate.py --fortune
./scripts/install_fortune.sh
```

## Roadmap

- ✅ `fortune` strings format
- [ ] Web UI
- [ ] backend quote service
