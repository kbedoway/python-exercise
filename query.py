from movies import Movies

movies = Movies('./movies.txt')

print("--------------------------")
print("q: quit")
print("sn: search movie names")
print("sc: search cast members")
print("list: list all movie names")
print("--------------------------")

# list all movies names with input included in name
def sn_func(movie_name):
    import linecache
    i = 1
    while i < 300:
        content = linecache.getline('movies.txt', i)
        if movie_name.lower() in content.lower():
            print(content, end="")
        i += 3

# list all cast members with input included in name
def sc_func(cast):
    import linecache
    i = 2
    while i < 300:
        content = linecache.getline('movies.txt', i)
        if cast.lower() in content.lower():
            prev_content = linecache.getline('movies.txt', i - 1)
            split_content = content.split(",")
            ci_content = content.lower() # case insensitive
            ci_split_content = ci_content.split(",")

            split_array = []
            j = 0
            for j in split_content:
                split_array.append(j)
            
            ci_split_array = []
            j = 0
            for j in ci_split_content:
                ci_split_array.append(j)           

            k = 0
            while k < len(ci_split_content):
                if cast.lower() in ci_split_content[k]:
                    print(prev_content, end="")
                    print("[", split_content[k], "]")
                k += 1
        i += 3

# list all movie names
def list_func():
    import linecache
    i = 1
    while i < 300:
        content = linecache.getline('movies.txt', i)
        print(content, end="")
        i += 3

# beginning of while
while True:
    print()
    option = input("Enter an option: ")

    # quit
    if option == "q":
        break

    # search movie names
    elif option == "sn":
        movie_name = input("Enter a word to search: ")
        sn_func(movie_name)

    # search cast
    elif option == "sc":
        cast = input("Enter a name to search: ")
        sc_func(cast)

    # print all movie names
    elif option == "list":
        list_func()
        continue

    # invalid option
    else:
        print("Invalid option, try again.")
# end of while
