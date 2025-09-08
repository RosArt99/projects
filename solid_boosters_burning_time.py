def get_positive_number(prompt: str, num_type: float):
    while True:
        try:
            value = num_type(input(prompt))
            if value <= 0:
                print("Value must be greater than zero. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    big_booster_total_fuel = get_positive_number("Enter big booster total fuel: ", int)
    small_booster_total_fuel = get_positive_number("Enter small booster total fuel: ", int)
    big_booster_fuel_consumption = get_positive_number("Enter big booster fuel consumption: ", float)
    small_booster_fuel_consumption = get_positive_number("Enter small booster fuel consumption: ", float)
    boosters_burning_time = get_positive_number("Enter boosters burning time: ", float)

    big_booster_thrust_limiter_coeff = big_booster_total_fuel / (boosters_burning_time * big_booster_fuel_consumption)
    small_booster_thrust_limiter_coeff = small_booster_total_fuel / (boosters_burning_time * small_booster_fuel_consumption)

    print(f"Big booster thrust limiter is set to {big_booster_thrust_limiter_coeff:.3f}")
    print(f"Small booster thrust limiter is set to {small_booster_thrust_limiter_coeff:.3f}")

if __name__ == "__main__":
    main()