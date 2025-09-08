def get_positive_number(promp: str, num_type: float):
    while True:
        try:
            value = num_type(input(promp))
            if value <= 0:
                print("Value must be greater than zero. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def check_trust(name: str, total_fuel: int, fuel_consumption: float, burning_time: float)->None:
    coeff = total_fuel / (burning_time * fuel_consumption)

    if coeff > 1:
        print(f"Warning: {name} thrust limiter coefficient exceeds 1. Means the burning time is too short. Additional fuel is required.")
    else:
        print(f"{name} thrust limiter is set to {coeff:.3f}")

def main():
    big_booster_total_fuel = get_positive_number("Enter big booster total fuel: ", int)
    small_booster_total_fuel = get_positive_number("Enter small booster total fuel: ", int)
    big_booster_fuel_consumption = get_positive_number("Enter big booster fuel consumption: ", float)
    small_booster_fuel_consumption = get_positive_number("Enter small booster fuel consumption: ", float)
    boosters_burning_time = get_positive_number("Enter boosters burning time: ", float)

    big_booster_thrust_limiter_coeff = big_booster_total_fuel / (boosters_burning_time * big_booster_fuel_consumption)
    small_booster_thrust_limiter_coeff = small_booster_total_fuel / (boosters_burning_time * small_booster_fuel_consumption)

    check_trust("Big Booster", big_booster_total_fuel, big_booster_fuel_consumption, boosters_burning_time)
    check_trust("Small Booster", small_booster_total_fuel, small_booster_fuel_consumption, boosters_burning_time)

if __name__ == "__main__":
    main()