# FD-Interest-calculator
A simple Python-based Fixed Deposit (FD) interest rate calculator that assigns the correct rate based on FD duration, user type (public/senior), and rate type (existing/revised).

## Fixed Deposit Interest Rate Finder (Python)

A small command-line utility to determine the applicable fixed-deposit (FD) interest rate based on:
- start and end dates (duration)
- user type (public / senior)
- rate type (existing / revised)

## Features
- Validates date format (YYYY-MM-DD)
- Calculates FD duration in days
- Assigns interest rate from defined buckets
- Friendly error messages when input or duration is invalid

## Files
- `fd_calculator.py` — main script
- `README.md` — this file

## How to run
1. Ensure you have Python 3 installed.
2. Save `fd_calculator.py` in a folder.
3. Run:

## Output sample
- Start date (YYYY-MM-DD)
- End date (YYYY-MM-DD)
- User type: public or senior
- Rate type: existing or revised

Enter start date (YYYY-MM-DD): 2025-01-01
Enter end date (YYYY-MM-DD): 2025-07-01
FD duration: 181 days
Enter user type (public/senior): public
Enter rate type (existing/revised): existing
Assigned interest rate: 6.35%
