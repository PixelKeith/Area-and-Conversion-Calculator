# Python Area Calculator and Unit Converter
import area
import conversion

def main():
    print("\nWelcome to Python Area Calculator and Unit Converter")

    while True:

        option = input("\n[1] Area Calculator\n[2] Unit Converter\n[0] Exit\n:")

        if option == "1":
            print("\nArea Calculator")

            while True:
                shape = input(
                    "[1] Square\n"
                    "[2] Parallelogram\n"
                    "[3] Rectangle\n"
                    "[4] Trapezoid\n"
                    "[5] Triangle\n"
                    "[6] Circle\n: "
                )

                match shape:
                    case "1":
                        area.area_square()
                        break

                    case "2":
                        area.area_parallelogram()
                        break

                    case "3":
                        area.area_rectangle()
                        break

                    case "4":
                        area.area_trapezoid()
                        break

                    case "5":
                        area.area_triangle()
                        break

                    case "6":
                        area.area_circle()
                        break

                    case _:
                        print("\nInvalid option.\n")

        elif option == "2":
            print("\nUnit Converter")

            while True:
                unit = input(
                    "[1] Length\n"
                    "[2] Mass\n"
                    "[3] Speed\n"
                    "[4] Temperature\n"
                    "[5] Time\n"
                    "[6] Volume\n:"
                )

                match unit:
                    case "1":
                        conversion.length_converter()
                        break

                    case "2":
                        conversion.mass_converter()
                        break

                    case "3":
                        conversion.speed_converter()
                        break

                    case "4":
                        conversion.temp_converter()
                        break

                    case "5":
                        conversion.time_converter()
                        break

                    case "6":
                        conversion.volume_converter()
                        break

                    case _:
                        print("\nInvalid option.\n")


        elif option == "0":
            print("Goodbye!")
            break
        else:
            print("\nPlease enter [1], [2], or [0]\n")

if __name__ == "__main__":
    main()