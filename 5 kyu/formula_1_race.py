def swap_list_position(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def champion_rank(pilot: int, events: str) -> int:
    pilots = [str(x+1) for x in range(20)]
    events = events.split()
    for n in range(0, len(events)-1, 2):
        if events[n+1] == 'O':
            p_id = pilots.index(events[n])
            swap_list_position(pilots, p_id, p_id-1)
        if events[n+1] == 'I':
            pilots.remove(events[n])

    if str(pilot) not in pilots:
        return -1
    else:
        return pilots.index(str(pilot))+1