import sys

def cal(salary):
    try:
        salary = int(salary)
        # 如果参数不能转换为 int 类型，会触发 ValueError 异常
        # 捕获这个异常，打印信息并退出
    except ValueError:
        print('Parameter Error')
        exit()
    start_point = 5000  # 起征点
    social_insurance_point = 0.08 + 0.02 + 0.005 + 0.06  # 社保比例
    # 需要缴税的那部分工资
    tax_part_salary = salary * (1-social_insurance_point) - start_point  
    if tax_part_salary <= 0:
        tax = 0 
    elif tax_part_salary <= 3000:
        tax = tax_part_salary * 0.03
    elif tax_part_salary <= 12000:
        tax = tax_part_salary * 0.1 - 210 
    elif tax_part_salary <= 25000:
        tax = tax_part_salary * 0.2 - 1410
    elif tax_part_salary <= 35000:
        tax = tax_part_salary * 0.25 - 2660
    elif tax_part_salary <= 55000:
        tax = tax_part_salary * 0.3 - 4410
    elif tax_part_salary <= 80000:
        tax = tax_part_salary * 0.35 - 7160
    else:
        tax = tax_part_salary * 0.45 - 15160
    after_tax_salary = salary * (1-social_insurance_point) - tax
    return '{:.2f}'.format(after_tax_salary)

if __name__ == '__main__':
    for i in sys.argv[1:]:
        num, salary = i.split(':')
        print('{}:{}'.format(num, cal(salary)))
