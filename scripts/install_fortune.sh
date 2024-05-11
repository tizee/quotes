#!/usr/bin/env sh

set -e

ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
DATA="${ROOT}/output/fortune"

# homebrew fortune
if which strfile > /dev/null ; then
  if which brew > /dev/null; then
    cp -vf ${DATA}/* $(brew --prefix fortune)/share/games/fortunes
  else
    echo "homebrew is not installed" && exit 1
  fi
fi
