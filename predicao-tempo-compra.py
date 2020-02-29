import pandas as pd
import matplotlib

data = pd.read_csv("nodejs_sale2.csv").rename(columns={'produto_quantidade':'qnt','forma_entrega':'frm_ent','forma_pagamento':'frm_pg','produto_id':'pd_id','valor_unitario':'val','cliente_id':'cl_id'})
data = data[['pd_id','qnt','val','frm_pg','cl_id','createdAt']]

# List just product with id == 1
gas = data[data.pd_id == 1]
print(gas)
gas = gas.groupby(['cl_id'])

print(gas.sum())

# Order by qnt
# gas_qnts = gas.sort_values(by="qnt")
# gas.to_csv('out1')
# print(data['qnt'].shape)
# print(data[data['qnt']!=1])
#