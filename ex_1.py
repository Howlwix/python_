def safe_div(a,b):
    try:
        return a/b
    except:
        return None
print(safe_div(2,0))