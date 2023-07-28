The point of this exercise was to manipulate data objects of a dictionary. A dictionary is a data set that carries data values that are corresponding to the key, that represents them. So the key is what is a unique description of the data and the value is what the key represents, as a result. 

For example, if the key is "name" then the value would be the person's name. Both data would have to be listed in that dictionary as a variable, such as person1 or maybe an ID number. The usefulness of the dictionary, is like any other object that carries key and value, as is a data object in JavaScript. They are the same thing, but used in different coding languages with slightly different syntax to display data in the real world. 

A way a dictionary is displayed, is that a dictionary could be any variable:
    
    id_101230056 = {
        "name" : "Jesus Christos",
        "address" : "12245 Barney Rubles Blvd.",
        "city" : "Franklin",
        "state" : "IN",
        "country" : "USA",
        "gender" : "male",
    }

The key is always immutable but, value are very much mutable. A very common way to get the value is one of two ways. The first is by the use of the key:
    
    id_101230056["gender"] = "male"

and the other way is by using the .get() method:

    id_101230056.get("gender") = "male"

For more understanding of dictionary methods, please check out the python reference to dictionary methods: https://docs.python.org/3/tutorial/datastructures.html

When accessing this site, scroll down to section "5.5 Dictionaries".

The best way to manipulate the data in a dictionary is to use the for loop. Other loops can be used, such as a while loop, but the for loop is the most common case. 

There are several ways to write a for loop for a dictionary, but each with their specific use cases. 

The default use of the dictionary itself is the same as accessing the keys. They accessing the key and print them out. Here is are two examples:

    for i in id_101230056:
        print(key)

    result: 
        name
        address
        city
        state
        country
        gender

The same result is reflective of the following for loop:

    for i in id_101230056.keys():
        print(i)

By default, if a key() or value() is not stated, then the result are the key to the dictionary.

The use of the value() will result with all of the corresponding values to the keys:

    for i in id_101230056.values():
        print(i)

    result:
        Jesus Christos
        12245 Barney Rubles Blvd.
        Franklin
        IN
        USA
        male

Another use of the dictionary is to get the corresponding values to the dictionary as it would display in the real world:

    for i,j in id_101230056.items():
        print(i ":" j)

    result:
        name : Jesus Christos
        address : 12245 Barney Rubles Blvd.
        city : Franklin
        state : IN
        country : USA
        gender : male

The method used in the for loop is items() becasue it can then diplay the results with the key and values. 

In many ways a for loop can be used to display data from the dictionary in anyway that the data could be used. Any types of methods or sytax can be used to get the desired output.

In this case, the pizza prices were cahnged, because of a scenario, where market conditions were changing. The best way was to use the direct access way, where you are calling the value of the key by accessing the key itself, and using the round() to then get the pizza price in the dictionary to change. The only data that changed were the values to the keys or [Pizza].

