# Zodiac Degree Analyzer

A minimal tool for structured astrological reference.  
No interpretations. No narrative. Just component data.

## Features

- Two input modes:
  - Sign + Degree + Minute (dropdown)
  - Decimal degree (0–360°)
- Output includes:
  - Sign
  - Duad
  - Decan
  - Bound
  - Numerology
  - Sabian Symbol (text only)

## Purpose

This tool returns raw symbolic data associated with a specific zodiac degree.  
It is intended as a structural aid, not an interpretive system.

## Live App

[https://yourusername-zodiac-analyzer.streamlit.app](#)

## Files

- `app_dropdown.py`: Streamlit app script
- `astrology_zodiac_data_en_full.csv`: Degree-to-data mapping table

## Usage

Run locally:

```bash
streamlit run app_dropdown.py
