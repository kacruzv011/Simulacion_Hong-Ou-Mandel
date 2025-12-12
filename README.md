# Simulación Cuántica del Efecto Hong–Ou–Mandel en 1D
### Bosones • Fermiones • Partículas Distinguibles

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![NumPy](https://img.shields.io/badge/Library-NumPy-orange.svg)
![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-green.svg)

Este repositorio contiene una simulación numérica del **efecto Hong–Ou–Mandel (HOM)**, uno de los fenómenos más fundamentales y contraintuitivos de la mecánica cuántica. El código simula la dispersión de dos paquetes de onda cuánticos contra un potencial delta unidimensional y visualiza las dramáticas diferencias en el comportamiento final para bosones, fermiones y partículas distinguibles.

El proyecto está inspirado en el enfoque pedagógico del artículo de Z. J. Deng et al. (2024), "Demonstrating two-particle interference with a one-dimensional delta potential well".

---

## 🎥 Presentación Guiada en Video

Para complementar este repositorio y el artículo asociado, hemos creado una presentación en video de 10 minutos. En ella, los autores (Kevin, Jorge y Edison) explican de manera guiada cada una de las secciones clave del artículo de investigación, unificando las tres perspectivas del efecto HOM:

-   La visión física e intuitiva del **potencial delta**.
-   El poder del formalismo abstracto de la **Teoría Cuántica de Campos**.
-   La **propuesta pedagógica** que conecta ambos mundos.

Este video es el punto de partida ideal para comprender los conceptos antes de explorar el código.

https://youtu.be/o3-ujWfGUkM

*(Para insertarlo con una miniatura, reemplaza `ID_DEL_VIDEO` y `URL_COMPLETA_DEL_VIDEO` en la siguiente línea):*
markdown



🧠 El Problema Físico: ¿Qué es el Efecto HOM?

El efecto Hong–Ou–Mandel describe lo que sucede cuando dos partículas idénticas llegan simultáneamente a un divisor de haz 50:50. La intuición clásica sugiere que las partículas saldrían por puertos separados el 50% de las veces. La mecánica cuántica predice algo radicalmente diferente, que depende de la naturaleza de las partículas.
boson Bosones: Las Partículas "Sociales"

Los bosones (como los fotones) obedecen la estadística de Bose-Einstein. Debido al principio de indistinguibilidad, hay dos "historias" que llevan al mismo resultado de que una partícula salga por cada puerto: (1) ambas rebotan o (2) ambas cruzan. Para los bosones, las amplitudes de probabilidad de estas dos historias interfieren destructivamente y se anulan.

    Resultado: La probabilidad de encontrar una partícula en cada puerto es cero. Los bosones siempre salen juntos por el mismo puerto, un fenómeno conocido como agrupamiento (bunching).

fermión Fermiones: Las Partículas "Antisociales"

Los fermiones (como los electrones) obedecen el principio de exclusión de Pauli. Para ellos, las mismas dos "historias" interfieren constructivamente. Son las historias en las que ambos terminarían en el mismo puerto las que se anulan.

    Resultado: La probabilidad de encontrarlos en el mismo puerto es cero. Los fermiones siempre salen por puertos separados, un fenómeno conocido como anti-agrupamiento (antibunching).

⚪ Partículas Distinguibles

Si las partículas son distinguibles (por ejemplo, tienen polarizaciones opuestas o son de diferente tipo), las "historias" ya no son indistinguibles y no hay interferencia cuántica.

    Resultado: Se recupera el comportamiento clásico. Hay un 25% de probabilidad para cada uno de los cuatro resultados posibles, lo que significa un 50% de probabilidad de coincidencia.

💻 El Modelo de Simulación

Esta simulación reproduce este fenómeno usando la Ecuación de Schrödinger en lugar de operadores abstractos.
1. Estado Inicial

Cada partícula se inicializa como un paquete de ondas Gausiano 1D, que representa una partícula localizada con un momento bien definido.

        
ψ(x,0)=(2Δπ)1/4e−Δ(x−s0)2+ik0x
ψ(x,0)=(π2Δ​)1/4e−Δ(x−s0​)2+ik0​x

      

Las dos partículas se inician en posiciones opuestas (s₁ = -s₀, s₂ = +s₀) con momentos opuestos (k₀ y -k₀), dirigiéndose una hacia la otra.
2. Interacción: El Potencial Delta

El divisor de haz se modela como un pozo de potencial delta en el origen,

        
V(x)=−αδ(x)V(x)=−αδ(x)

      

. Este potencial tiene coeficientes de transmisión (T) y reflexión (R) que dependen de la energía y pueden ajustarse para simular un divisor 50:50.
3. Propagación Temporal

La evolución en el tiempo se calcula en el espacio de momentos (o de Fourier), donde es mucho más simple. El proceso es:

    FFT: Transformar los paquetes de onda iniciales al espacio k usando la Transformada Rápida de Fourier (FFT).

    Evolución: Aplicar el factor de fase de evolución temporal

            
    e−iE(k)t/ℏe−iE(k)t/ℏ

          

    .

    Dispersión (Scattering): Calcular por separado los componentes de onda reflejado y transmitido multiplicando por los coeficientes R(k) y T(k).

    IFFT: Regresar al espacio de posiciones usando la FFT inversa (IFFT). Se aplica una inversión espacial (x -> -x) al componente reflejado para asegurar que se propague en la dirección correcta.

4. Construcción de Estados de Dos Partículas

Una vez calculados los estados finales de una partícula phi1_final y phi2_final, el código construye los estados de dos partículas siguiendo las reglas de la mecánica cuántica:

    Estado Directo (base para partículas distinguibles):
    psi_dist = np.outer(phi1_final, phi2_final)

    Estado Intercambiado:
    psi_exch = psi_dist.T

    Bosones (simétrico):
    psi_B = (psi_dist + psi_exch) / sqrt(2)

    Fermiones (antisimétrico):
    psi_F = (psi_dist - psi_exch) / sqrt(2)

📊 Resultados y Visualización

El script genera una animación (simulacion_final_articulo.gif) que muestra la evolución de la densidad de probabilidad

        
∣Ψ(x1,x2)∣2∣Ψ(x1​,x2​)∣2

      

en el espacio de configuración, así como la probabilidad de separación entre partículas.

    Gráficos 2D Superiores: Muestran la probabilidad de encontrar la partícula 1 en X₁ y la partícula 2 en X₂. Al final de la simulación:

        Distinguibles: Mostrará 4 picos, uno en cada cuadrante.

        Bosones: Mostrará solo 2 picos, en los cuadrantes donde ambas partículas están juntas (abajo-izquierda y arriba-derecha).

        Fermiones: Mostrará solo 2 picos, en los cuadrantes donde las partículas están separadas (arriba-izquierda y abajo-derecha).

    Gráfico 1D Inferior (P_sep(|r|)): Muestra la probabilidad de encontrar las partículas a una distancia |r| = |x₁ - x₂|.

        Bosones: Tendrá un pico en r=0 (alta probabilidad de encontrarlas juntas).

        Fermiones: Será cero en r=0 (probabilidad nula de encontrarlas juntas).

🚀 Cómo Ejecutar la Simulación
1. Prerrequisitos

Asegúrate de tener Python 3 y las siguientes bibliotecas instaladas:
code Bash

    
pip install numpy matplotlib

  

2. Ejecutar el Script

Clona este repositorio y ejecuta el script principal desde tu terminal:
code Bash

    
python nombre_del_script.py

  

El programa comenzará a calcular los fotogramas de la animación y mostrará el progreso en la consola.
3. Salida

Al finalizar, se guardará un archivo llamado simulacion_final_articulo.gif en el mismo directorio.
🎓 Agradecimientos y Citas

Este trabajo se inspira y expande sobre las ideas presentadas en:

    Z. J. Deng, X. Zhang, Y. Shen, W. T. Liu, and P. X. Chen, "Demonstrating two-particle interference with a one-dimensional delta potential well," arXiv:2408.16205 [quant-ph], 2024.

El código y los resultados fueron desarrollados como parte del proyecto de investigación [Nombre de tu proyecto o curso, si aplica] en la Universidad Distrital Francisco José de Caldas.
