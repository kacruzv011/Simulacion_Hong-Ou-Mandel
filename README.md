Simulación Cuántica: Interferencia de Dos Partículas (Bosones, Fermiones y Distinguibles)

Este proyecto implementa una simulación numérica del fenómeno de interferencia de dos partículas inspirado en el experimento de Hong–Ou–Mandel (HOM), modelando la interacción mediante un potencial Delta de Dirac y propagación cuántica en 1D.

El código genera una animación completa donde se muestran:

La función de probabilidad para bosones (simétrica)

La función de probabilidad para fermiones (antisimétrica)

El caso distinguible

La función de correlación local 
𝑔
(
2
)
(
𝑥
,
𝑥
)
g
(2)
(x,x)

La probabilidad de coincidencia en la diagonal 
𝑃
(
𝑥
1
=
𝑥
2
)
P(x
1
	​

=x
2
	​

)

La distribución de separaciones 
∣
𝑥
1
−
𝑥
2
∣
∣x
1
	​

−x
2
	​

∣

La simulación permite visualizar:

Bunching en bosones

Anti-bunching en fermiones

La diferencia fundamental entre partículas cuánticas simétricas, antisimétricas y distinguibles.

🧠 Fundamento físico

El experimento HOM clásico estudia cómo dos fotones idénticos interfieren al cruzar un divisor de haz 50/50.
Aquí replicamos un análogo en 1D, donde usamos:

Paquetes gaussianos como estados iniciales

Un potencial delta que actúa como barrera/dispersor

Propagación temporal vía FFT

Construcción del estado bipartícula:

Ψ
𝐵
=
1
2
(
𝜓
1
(
𝑥
1
)
𝜓
2
(
𝑥
2
)
+
𝜓
1
(
𝑥
2
)
𝜓
2
(
𝑥
1
)
)
Ψ
B
	​

=
2
	​

1
	​

(ψ
1
	​

(x
1
	​

)ψ
2
	​

(x
2
	​

)+ψ
1
	​

(x
2
	​

)ψ
2
	​

(x
1
	​

))
Ψ
𝐹
=
1
2
(
𝜓
1
(
𝑥
1
)
𝜓
2
(
𝑥
2
)
−
𝜓
1
(
𝑥
2
)
𝜓
2
(
𝑥
1
)
)
Ψ
F
	​

=
2
	​

1
	​

(ψ
1
	​

(x
1
	​

)ψ
2
	​

(x
2
	​

)−ψ
1
	​

(x
2
	​

)ψ
2
	​

(x
1
	​

))
📦 Requisitos

El código utiliza únicamente librerías estándar:

pip install numpy matplotlib

▶️ Ejecución

Simplemente corre el script:

python simulacion_HOM.py


El programa:

Inicializa parámetros físicos y numéricos

Construye paquetes gaussianos

Propaga ambos paquetes en el tiempo

Construye los estados bosónico, fermiónico y distinguible

Calcula correlaciones y secciones diagonales

Genera y guarda una animación .gif

🎞️ Salida

El programa intenta guardar automáticamente:

simulacion_cuantica_corregida.gif


Si el guardado falla, se abrirá la animación en una ventana interactiva.

📁 Estructura del repositorio (sugerida)
/
├── simulacion_HOM.py
├── README.md
└── simulacion_cuantica_corregida.gif   (opcional)

🧩 Principales componentes del código
1️⃣ Paquetes gaussianos

Sean los estados iniciales desplazados en ±x:

gaussian_wave_packet(x, s0, k0)

2️⃣ Coeficientes de transmisión y reflexión

Para un potencial Delta:

𝑇
=
1
1
+
𝑖
𝛽
,
𝑅
=
−
𝑖
𝛽
1
+
𝑖
𝛽
T=
1+iβ
1
	​

,R=−
1+iβ
iβ
	​

3️⃣ Propagación temporal

Usamos FFT para evolución libre:

𝑒
−
𝑖
𝑘
2
𝜏
e
−ik
2
τ

Y mezclamos transmisión/reflexión mediante una sigmoide suave.

4️⃣ Construcción de los estados bipartícula

Bosones (simetría)

Fermiones (antisimetría)

Distinguibles

5️⃣ Cálculo de:

Densidad conjunta 
∣
Ψ
(
𝑥
1
,
𝑥
2
)
∣
2
∣Ψ(x
1
	​

,x
2
	​

)∣
2

Diagonal 
𝑃
(
𝑥
1
=
𝑥
2
)
P(x
1
	​

=x
2
	​

)

Correlación 
𝑔
(
2
)
(
𝑥
,
𝑥
)
g
(2)
(x,x)

Distribución de separaciones

📊 Visualizaciones generadas

La animación muestra seis paneles:

Bosones — interferencia constructiva (bunching)

Fermiones — exclusión de Pauli (anti-bunching)

Distinguibles — sin efectos cuánticos

Correlación local 
𝑔
(
2
)
(
𝑥
,
𝑥
)
g
(2)
(x,x)

Diagrama de coincidencia

Distribución de separación

🧪 Limitaciones y aproximaciones

La inversión de dirección se aproxima mediante un flip espacial

La mezcla entre regiones incidente/reflejada/transmitida usa una sigmoide suave

Se asume 
ℏ
=
1
ℏ=1 y 
2
𝑚
=
1
2m=1

La propagación no usa split-operator completo (más costoso)

Aun así, reproduce cualitativamente:

HOM-like bunching

Antibunching fermiónico

Dinámica onda–barrera realista

📝 Autor

Simulación elaborada por George como exploración computacional de interferencia cuántica multipartícula.

📌 Licencia

MIT — libre uso y modificación con atribución.

🤖 Uso de Inteligencia Artificial

Este README y partes auxiliares del diseño fueron elaborados con asistencia de modelos de lenguaje de inteligencia artificial.
El contenido técnico del código, conceptos físicos y ajustes numéricos deben ser revisados por especialistas antes de emplearse en investigación formal o publicaciones científicas.
