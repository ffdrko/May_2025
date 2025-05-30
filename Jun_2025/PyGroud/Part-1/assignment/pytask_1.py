try:
    total_value = int(input("Enter the total value: "))
    main_value = int(input("Enter the main value: "))

    total = main_value / total_value * 100

    print(f"That is {total}%.")
except ValueError:
    print("Please enter a number, Run the program again.")