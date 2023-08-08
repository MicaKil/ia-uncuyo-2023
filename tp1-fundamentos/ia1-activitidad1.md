# Actividad Preliminar I
**Estudiante:** Del Longo, Micaela (11653)
## Analizar y responder las siguiente preguntas:
### 1. Buscar 2 ejemplos de aplicaciones de inteligencia artificial.
**Wildlife Insights**

Wildlife Insights utiliza a la IA para reducir el tiempo necesario para pasar los datos de trampas fotográficas en información útil sobre la biodiversidad. Cualquiera que recolecte datos de trampas fotográficas puede utilizar Wildlife Insights para cargar los datos en Google Cloud y acceder a modelos de IA entrenados para clasificar automáticamente las imágenes de las trampas fotográficas. Su objetivo es ayudar en el monitoreo y protección de especies en riesgo de extinción.

<p align="center">
  <img src="image.png" alt="Un tigre de Sumatra captado por una cámara"/>
</p>
<p style="text-align: center; font-style:italic;"> Un tigre de Sumatra captado por una trampa fotográfica. </p>

El modelo de IA se entrena utilizando la biblioteca de código abierto TensorFlow de Google.

La IA ayuda a:

1. **Filtrar imágenes en blanco (imágenes sin un animal):** El modelo clasifica las imágenes como en blanco solo cuando tiene certeza, reduciendo la posibilidad de eliminar imágenes valiosas de animales.

2. **Clasificar animales:** Los modelos buscan proporcionar una predicción en el nivel taxonómico más bajo en el que tienen confianza. Por ejemplo, si los modelos están seguros de que hay un ciervo en la imagen, pero no están seguros de la especie exacta de ciervo, mostrarán "ciervo" como la predicción.

**Ciberseguridad**

La inteligencia artificial se utiliza en ciberseguridad para detectar y responder a amenazas cibernéticas en tiempo real. Los algoritmos de IA pueden analizar grandes cantidades de datos y detectar patrones que son indicativos de una amenaza.

Los enfoques tradicionales de ciberseguridad se basan en sistemas de detección basados en firmas que solo son efectivos contra amenazas conocidas. Por otro lado, las soluciones basadas en IA utilizan algoritmos de *machine learning* que pueden detectar y responder tanto a amenazas conocidas como desconocidas en tiempo real.

Estos algoritmos se entrenan con una gran cantidad de datos para identificar patrones difíciles de percibir para los humanos. A medida que surgen nuevas amenazas, los algoritmos de *machine learning* se entrenan con nuevos datos para mejorar su capacidad de detección y respuesta.

### 2. ¿Qué se entiende por inteligencia artificial?

Existen cuatro aproximaciones para definir la IA:

1. <span style="color:hotpink">**Pensar**</span> **de Forma** <span style="color:lightskyblue"> **Humana**</span>
   
   *"El emocionante nuevo esfuerzo por hacer que las computadoras piensen... máquinas con mentes, en el sentido completo y literal." (Haugeland, 1985)*

   *"La automatización de actividades que asociamos con el pensamiento humano, actividades como la toma de decisiones, la resolución de problemas, el aprendizaje..." (Bellman, 1978)*

2. <span style="color:hotpink">**Pensar**</span> <span style="color:lightgreen">**Racionalmente** </span> 

    *"El estudio de las facultades mentales a través del uso de modelos computacionales." (Charniak y McDermott, 1985)*

    *"El estudio de los cálculos que permiten percibir, razonar y actuar." (Winston, 1992)*

3. <span style="color:plum">**Actuar** </span> **de Forma** <span style="color:lightskyblue"> **Humana**</span>

    *"El arte de crear máquinas que realizan funciones que requieren inteligencia cuando son realizadas por personas." (Kurzweil, 1990)*

    *"El estudio de cómo hacer que las computadoras hagan cosas en las que, en este momento, las personas son mejores." (Rich y Knight, 1991)*

4. <span style="color:plum">**Actuar** </span> <span style="color:lightgreen">**Racionalmente** </span> 

    *"La Inteligencia Computacional es el estudio del diseño de agentes inteligentes." (Poole et al., 1998)*

    *"La IA... se preocupa por el comportamiento inteligente en artefactos." (Nilsson, 1998)*

