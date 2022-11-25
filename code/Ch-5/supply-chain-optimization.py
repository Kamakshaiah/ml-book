## Find the optimal locations of your manufacturing facilities to meet your customers’ demand and reduce production costs
# variables

import pandas as pd
from pulp import *

# Import Manufacturing Costs
manvar_costs = pd.read_excel('variable_costs.xlsx', index_col = 0)
# Import Freight Costs
freight_costs = pd.read_excel('freight_costs.xlsx', index_col = 0)
# Variable Cost
var_cost = freight_costs/1000 + manvar_costs 
# Import Plant Fixed Costs
fixed_costs = pd.read_excel('fixed_cost.xlsx', index_col = 0)
# Import Low Capacity and High Capacity Plant
cap = pd.read_excel('capacity.xlsx', index_col = 0)
# Import Demand
demand = pd.read_excel('demand.xlsx', index_col = 0)

# Define Decision Variables
loc = ['USA', 'Germany', 'Japan', 'Brazil', 'India']
size = ['Low', 'High']

# Initialize Class
model = LpProblem("Supply Chain Optimization", LpMinimize)

# Create Decision Variables
x = LpVariable.dicts("production_", [(i,j) for i in loc for j in loc],
                     lowBound=0, upBound=None, cat='continuous')
y = LpVariable.dicts("plant_", 
                     [(i,s) for s in size for i in loc], cat='Binary')

# Define Objective Function

model += (lpSum([fixed_costs.loc[i,s] * y[(i,s)] * 1000 for s in size for i in loc])
          + lpSum([var_cost.loc[i,j] * x[(i,j)]   for i in loc for j in loc]))

# Add Constraints
for j in loc:
    model += lpSum([x[(i, j)] for i in loc]) == demand.loc[j,'Demand']
for i in loc:
    model += lpSum([x[(i, j)] for j in loc]) <= lpSum([cap.loc[i,s]*y[(i,s)] * 1000
                                                       for s in size])

# Solve Model
model.solve()
print("Total Costs = {:,} ($/Month)".format(int(value(model.objective))))
print('\n' + "Status: {}".format(LpStatus[model.status]))


# Dictionnary
dict_plant = {}
dict_prod = {}
for v in model.variables():
    if 'plant' in v.name:
        name = v.name.replace('plant__', '').replace('_', '')
        dict_plant[name] = int(v.varValue)
        p_name = name
    else:
        name = v.name.replace('production__', '').replace('_', '')
        dict_prod[name] = v.varValue
    print(name, "=", v.varValue)

