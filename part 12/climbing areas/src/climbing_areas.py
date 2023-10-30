class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

class ClimbingArea:
    def __init__(self, name: str):
        self.name = name
        self.__routes = []

    def add_route(self, route: ClimbingRoute):
        self.__routes.append(route)

    def routes(self):
        return len(self.__routes)

    def hardest_route(self):
        def by_difficulty(route):
            return route.grade

        routes_in_order = sorted(self.__routes, key=by_difficulty)
        # last route
        return routes_in_order[-1]




def sort_by_number_of_routes(areas: list):
    def new_order(a: ClimbingArea):
        return a.routes()
    return sorted(areas, key= new_order)



def sort_by_most_difficult(areas: ClimbingArea):
    def new_order(area: ClimbingArea):
        return area.hardest_route().grade, area.hardest_route().length
    return sorted(areas, key=new_order,reverse=True)
