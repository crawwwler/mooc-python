def sort_by_seasons(items: list):
    def new_order(d: dict):
        return d["seasons"]
    return sorted(items, key=new_order)
