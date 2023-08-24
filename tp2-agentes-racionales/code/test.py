from env import Environment
from agent import Agent    

# ## Ejercicio D)
# Evaluar el desempeño del agente agente reflexivo (medida de desempeño y unidades de tiempo consumidas) para:
# 1. Entornos de: 2x2, 4x4, 8x8, 16x16, 32x32, 64x64, 128x128 
# 2. Porcentaje de Suciedad en el ambiente: 0.1, 0.2, 0.4, 0.8
# 3. Repetir 10 veces cada combinación.

# **Nota:** Se recomienda elaborar una tabla en google sheets (o algo similar) en donde se presente los resultados en términos de la medida 
# de rendimiento para cada uno de los casos. Esto luego se podrá utilizar para realizar alguna visualización de los resultados.

# ## Ejercicio E)
# Repetir el procedimiento descrito en el punto C, para el caso de un agente con comportamiento totalmente aleatorio.  En cada periodo de tiempo,
#  el agente toma una acción al azar.

size = [2, 4, 8, 16, 32, 64, 128]
dirt_rate = [0.1, 0.2, 0.4, 0.8]

f = open("testResults.txt", "w+")

for s in size:
    f.write("Tamaño %dx%d \n" %(s, s))
    print(s)
    n = s**2 # num de casillas
    for d in dirt_rate:
        f.write("Porcentaje de Suciedad en el ambiente: %f \n" %d)
        cT = 0
        dT = 0
        pT = 0
        for i in range(10):
            f.write("Simulación n°%d: \n" %(i + 1))
            env = Environment(s, s, d)
            env.printEnv()
            agent = Agent(env)

            while agent.getTotalLife() > 0:
                agent.think()
                agent.env.printEnv()

            c = agent.getTotalCleaned()
            cT += c
            f.write(" Total limpiado: %d \n" %c)

            d = env.getInitDirt()
            dT += d
            f.write(" Suciedad inicial: %d \n" %d)

            p = agent.getPerformance()
            pT += p
            f.write(" Porcentaje de suciedad limpiada: %f%% \n" %p)

            print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")

        f.write("Promedio limpiado: %f \n" %(cT/10))
        f.write("Promedio suciedad inicial: %f \n" %(dT/10))
        f.write("Promedio porcentaje de suciedad limpiadas: %f \n" %(pT/10))

        f.write("-------------------------------------------------------------------------------------------------------------------\n")

    f.write("===================================================================================================================\n")

f.close()