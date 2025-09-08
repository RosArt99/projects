looper = True
while looper:
    try:
        big_booster_total_fuel = int(input("Enter big booster total fuel: "))
        small_booster_total_fuel = int(input("Enter small booster total fuel: "))
        big_booster_fuel_consumption = float(input("Enter big booster fuel consumption: "))
        small_booster_fuel_consumption = float(input("Enter small booster fuel consumption: "))
        boosters_burning_time = float(input("Enter boosters burning time: "))
        if big_booster_total_fuel <= 0 or small_booster_total_fuel <= 0 or big_booster_fuel_consumption <= 0 or small_booster_fuel_consumption <= 0 or boosters_burning_time <= 0:
            raise TypeError
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except TypeError:
        print("All values must be greater than zero. Please try again.")
    else:
        big_booster_thrust_limiter_coeff = big_booster_total_fuel / (boosters_burning_time * big_booster_fuel_consumption)
        small_booster_thrust_limiter_coeff = small_booster_total_fuel / (boosters_burning_time * small_booster_fuel_consumption)
        print(f"Big booster thrust limiter is set to {big_booster_thrust_limiter_coeff:.3f}")
        print(f"Small booster thrust limiter is set to {small_booster_thrust_limiter_coeff:.3f}")
        looper = False