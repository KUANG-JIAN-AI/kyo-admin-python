from datetime import datetime


def format_time(ts):
    if not ts:
        return None
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")


def handle_page(page, pagination):
    pages = pagination.pages
    if pages <= 10:
        return list(range(1, pages + 1))

    if page > pages - 5:
        return [1, "..."] + list(range(pages - 5, pages + 1))
    elif page > 4:
        return [1, "...", page - 2, page - 1, page, page + 1, page + 2, "...", pages]
    else:
        return list(range(1, 11)) + ["...", pages]
