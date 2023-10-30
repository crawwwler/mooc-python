def sort_by_remaining_stock(items: list):
    def ordered_by_rs(t: tuple):
        return t[2]
    return sorted(items, key=ordered_by_rs)