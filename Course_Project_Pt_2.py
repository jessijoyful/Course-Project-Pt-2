import datetime
def calculate_tax_and_netpay(total_hours, hourly_rate, tax_rate):
    tax = float(total_hours) * float(hourly_rate) * (float(tax_rate) / 100)

    net_pay = float(total_hours) * float(hourly_rate) - tax

    return tax, net_pay

def get_name():
    name = input ("Enter Employee Name: ")

    return name

def get_total_hours():
    total_hours = input ("Enter Total Hours: ")

    return total_hours

def get_hourly_rate():
    hourly_rate = float(input("Enter Hourly Rate: "))

    return hourly_rate

def get_tax_rate():
    tax_rate = float(input("Enter Tax Rate (In %): "))

    return tax_rate

def get_gross_pay(total_hours, hourly_rate):

    gross_pay = float(total_hours) * float(hourly_rate)

    return gross_pay

def display_employee_info(from_date, to_date, name, total_hours, hourly_rate, tax_rate, tax, gross_pay, net_pay):

    print("----------------------------------------------------")
    print("From Date: ", from_date.strftime('%m/%d/%Y'))
    print("To Date: ", to_date.strftime('%m/%d/%Y'))
    print("Employee Name: ", name)
    print("Total Hours: ", total_hours)
    print("Hourly Rate: ", hourly_rate)
    print("Gross Pay: ", gross_pay)
    print("Tax Rate: ", tax_rate)
    print("Income Tax: ", tax)
    print("Net Pay: ", net_pay)

    print("-----------------------------------------------------")

def display_total_info(total_dict):

    print("-----------------------------------------------------")
    print("Total Number of Employees: ", total_dict['total_employees'])
    print("Total Hours: ",total_dict['total_hours'])
    print("Total Tax: ", total_dict['total_tax'])
    print("Total Gross Pay: ", total_dict['total_gross_pay'])
    print("Total Net Pay: ", total_dict['total_net_pay'])

    print("-----------------------------------------------------")

def get_from_and_to_dates():
    from_date = input("Enter From Date in mm/dd/yyyy Format: ")
    from_date = datetime.datetime.strptime(from_date, "%m/%d/%Y").date()
    to_date = input("Enter To Date in mm/dd/yyyy Format: ")
    to_date = datetime.datetime.strptime(to_date, "%m/%d/%Y").date()

    return from_date, to_date

def calculate_employees_taxes(employee_list, total_dict):
    for employee in employee_list:
        from_date, to_date, name, hours, hourly_rate, tax_rate = employee 
        gross_pay = get_gross_pay(hours, hourly_rate)
        tax, net_pay = calculate_tax_and_netpay(hours, hourly_rate, tax_rate)
        display_employee_info(from_date, to_date, name, hours, hourly_rate, tax_rate, tax, gross_pay, net_pay)

    total_dict['total_employees'] += 1
    total_dict['total_hours'] += int(hours)
    total_dict['total_tax'] += tax
    total_dict['total_gross_pay'] += gross_pay
    total_dict['total_net_pay'] += net_pay

def main():
    employee_list = []
    total_dict = {"total_employees" : 0, "total_hours" :0, "total_tax" : 0, "total_gross_pay" : 0, "total_net_pay" : 0}
    while True:

        name = get_name()

        if name == "End":
            break

        from_date, to_date = get_from_and_to_dates()

        hours = get_total_hours()

        hourly_rate = get_hourly_rate()

        tax_rate = get_tax_rate()

        print()

        employee_list.append([from_date, to_date, name, hours, hourly_rate, tax_rate])

        calculate_employees_taxes(employee_list, total_dict)

        display_total_info(total_dict)

if __name__ == "__main__":
    main()