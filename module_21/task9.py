def move(disks, x_tower, y_tower, z_tower):
    if disks == 1:
        action = '{disk} - {start} - {stop}'.format(
            disk=1,
            start=x_tower,
            stop=y_tower
        )
        print(action)
        return
    else:
        move(disks - 1, x_tower, z_tower, y_tower)
        action = '{disk} - {start} - {stop}'.format(
            disk=disks,
            start=x_tower,
            stop=y_tower
        )
        print(action)
        move(disks - 1, z_tower, y_tower, x_tower)


disk_amt = int(input('Кол-во дисков: '))
start_tower = int(input('С какой башни переносим (1, 2, 3): '))
stop_tower = int(input('На какую башню переносим (1, 2, 3): '))

towers = [1, 2, 3]
auxiliary_tower = 0
for tower in towers:
    if tower != start_tower and tower != stop_tower:
        auxiliary_tower = tower
        break

move(disk_amt, start_tower, stop_tower, auxiliary_tower)

