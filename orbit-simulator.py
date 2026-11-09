import matplotlib.pyplot as plt
import math

#Konstanten
M = 5.972*(10**24) #Erdmasse in kg
R = 6.371*(10**6) #Erdradius in m
G = 6.674*(10**(-11)) # Gravitationskonstante

# FG=FR
# <=> G*M*m/r**2 = m*v**2/r
# <=> v = sqrt(G*M/r)

#Startwerte setzen


r = R + 400000

x = r #am Anfang
y = 0 #am Anfang
vx = 0 #beim Start
vy = math.sqrt(G*M/r)
print("r am Anfang", r)
# Beuschleunigung:
# m*a = G*M*m/r**2
# <=> a = -G*M/r**2, da Richtung Erdmittelpunkt zeigt

#Außerdem:
# cos(a) = x/r, für X-Komponente
# sin(a) = y/r, für Y-Komponente
# => ax = a*x/r
# <=> ax = -G*M*x/(r**3)
# ax = -G*M*x/(r**3)
# ay = -G*M*y/(r**3)

dt = 0.1 #Zeitschritt in Sekunden
# alle x-Orte
xs = []
# alle y-Orte
ys = []


for i in range (60000): 
    # r**2 = x**2 + y**2, Abstand zum Erdmittelpunkt
    # r = sqrt(x**2 + y**2)
    r = math.sqrt(x**2+y**2)
    ax = -G*M*x/(r**3)
    ay = -G*M*y/(r**3)
    
    
    vx = vx + ax*dt
    vy = vy + ay*dt
    
    x = x + vx*dt
    y = y + vy*dt
    

    xs.append(x) 
    ys.append(y)
    
    
plt.plot(xs, ys)
plt.axis("equal")

#Erde zeigen
erde = plt.Circle((0, 0), R, color="green")
plt.gca().add_patch(erde)


plt.title(f"Orbit in 400 km Höhe")
plt.xlabel("x in m")
plt.ylabel("y in m")

plt.text(0, 0, "Erde", ha="center", va="center", color="white")

print("r am Ende", r)

plt.show()
    

