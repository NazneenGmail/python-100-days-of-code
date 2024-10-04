import US_States_List_In_Order_of_Joining_Union
print(f"First State: {US_States_List_In_Order_of_Joining_Union.states_list[0]}")
print(f"Second State: {US_States_List_In_Order_of_Joining_Union.states_list[1]}")
print(f"Last State: {US_States_List_In_Order_of_Joining_Union.states_list[-1]}")
print(f"Second Last State: {US_States_List_In_Order_of_Joining_Union.states_list[-2]}")

US_States_List_In_Order_of_Joining_Union.states_list[1] = 'Pencilvania'
print(f"\nFunny name changed: {US_States_List_In_Order_of_Joining_Union.states_list[1]}")
US_States_List_In_Order_of_Joining_Union.states_list[1] = 'Pennsylvania'
print(f"Restored correct name: {US_States_List_In_Order_of_Joining_Union.states_list[1]}")

US_States_List_In_Order_of_Joining_Union.states_list.append('I am a new state')
print(f"\nAdd new state to end of states list. '{US_States_List_In_Order_of_Joining_Union.states_list[-1]}'")
US_States_List_In_Order_of_Joining_Union.states_list.remove('I am a new state')
print(f"New state removed. Now last state is back to :'{US_States_List_In_Order_of_Joining_Union.states_list[-1]}'")

print(f"\nList length: {len(US_States_List_In_Order_of_Joining_Union.states_list)}")
print(f"\nAccess Last List Item: "
      f"{US_States_List_In_Order_of_Joining_Union.states_list[len(US_States_List_In_Order_of_Joining_Union.states_list) - 1]}")