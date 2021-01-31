#!/usr/bin/env python3

'''
Tools for IceGauntlet Dungeon server
'''

import json


# Following definitions are taken from game/common.py
KEY = 119
TREASURE = 121
EXIT = 101
TELEPORT = 38
HAM = 116
JAR = 113

DOORS = list(range(19, 34))

EMPTY_TILE = 48
NULL_TILE = 255

DEFAULT_SPAWN = 250
WARRIOR_SPAWN = DEFAULT_SPAWN + 1
VALKYRIE_SPAWN = DEFAULT_SPAWN + 2
WIZARD_SPAWN = DEFAULT_SPAWN + 3
ELF_SPAWN = DEFAULT_SPAWN + 4
SPAWN_IDS = [DEFAULT_SPAWN, WARRIOR_SPAWN, VALKYRIE_SPAWN, WIZARD_SPAWN, ELF_SPAWN]

AVAILABLE_OBJECT_IDS = [KEY, TREASURE, EXIT, TELEPORT, HAM, JAR] + DOORS + SPAWN_IDS

# Taken from game/room.py
_DOOR_DIRECTION_ = {
    19: [(0, -1)],
    20: [(1, 0)],
    21: [(0, -1), (1, 0)],
    22: [(0, 1)],
    23: [(0, -1), (0, 1)],
    24: [(1, 0), (0, 1)],
    25: [(0, -1), (1, 0), (0, 1)],
    26: [(-1, 0)],
    27: [(-1, 0), (0, -1)],
    28: [(-1, 0), (1, 0)],
    29: [(0, -1), (-1, 0), (1, 0)],
    30: [(-1, 0), (0, 1)],
    31: [(0, -1), (-1, 0), (0, 1)],
    32: [(-1, 0), (0, 1), (1, 0)],
    33: [(0, -1), (-1, 0), (0, 1), (1, 0)]
}


def get_map_objects(room):
    '''Get list of available objects in the room'''
    room = json.loads(room)
    objects = []
    row = 0
    for map_row in room['data']:
        column = 0
        for tile in map_row:
            if tile in AVAILABLE_OBJECT_IDS:
                objects.append((tile, (column, row)))
            column += 1
        row += 1
    return objects


def filter_map_objects(room):
    '''Return a map without objects (walls)'''
    room = json.loads(room)
    filtered_map = []
    for row in room['data']:
        filtered_row = []
        for tile in row:
            if (tile in AVAILABLE_OBJECT_IDS) or (tile == NULL_TILE):
                filtered_row.append(EMPTY_TILE)
            else:
                filtered_row.append(tile)
        filtered_map.append(filtered_row)
    room['data'] = filtered_map
    return json.dumps(room)


def search_adjacent_door(items, position, visited=None):
    '''Return the list of door tiles adjacent to a given one'''

    def door_at(position):
        for item_id in items:
            item_type, item_position = items[item_id]
            if position == item_position:
                if item_type in DOORS:
                    return item_id, item_type
        return None, None

    if not visited:
        visited = []
    if position in visited:
        return []
    visited.append(position)
    door_id, door_type = door_at(position)
    if not door_id:
        return []
    doors = {door_id}
    column, row = position
    for dir_x, dir_y in _DOOR_DIRECTION_[door_type]:
        doors = doors.union(search_adjacent_door(items, (column + dir_x, row + dir_y), visited))
    print(f'Adjacent doors: {doors}')
    return doors
