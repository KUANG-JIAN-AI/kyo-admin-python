from datetime import datetime


def format_time(ts):
    if not ts:
        return None
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")


def handle_page(page, pagination):
    paginate = []
    if pagination.pages > 10:
        if page > pagination.pages - 5:
            paginate = [
                1,
                "...",
                pagination.pages - 5,
                pagination.pages - 4,
                pagination.pages - 3,
                pagination.pages - 2,
                pagination.pages - 1,
                pagination.pages,
            ]
        elif page > 4:
            paginate = [
                1,
                "...",
                page - 2,
                page - 1,
                page,
                page + 1,
                page + 2,
                "...",
                pagination.pages,
            ]
        else:
            paginate = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "...", pagination.pages]
    else:
        for i in pagination.pages:
            paginate.append(i)
    return paginate
