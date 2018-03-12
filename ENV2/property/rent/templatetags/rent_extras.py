from django import template
import datetime

register = template.Library()

@register.filter
def is_room_occupied_test(room,lease):
    is_occupied = False
    for item in lease:
        if item.lease_room.room_id == room:
            is_occupied = True
            
    return is_occupied

@register.filter
def is_room_occupied(room,lease):
    is_occupied = False
    for item in lease:
        if item.lease_room.room_id == room and current_month_record(item):
            is_occupied = True
            
    return is_occupied

@register.filter
def get_matching_record(data_list,room):
    return data_list.filter(lease_room=room)

@register.filter
def get_lease_by_room(lease_details,room):
    for item in lease_details:
        if item.lease_room.room_id == room and current_month_record(item):
            return item                


def current_month_record(item):
    today = datetime.date.today()
    compare = item.lease_start_date <= today and today <= item.lease_end_date
    if compare: 
        return True
    else:
        return False