Las definiciones de los ítems 1 y 2 se enfocan en el proceso de **pensamiento** y **razonamiento**, mientras que las de los ítems 3 y 4 se enfocan en el **comportamiento**.  Las de los ítems 1 y 4 miden el éxito en términos de fidelidad al rendimiento **humano**, mientras que las de los ítems 2 y 3 se mide frente a una medida de rendimiento **ideal** llamada **racionalidad**. Un sistema es racional si hace lo "correcto", considerando lo que sabe.

### 3. ¿Qué se entiende por Inteligencia?

La inteligencia puede entenderse como la capacidad tanto de entender o comprender como de resolver problemas.

Sin embargo, en la actualidad se ha aceptado que no existe un concepto único de inteligencia, sino que existen numerosas formas de ella.

Howard Gardner, creador de la teoría de las inteligencias múltiples, propuso varios tipos de inteligencia:

1. Inteligencia **lingüístico-verbal**
   
   Las personas con mayor inteligencia lingüístico-verbal tienen facilidad para aprender nuevos idiomas, hablar y escribir de manera eficaz y sobresaliente, y tener en líneas generales una comprensión del lenguaje verbal que está más allá de lo común.

2. Inteligencia **lógico-matemática**

    Este tipo de inteligencia implica los razonamientos abstractos no verbales. Son, por ejemplo, aquellos que involucran el cálculo, la percepción geométrica, el reconocimiento de patrones numéricos o lógicos, o el manejo de mecanismos de raciocinio formal, como las matemáticas, la lógica, la física, la química, entre otras ciencias exactas y aplicadas.

3. Inteligencia **espacial o visual**

    En esta categoría se encuentra la capacidad para manejar órdenes espaciales abstractas, empleando para ello la imaginación y el sentido de la orientación o de la lógica.

    Se aplica a la hora de utilizar eficientemente mapas, coordenadas y orientaciones. Además, permite imaginar un objeto desde un ángulo de percepción distinto al que se tiene, o para crear una perspectiva propia.

4. Inteligencia **musical**

    Este tipo de inteligencia implica una cierta percepción del ritmo, así como una interrelación estrecha entre el oído y la mente, que permite comprender, distinguir y seguir patrones rítmicos, o incluso crearlos.

5. Inteligencia **corporal-kinestésica**
    
    Se trata de la inteligencia aplicada a la coordinación de los movimientos del cuerpo, lo cual se extiende también al uso de sus herramientas.

6. Inteligencia **intrapersonal**
    
    Este es un tipo de inteligencia introspectiva, tiende a la examinación de los aspectos interiores del individuo. Esto pasa por reconocer las propias emociones, sentimientos, las lógicas que rigen la conducta, y de esa manera poder organizarlas, elegirlas y aplicar la “inteligencia emocional”.

7. Inteligencia **interpersonal**
    
    Al contrario de la anterior, esta se refiere a los aspectos del trato con los demás, es decir, la capacidad de establecer vínculos efectivos con otros seres humanos y reconocer sus emociones, sus pensamientos, y brindarles una respuesta adecuada.

    La inteligencia interpersonal implica altos niveles de empatía, de carisma o de manipulación. 

8. Inteligencia **naturalista**

    Se la define como la capacidad para observar y comprender las relaciones propias de la naturaleza y el medio ambiente, o reconocer sus patrones.
    
### 4. ¿Qué se entiende por artificial?

Se trata de un adjetivo que alude a aquello que es fabricado por el hombre: es decir, que no procede de la naturaleza. Artificial también es lo que resulta falso, ilusorio o simulado.
## Fuentes

- Wildlife Insights. Recuperado de https://www.wildlifeinsights.org/
- Sonya Moisset. How to Use Artificial Intelligence in Cybersecurity. FreeCodeCamp. Recuperado de https://www.freecodecamp.org/news/how-to-use-artificial-intelligence-in-cybersecurity/
- Russell, S. J., & Norvig, P. (2009). Artificial Intelligence: A Modern Approach (3rd ed.). Prentice Hall.
- Teoría de las Inteligencias Múltiples. Concepto. Recuperado de https://concepto.de/teoria-de-las-inteligencias-multiples/
- Inteligencia. Concepto. Recuperado de https://concepto.de/inteligencia/
- Artificial. Definición. Recuperado de https://definicion.de/artificial/