from datetime import datetime

interest_buckets = {
    "public_existing": [
        (7, 45, 5.75),
        (45, 179, 6.25),
        (180, 210, 6.35),
        (211, 364, 6.4),
        (365, 729, 6.8),
        (730, 1094, 6.8),
        (1095, 1274, 6.8),
        (1825, 3650, 6.85)
    ],
    "public_revised": [
        (7, 45, 5.75),
        (45, 179, 6.25),
        (180, 210, 6.35),
        (211, 364, 6.4),
        (365, 729, 7.0),
        (730, 1094, 6.75),
        (1095, 1274, 6.7),
        (1825, 3650, 6.6)
    ],
    "senior_existing": [
        (7, 45, 6.25),
        (45, 179, 6.75),
        (180, 210, 6.85),
        (211, 364, 6.9),
        (365, 729, 7.3),
        (730, 1094, 7.3),
        (1095, 1274, 7.3),
        (1825, 3650, 7.35)
    ],
    "senior_revised": [
        (7, 45, 6.25),
        (45, 179, 6.75),
        (180, 210, 6.85),
        (211, 364, 6.9),
        (365, 729, 7.5),
        (730, 1094, 7.25),
        (1095, 1274, 7.2),
        (1825, 3650, 7.1)
    ]
}

def parse_date(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return datetime.strptime(s, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD. Try again.")

def get_choice(prompt, allowed):
    while True:
        c = input(prompt).strip().lower()
        if c in allowed:
            return c
        print(f"Invalid choice. Allowed: {', '.join(allowed)}")

def find_rate(user_type, rate_type, duration_days):
    key = f"{user_type}_{rate_type}"
    buckets = interest_buckets.get(key)
    if not buckets:
        return None, f"Invalid user/rate type: {key}"
    for min_d, max_d, rate in buckets:
        # treat bucket ranges as inclusive
        if min_d <= duration_days <= max_d:
            return rate, None
    # If duration not matched, give friendly feedback:
    min_allowed = min(b[0] for b in buckets)
    max_allowed = max(b[1] for b in buckets)
    return None, f"Duration {duration_days} days not in allowed range ({min_allowed}-{max_allowed} days)."

def main():
    print("Fixed Deposit Interest Rate Finder")
    start_date = parse_date("Enter start date (YYYY-MM-DD): ")
    end_date = parse_date("Enter end date (YYYY-MM-DD): ")

    if end_date <= start_date:
        print("End date must be after start date.")
        return

    duration_days = (end_date - start_date).days
    print(f"FD duration: {duration_days} days")

    user_type = get_choice("Enter user type (public/senior): ", {"public", "senior"})
    rate_type = get_choice("Enter rate type (existing/revised): ", {"existing", "revised"})

    rate, err = find_rate(user_type, rate_type, duration_days)
    if err:
        print(err)
    else:
        print(f"Assigned interest rate: {rate:.2f}%")

if __name__ == "__main__":
    main()
