def filter_forbidden(sentence: str, forbidden: str):
    return "".join([c for c in sentence if not c in forbidden])