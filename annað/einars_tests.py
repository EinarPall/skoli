# n = 1
# while n < 10:
#     print(n)
#     n += 1

def fund_me(age, monthly_salary):
    if int(age) < 24 and monthly_salary < 100000:
        return 20000
    else:
        return "Not applicable for fund"

older_gentleman = fund_me("25", 20000)
younger_gentleman = fund_me(22, 20000)
print(older_gentleman)
print(younger_gentleman)

