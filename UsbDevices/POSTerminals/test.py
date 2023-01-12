from SmartSale.operations import ConnectionCheck, Payment, Refund

print(ConnectionCheck().query())
query = Payment(100).query()
print(query)
