# Proyecto Sprint 2

# Paso 1: Limpieza inicial de un registro de cliente
# Este paso sirve como base para entender los elementos clave de un registro antes de escalar el proceso al resto de los usuarios.

# Queremos aplicar las siguientes transformaciones:

# Eliminar espacios en blanco y guiones bajos (_) del nombre del usuario.
# Dividir el nombre en una lista separando nombre y apellido.
# Convertir la edad del usuario a un número entero.
# Instrucciones:

# Usa la variable user predefinida.
# Modifica los valores directamente en esa lista.
#Muestra el resultado final con print(user).

# Usuario de ejemplo
user = ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]]

# Paso 1: limpiar y dividir el nombre
user[1] = user[1].strip().replace('_', ' ')# escribe tu código aquí

# Paso 2: dividir el nombre en una lista
user[1]  = user[1].split()# escribe tu código aquí

# Paso 3: convertir la edad a entero
user[2] = int(user[2])# escribe tu código aquí

# Mostrar resultado
print(user)






#Paso 2: Convertir las categorías a minúsculas
#En los datos actuales, las categorías favoritas de los clientes están escritas completamente en mayúsculas. Este formato puede causar inconsistencias en análisis posteriores, como al agrupar, filtrar o contar categorías. Para garantizar una lectura uniforme y facilitar futuras operaciones, es necesario normalizar estos valores a minúsculas.

#En este paso, trabajaremos con una lista de ejemplo llamada fav_categories y construiremos una nueva lista llamada fav_categories_low, que contendrá las versiones en minúsculas de cada categoría.

#Instrucciones:

#Crea una nueva lista donde cada categoría esté en minúscula.

#Usando un bucle, recorre y transforma cada elemento de la lista con las categorias en mayuscula para que queden en minuscula.

#Anade cada elemento a la nueva lista fav_categories_low

#Muestra el resultado utilizando print para verificar que la conversión fue exitosa.

# Lista original de categorías favoritas escritas en mayúsculas
fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']

# 1. Lista vacía donde almacenaremos las categorías convertidas a minúsculas
fav_categories_low = []

# 2. Recorremos cada categoría en la lista original
for category in fav_categories:# escribe tu código aquí
    # 2. Convertimos la categoría a minúscula utilizando el método lower()
    lowered_category = category.lower() #variable de for
    fav_categories_low.append(lowered_category)# escribe tu código aquí

# 4. Mostramos en pantalla la lista resultante con las categorías en minúsculas
print(fav_categories_low)









# Paso 3: Limpieza completa de un usuario
# Ahora vamos a empaquetar todo ese proceso dentro de una función reutilizable.

# Crea una función llamada clean_user(user) que realice estas acciones:

# Limpie espacios y guiones del nombre y lo divida en nombre/apellido.
# Convierta la edad a entero.
# Convierta las categorías a minúsculas.
# Usa el mismo código que escribiste en los pasos anteriores. Solo necesitas ajustarlo para que funcione dentro de una función.

# Prueba tu función con el usuario test_user y muestra el resultado.



def clean_user(user):
    # Limpia y divide el nombre
    name = user[1].strip().replace('_',' ').split()# escribe tu código aquí

    # Edad como entero
    age = int(user[2])# escribe tu código aquí  # noqa: F821

    # Categorías a minúsculas

    categories = []
    for cat in user [3]:# escribe tu código aquí
        categories.append(cat.lower())# escribe tu código aquí

    return [user[0], name, age, categories, user[4]]

# Prueba
test_user = ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]]
print(clean_user(test_user))



# Paso 4: Limpieza de toda la base de usuarios
# Ya tienes la función clean_user() funcionando correctamente. Ahora es momento de aplicarla a todos los registros de clientes.

# Itera sobre la lista users_raw,
# Usa la función clean_user() para limpiar cada usuario,
# Guarda los resultados en una nueva lista llamada users_clean.
# Al final, imprime users_clean para verificar que todos los usuarios han sido transformados correctamente.


def clean_user(user):
    name = user[1].lower().strip().replace('_',' ').split()

    age = int(user[2])

    categories = []
    for cat in user [3]:
        categories.append(cat.lower())

    return [user[0], name, age, categories, user[4]]


users_raw = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]]
]

users_clean = []

for user in users_raw:
    cleaned_user = clean_user(user)
    users_clean.append(cleaned_user)


print(users_clean)
































# Paso 5: Calcular ingresos totales
# Ahora que tienes todos los registros de clientes limpios, el siguiente paso es comenzar a generar insights que puedan ayudar a la empresa a tomar decisiones estratégicas.

