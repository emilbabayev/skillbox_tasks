stall_info = input('Введите 10 стойл в одну строку. a — свободное стойло, b — занятое:\n')
milk_produced = 0

for stall_id, stall_status in enumerate(stall_info, start=1):
    if stall_status == 'b':
        milk_produced += stall_id * 2

print(f'Произведено молока в день: {milk_produced}')