employees_full_name = "Jean Zakwanzi"
number_of_hours = 40
hourly_pay_rate = 6.75
federal_tax_withholding_rate = 0.2
state_tax_withholding_rate = 0.09

Gross_pay = hourly_pay_rate*number_of_hours
federal_tax_withholding =federal_tax_withholding_rate*Gross_pay
state_tax_withholding =state_tax_withholding_rate * Gross_pay
total_deduction = federal_tax_withholding + state_tax_withholding
net_pay = Gross_pay + total_deduction


print("The name of employee is",employees_full_name)
print("He/She worked",number_of_hours,"in a week")
print('hourly pay rate was',hourly_pay_rate)
print('federal tax',federal_tax_withholding_rate)
print('state tax was',state_tax_withholding_rate)

print("Gross pay",'$',Gross_pay)
print("federal tax", '$',federal_tax_withholding)
print("state tax",'$',state_tax_withholding)
print("total deductions",'$',total_deduction)
print("net pay",'$',net_pay)
