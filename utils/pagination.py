import math


def make_pagination_range(page_range, qty_pages, current_page):

    middle_range = math.ceil(qty_pages / 2)
    start_rage = current_page - middle_range
    stop_rage = current_page + middle_range
    total_pages = len(page_range)

    start_range_offset = abs(start_rage) if start_rage < 0 else 0

    if start_rage < 0:
        start_rage = 0
        stop_rage += start_range_offset

    if stop_rage >= total_pages:
        start_rage = start_rage - abs(total_pages - stop_rage)


    pagination = page_range[start_rage:stop_rage]
    return {
        "pagination": pagination,
        "page_range": page_range,
        "qty_pages": qty_pages,
        "current_page": current_page,
        "total_pages": total_pages,
        "start_range": start_rage,
        "stop_range": stop_rage,
        "first_page_out_of_range": current_page > middle_range,
        "last_page_out_of_range": stop_rage < total_pages
    }