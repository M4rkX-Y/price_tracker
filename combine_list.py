import cpudb

def combine():
    amz_cpu = cpudb.get_amz_all()
    nwe_cpu = cpudb.get_nwe_all()
    url = []
    availability = []
    price = []
    i=0
    all=[]

    for cpu1 in nwe_cpu:
        url.append(cpu1[0])
        availability.append(cpu1[1])
        price.append(cpu1[2])

    for cpu2 in amz_cpu:
        product = list(cpu2)
        product.append(url[i])
        product.append(availability[i])
        product.append(price[i])
        all.append(product)
        i=i+1
    
    return all


