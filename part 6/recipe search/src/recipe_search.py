def recipes_reader(fileName: str):
    x = []
    dic_to_return = {}
    with open(fileName) as file_name:
        for line in file_name:
            line = line.strip()
            if len(line) == 0 :
                dic_to_return[x[0]] = x[1:]
                x = []
                continue
            x.append(line)
        dic_to_return[x[0]] = x[1:]
    
    return dic_to_return



def search_by_name(fileName: str, word: str):
    dic = recipes_reader(fileName)
    list_to_return = []
    for key in dic :
        k = str(key)
        if word in k.lower():
            list_to_return.append(key)
    return list_to_return


def search_by_time(fileName: str, prep_time: int):
    dic = recipes_reader(fileName)
    list_to_return = []
    for key in dic :
        time = int(dic[key][0])
        if time <= prep_time:
            x = f"{key}, preparation time {time} min"
            list_to_return.append(x)
    return list_to_return
            

def search_by_ingredient(fileName: str, ingredient: str):
    dic = recipes_reader(fileName)
    list_to_return = []
    for key in dic :
        if ingredient in dic[key] :
            x = f"{key}, preparation time {int(dic[key][0])} min"
            list_to_return.append(x)
    return list_to_return



if __name__ == "__main__" :
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)