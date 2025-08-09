print("👋 Hey there! I'm your friendly calculator, here to help you crunch some numbers.")

while True:
    first_input = input("🔢 Let's start—what's your first number? ")
    try:
        num1 = float(first_input)
        break
    except ValueError:
        print(f"😅 Hmm, '{first_input}' doesn't seem like a number. Give it another shot!")

while True:
    second_input = input("🔢 Awesome. Now, what's the second number? ")
    try:
        num2 = float(second_input)
        break
    except ValueError:
        print(f"😬 Oops! '{second_input}' isn't a valid number either. Try again!")

print("\n🤔 So, what do you want to do with these numbers?")
print("1️⃣ Add")
print("2️⃣ Subtract")
print("3️⃣ Multiply")
print("4️⃣ Divide")

choice = input("👉 Just type 1, 2, 3, or 4 to choose: ")

print("\n🧮 Calculating...")
if choice == '1':
    result = num1 + num2
    print(f"✅ Easy math! {num1} plus {num2} equals {result}")

elif choice == '2':
    result = num1 - num2
    print(f"✅ Got it! {num1} minus {num2} gives you {result}")

elif choice == '3':
    result = num1 * num2
    print(f"✅ Multiplying magic! {num1} times {num2} equals {result}")

elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"✅ Division done! {num1} divided by {num2} equals {result}")
    else:
        print("❌ Uh-oh! Division by zero isn't allowed. Let's not break the universe today.")

else:
    print("😕 Hmm, that wasn't one of the options. Maybe try again and pick 1, 2, 3, or 4.")

print("\n🎉 Thanks for hanging out with me! Hope your day adds up to something great.")