def sort_by_ratings(items: list):
    def new_order(d: dict):
        return d["rating"]
    return sorted(items, key=new_order, reverse= True)
