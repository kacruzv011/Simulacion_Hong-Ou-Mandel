# Simulación Cuántica del Efecto Hong–Ou–Mandel en 1D  
### Bosones • Fermiones • Partículas Distinguibles

Este repositorio contiene una simulación numérica avanzada del comportamiento de dos partículas cuánticas al interactuar mediante un potencial Delta de Dirac, usando paquetes gaussianos y propagación de Fourier.  

El objetivo principal es ilustrar visual y cuantitativamente el **efecto Hong–Ou–Mandel (HOM)** y sus diferencias fundamentales entre bosones, fermiones y partículas distinguibles.

---

## 🧠 Introducción

El experimento HOM es uno de los fenómenos cuánticos más famosos, demostrando que:

- Los **bosones** tienden a “agruparse” (*bunching*).  
- Los **fermiones** tienden a evitarse por el principio de exclusión (*antibunching*).  
- Las partículas distinguibles no presentan interferencia cuántica.

Esta simulación reproduce de manera efectiva qué ocurre cuando dos partículas idénticas se acercan desde direcciones opuestas, interactúan con un potencial localizado y evolucionan en el tiempo.

El enfoque numérico permite visualizar simultáneamente:

- Función de probabilidad bidimensional  
- Correlación local \( g^{(2)}(x,x) \)  
- Probabilidad a lo largo de la diagonal (coincidencias)  
- Distribución de separaciones  
- Diferencias cualitativas entre simetrización, antisimetrización y su ausencia

---

## 📘 Modelo Físico

### 1. Paquetes Gaussianos Iniciales

Cada partícula inicia como:

\[
\psi(x) = \left( \frac{2\Delta}{\pi} \right)^{1/4}
e^{-\Delta(x-s_0)^2 + ik_0 x}
\]

con posiciones iniciales opuestas:

- \( s_1 = -10 \)
- \( s_2 = +10 \)

### 2. Potencial Delta de Dirac

Se usa un potencial localizado:

\[
V(x) = \lambda \delta(x)
\]

El cual tiene soluciones exactas para transmisión y reflexión:

\[
T = \frac{1}{1 + i\beta}, \qquad  
R = -\frac{i\beta}{1+i\beta}
\]

donde \( \beta = \lambda/|k| \).

Esto permite generar la interferencia sin necesidad de resolver la ecuación de Schrödinger completa.

### 3. Propagación Temporal

La evolución libre en espacio de momentos se implementa usando FFT:

\[
e^{-ik^2\tau}
\]

Luego se agrega el efecto del potencial mediante los coeficientes \(T\) y \(R\).

---

## 🎲 Estados de Dos Partículas

La simulación construye los estados:

### Bosones (simétrico)
\[
\Psi_B = \frac{1}{\sqrt{2}}
\left( \psi_1(x_1)\psi_2(x_2) + 
       \psi_2(x_1)\psi_1(x_2) \right)
\]

### Fermiones (antisimétrico)
\[
\Psi_F = \frac{1}{\sqrt{2}}
\left( \psi_1(x_1)\psi_2(x_2) - 
       \psi_2(x_1)\psi_1(x_2) \right)
\]

### Distinguibles
\[
\Psi_D = \psi_1(x_1)\psi_2(x_2)
\]

---

## 📊 Animaciones y Resultados

El programa genera una animación con **seis paneles simultáneos**:

