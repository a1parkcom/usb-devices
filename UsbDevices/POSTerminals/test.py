from SmartSale import SmartSale

sm = SmartSale()
print(sm.is_connection())

pay = sm.pay(100, 202)
print(pay)

refund = sm.refund()
print(refund)

fixed_pay = sm.fixed_pay(203)
print(fixed_pay)