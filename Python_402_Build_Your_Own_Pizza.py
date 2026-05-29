# Build Your Own Pizza
# Alexander Fraser
# 24 May 2026

size_list = {"S": 6, "M": 8, "L": 10}
base_list = {"C": 0, "T": 1, "D": 2}
service_list = {"T": 0, "E": 2}
discount_code = "P1ZZ4"

def collect_input(retry_flag):
    if retry_flag == 1:
        print("The inputs you entered were invalid. Please try again.")

    size = input("Pick a size: [S]mall=$6, [M]edium=$8, [L]arge=$10: ")
    base = input("Choose your base: [C]lassic=$0, [T]hin=$1, [D]eep=$2: ")
    toppings = input("How many toppings would you like ($1.50 each up to "
                    + "a max of 4 toppings): ")
    service = input("[T]akeout=$0 or [E]at-in=$2: ")
    discount = input("Enter the discount code: ")

    client_inputs = [size, base, toppings, service, discount]

    return client_inputs

def check_input(client_inputs):
    input_indicator = 0
    if client_inputs[0] not in size_list:
        input_indicator = 1
    if client_inputs[1] not in base_list:
        input_indicator = 1
    try:
        val = int(client_inputs[2])
        if val not in range(0,5):
            input_indicator = 1
    except:
        input_indicator = 1
    if client_inputs[3] not in service_list:
        input_indicator = 1
        
    return input_indicator

def calculate_cost(client_inputs):
    total_cost = 0
    total_cost = total_cost + size_list[client_inputs[0]]
    total_cost = total_cost + base_list[client_inputs[1]]
    total_cost = total_cost + int(client_inputs[2]) * 1.5 
    total_cost = total_cost + service_list[client_inputs[3]]
    if client_inputs[4] == discount_code:
        total_cost = total_cost * 0.8

    return total_cost

def main():
    client_inputs = []
    input_indicator = 1
    retry_flag = 0

    print("Build Your Own Pizza")
    while input_indicator == 1:
        client_inputs.clear()
        client_inputs = collect_input(retry_flag)
        input_indicator = check_input(client_inputs)
        retry_flag = 1

    total_cost = calculate_cost(client_inputs)
    print("Your pizza costs: $%.2f" % total_cost)

if __name__ == "__main__":
    main()
