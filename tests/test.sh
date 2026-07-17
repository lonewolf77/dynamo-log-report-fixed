#!/bin/bash

# Ensure output directory exists for Harbor
mkdir -p /logs/verifier

# Run plain pytest with CTRF reporting. Dependencies are baked into the image.
pytest /tests/test_outputs.py -rA --ctrf /logs/verifier/ctrf.json

# Write the final reward securely to the correct Harness location
if [ $? -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
