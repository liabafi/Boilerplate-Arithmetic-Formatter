def arithmetic_arranger(problems, response=False):

  def problem_size_not_ok(problems):
    if len(problems) > 5:
      return True
    else:
      return False

  #Checks if number of items on the 'problems' list
  #is bigger than 5, if so, it alerts with True.

  def digit_quantity_not_ok(Sep):
    if len(Sep[0]) > 4 or len(Sep[2]) > 4:
      return True
    else:
      return False

  #Checks if the size of items on the 'Sep' list is
  #bigger than 4 digits, if so, it alerts with True.

  def numbers_not_ok(Sep):
    if Sep[0].isdigit() and Sep[2].isdigit():
      return False
    else:
      return True

  #Checks if the items on the 'Sep' list are
  #not integers, if so, it alerts with True.

  def operator_not_ok(Sep):
    if Sep[1] != '+' and Sep[1] != '-':
      return True
    else:
      return False

  #Checks if the of operators on the 'Sep' list
  #aren't '+' or '-' , if so, it alerts with True.

  def operation(Sep):
    if Sep[1] == '+':
      return int(Sep[0]) + int(Sep[2])
    else:
      return int(Sep[0]) - int(Sep[2])

  #Considering all previous checks have been made
  #this function will proceed to return the value
  #of the operation described by the list 'Sep'.

  def biggest_number_size(Sep):
    if len(str(Sep[0])) >= len(str(Sep[2])):
      return len(str(Sep[0]))
    else:
      return len(str(Sep[2]))

  #Compares the numbers in the list 'Sep' and
  #returns the lenth of the biggest one.

  def formatting(temporary_list, response):
    final = ''
    btwn = '    '  #between operations

    for i in range(len(temporary_list)):
      Space = int(temporary_list[i][4]) + 2
      final = final + (temporary_list[i][0]).rjust(Space)
      if i != len(temporary_list) - 1:
        final = final + btwn
    final = final + '\n'
    #Creates the first line in the reponse and ends it with '\n'.

    for i in range(len(temporary_list)):
      Space = int(temporary_list[i][4]) + 2
      AddS = ''
      for j in range(Space - len(str(temporary_list[i][2])) - 1):
        AddS = AddS + ' '
      final = final + (temporary_list[i][1] + AddS +
                       temporary_list[i][2]).rjust(Space)
      if i != len(temporary_list) - 1:
        final = final + btwn
    final = final + '\n'
    #Creates the second line in the reponse and ends it with '\n'.

    for i in range(len(temporary_list)):
      Space = int(temporary_list[i][4]) + 2
      dash = ''
      for j in range(Space):
        dash = dash + '-'
      final = final + dash
      if i != len(temporary_list) - 1:
        final = final + btwn
    if response:
      final = final + '\n'
    #Creates the third line in the reponse. Ends it with '\n'
    #if 'response' is set to True.

    if response == True:
      for i in range(len(temporary_list)):
        Space = int(temporary_list[i][4]) + 2
        final = final + (f'{temporary_list[i][3]:>{Space}}')
        if i != len(temporary_list) - 1:
          final = final + btwn
      #Creates the fourth line in the reponse if 'response' valeu == True.

    return final

  #Inicializing some necessary lists
  temporary_list = []
  #----------

  if problem_size_not_ok(problems):
    return "Error: Too many problems."
  #Testing the list 'problem' with previous funcion

  for i in range(len(problems)):
    temporary_list.append([])
  #Create a space in 'temporary_list' for each item
  #in the 'problems' list

  for i in range(len(problems)):
    Sep = problems[i].split()
    #Temporary separation of i.

    if numbers_not_ok(Sep):
      return "Error: Numbers must only contain digits."
    #Digits only check.

    if digit_quantity_not_ok(Sep):
      return "Error: Numbers cannot be more than four digits."
    #4 digits per number check.

    if operator_not_ok(Sep):
      return "Error: Operator must be '+' or '-'."
    #Operator check.

    Sep.append(operation(Sep))
    #Sep now contains ["Number1", "Operator", "Number2", Result]

    Sep.append(biggest_number_size(Sep))
    #Sep now has the size of digits from
    #the bigget number inside self.
    #Sep is ["Number1", "Operator", "Number2", Result, BN_Size]

    temporary_list[int(i)] = Sep
    #list now have contents in spec.
  #end of for and checks

  return formatting(temporary_list, response)
