# Simulación Cuántica: Interferencia de Dos Partículas (Bosones, Fermiones y Distinguibles)

Este repositorio contiene una simulación numérica del fenómeno de interferencia de dos partículas inspirado en el experimento de Hong–Ou–Mandel (HOM), modelando la interacción mediante un potencial Delta de Dirac y propagación cuántica en 1D.

La animación generada muestra:

- La función de probabilidad para bosones (estado simétrico)
- La función de probabilidad para fermiones (estado antisimétrico)
- El caso distinguible
- La función de correlación local \( g^{(2)}(x,x) \)
- La probabilidad de coincidencia en la diagonal
- La distribución de separaciones \( |x_1 - x_2| \)

Esto permite visualizar claramente:
- **Bunching** en bosones  
- **Antibunching** en fermiones  
- La diferencia entre partículas idénticas y distinguibles

---

## 🧠 Fundamento físico

El experimento HOM muestra cómo dos partículas idénticas interfieren al cruzar un divisor de haz.  
Aquí se implementa una analogía en 1D con:

- Paquetes gaussianos como estados iniciales  
- Un potencial Delta que actúa como dispersor  
- Evolución temporal mediante FFT  
- Construcción de estados bipartícula:

\[
\Psi_B = \frac{1}{\sqrt{2}}(\psi_1 \psi_2 + \psi_2 \psi_1)
\]

\[
\Psi_F = \frac{1}{\sqrt{2}}(\psi_1 \psi_2 - \psi_2 \psi_1)
\]

---

## 📦 Requisitos

Instalar dependencias:

```bash>
<img width="1022" height="561" alt="Screenshot from 2025-12-11 13-35-06" src="https://github.com/user-attachments/assets/ca2ec098-e5cf-44d2-b3f7-7203ed15efdd" />

