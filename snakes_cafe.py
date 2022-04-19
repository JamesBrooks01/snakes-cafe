print(
"""***********************************************
******    Welcome to the Snakes Cafe!   *******
******    Please see our menu below.    *******
******
****** To quit at any time, type "quit" *******
** To see a summary of your meal, type "meal **
***********************************************""")

print(
  """Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
"""
)

print(
  """***********************************
** What would you like to order? **
***********************************"""
)

menuDict = {
  'Appetizers': ['Wings', 'Cookies', 'Spring Rolls'],
  'Entrees': ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden'],
  'Desserts': ['Ice Cream', 'Cake', 'Pie'],
  'Drinks': ['Coffee', 'Tea', 'Unicorn Tears']
}
mealTypes = ['Appetizers', 'Entrees', 'Desserts', 'Drinks']

def order():
  mealDict = {}
  mealSummary = []
  num = 0
  while True:
    userOrder = input("> ")
    isInMenu = []
    if userOrder == 'quit':
      break
    if userOrder == 'meal':
      for item in mealDict:
        if int(mealDict[item]) > 1:
          mealSummary.append(f"{mealDict[item]} orders of {item}")
        else:
          mealSummary.append(f"{mealDict[item]} order of {item}")
      summary = "** Your meal is "
      for meal in mealSummary:
        if meal == mealSummary[-1]:
          summary += f"{meal}. **"
        else:
          summary += f"{meal}, "
      print(summary)
      break
    if userOrder not in mealDict:
      num = 0
    for type in mealTypes:
      isInMenu.append(userOrder in menuDict[type])
    if True in isInMenu:
      num += 1
      mealDict.update({f"{userOrder}": f"{num}"})
      if num > 1:
        print(f"** {num} orders of {userOrder} have been added to your meal **")
      else:
        print(f"** {num} order of {userOrder} has been added to your meal **")
    else:
      print("That meal isn't on our menu or the name was entered incorrectly. Remember that the input is Case Sensitive")

order()