# La empresa desea conocer sus ingresos totales.

# Para calcular los ingresos de la empresa, sigue estos pasos:

# Crea una variable revenue con valor inicial 0.
# Itera sobre la lista users_clean con un bucle for.
# En cada iteración, extrae la lista de gastos de cada usuario (la última posición de la sublista).
# Suma esos valores con sum() y añádelos a revenue.
# Al finalizar, imprime el resultado final para mostrar el ingreso total generado por todos los usuarios.

users_clean = [['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
         			 ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
         			 ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
         			 ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
         			 ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
         			 ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
         			 ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
         			 ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
         			 ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
         			 ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]]

revenue = 0

for gastos in users_clean:
    totales = gastos[4]
    revenue += sum(totales)
    
print(revenue)



# Paso 6: Usuarios menores de 30 años
# El equipo de marketing quiere segmentar a los usuarios jóvenes para campañas específicas. Vamos a identificarlos.

# Recorre la lista de usuarios users_clean que has preparado anteriormente y muestra los nombres de los clientes menores de 30 años.

# Pasos:
# Escribe un bucle for que recorra cada usuario en users_clean.

# Agrega una condición if para seleccionar a los usuarios menores de 30 años.

# Dentro del bloque, imprime solo el primer elemento del nombre del usuario.

# 📌 Recuerda:

# Si un elemento dentro de la lista contiene otra lista (como el nombre del usuario), puedes acceder a sus valores usando múltiples índices. Primero accede a la posición del nombre completo, y luego selecciona la parte específica que quieras mostrar.

# Al ejecutar el código, deberás ver los nombres de los usuarios menores de 30 años.


for edades in users_clean:
    if edades[2] < 30:
        print(edades[1][0])





# Paso 7: Jóvenes con alto gasto
# Ahora filtraremos a los usuarios jóvenes que también han gastado mucho dinero, para que la empresa pueda identificarlos y darles beneficios especiales.

# Debajo tienes la lista users_clean con todos los datos procesados.

# Pasos:
# Escribe un bucle for que recorra cada usuario en users_clean.
# Calcula el total gastado por cada usuario (suma de la lista de gastos).
# Usa una condición if para mostrar solo los usuarios menores de 30 años y con un gasto total superior a $1000.
# Imprime solo la primera parte del nombre de cada usuario que cumpla ambos criterios.
for user in users_clean:
    totales = user[4]
    sumatoria = sum(totales)

    if user[2] < 30 and sumatoria > 1000:
        print(user[1][0])





# Paso 8: Usuarios que compraron ropa
# Store 1 también está explorando patrones de compra por categoría. Comenzamos con la categoría "clothes".

# Debajo tienes la lista users_clean con toda la información de compras ya procesada.

# Pasos:
# Escribe un bucle for que recorra cada usuario en users_clean.
# Usa una condición if para verificar si "clothes" está entre las categorías compradas.
# Si cumple la condición, imprime el nombre del usuario y su edad en la misma línea.

for user in users_clean:
    if 'clothes' in user[3]:
        print(user[1][0], user[2])



# Paso 9: Función con filtro por categoría
# Para automatizar el análisis por categoría, implementaremos una función reutilizable que permita obtener los clientes que hayan comprado en una categoría específica.

# Debajo tienes el nombre de la función y una prueba ya preparada con la categoría "home". Solo necesitas completar el cuerpo de la función.

# Pasos:
# Completa la definición de la función get_clients_by_category con dos argumentos: una lista de usuarios y una categoría a buscar.

# Dentro de la función:

# Crea una lista vacía para guardar los resultados.
# Recorre cada usuario con un bucle for.
# Usa una condición if para verificar si la categoría está en su lista de compras.
# Si se cumple la condición, agrega a la lista de resultados una sublista con su ID, nombre completo, edad y gasto total.
# Devuelve la lista resultante al final de la función

users_clean = [['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
         			 ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
         			 ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
         			 ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
         			 ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
         			 ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
         			 ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
         			 ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
         			 ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
         			 ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]]

def usuario_completo(users, category):
    usuarios_filtrados = []
    cat = category
    
    for user in users:
        categoria = user[3]
        if cat in categoria:
                id = user[0]
                name = user[1]
                age = user[2]
                gasto_final = sum(user[4])
                usuarios_filtrados.append([id, name, age, gasto_final])
    return usuarios_filtrados

clientes_home = usuario_completo(users_clean, 'home')
print(clientes_home)