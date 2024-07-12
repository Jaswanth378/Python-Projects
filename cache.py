#Jaswanth Kattubavi Sreenivasulu


def fifo(requests, cache, cache_size):
        #FIFO  cache management algorithm
    for request in requests:
        if request in cache:
            print("hit")
            continue
        print("miss")
        if len(cache) >= cache_size:
            # When the cache is full, pop out the first item
            cache.pop(0)
        cache.append(request)


def lfu(requests, cache, cache_size):
    # LFU cache management algorithm
    dict = {}
    for request in requests:
        if request in dict:
            dict[request] = dict.get(request) + 1
            if request not in cache:
                if len(cache) >= cache_size:
                    # Sort cache items by frequency and remove the least frequently Requested page

                    sorted_cache_dict = sorted(dict.items(), key=lambda x: (x[1], x[0]))
                    for k, v in sorted_cache_dict:
                        if k in cache:
                            cache.remove(k)
                            break
                print("miss")
                cache.append(request)
            else:
                print("hit")
        else:
            print("miss")
            dict[request] = 1
            if len(cache) >= cache_size:
                # Sort cache items by frequency and remove the least frequently Requested page
                sorted_cache_dict = sorted(dict.items(), key=lambda x: (x[1], x[0]))
                for k, v in sorted_cache_dict:
                    if k in cache:
                        cache.remove(k)
                        break
            cache.append(request)


if __name__ == "__main__":
    while True:
        cache = []
        requests = []
        cache_size = 8

        users_input = None
        while True:
            try:
                users_input = input()
                users_input = int(users_input)
            except ValueError:
                continue
            if not users_input or users_input == 0:
                break
            requests.append(users_input)

        preference = input()
        if preference in ["1", "2"]:
            algo = fifo if preference == "1" else lfu
            algo(requests, cache, cache_size)
            print(cache)
            cache.clear()
        elif preference.upper() == "Q":
            exit()
        else:
            break