import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- 0. Configuración Inicial ---
print("===================================================================")
print("Simulación Cuántica: Bosones vs Fermiones (Hong-Ou-Mandel)")
print("===================================================================")

# --- 1. Parámetros Optimizados para Visualización ---
# Reduje K0 y ajusté S1/S2 para que la interacción se vea en cámara lenta
S1 = -10.0; S2 = 10.0   # Posiciones iniciales más cercanas
LAMBDA = 5.0            # Potencial de barrera (Delta de Dirac)
DELTA = 0.5             # Ancho del paquete (más ancho = mejor interferencia)
K0_HOM = 5.0            # Momento REDUCIDO (antes 20) para ver la evolución lenta

N_POINTS = 512          # Mayor resolución espacial
X_MAX = 30.0            # Zoom al área de interés
X = np.linspace(-X_MAX, X_MAX, N_POINTS)
DX = X[1] - X[0]
K = np.fft.fftfreq(N_POINTS, d=DX) * 2 * np.pi

# --- 2. Funciones Físicas ---

def gaussian_wave_packet(x, s0, k0):
    """Paquete gaussiano inicial"""
    norm = ((2 * DELTA / np.pi)**0.25)
    return norm * np.exp(-DELTA * (x - s0)**2 + 1j * k0 * x)

def get_transmission_reflection(k_grid):
    """Coeficientes de transmisión y reflexión para potencial Delta"""
    # Evitar división por cero en k=0
    k_safe = np.where(k_grid == 0, 1e-10, k_grid)
    beta = (LAMBDA) / (np.abs(k_safe)) # Beta depende de la magnitud de k

    # Coeficientes analíticos para delta de Dirac
    # T = 1 / (1 + i*beta), R = -i*beta / (1 + i*beta)
    # Nota: El signo y fase exacta dependen de la convención, usamos la estándar
    denom = 1 - 1j * beta
    t_k = 1 / denom
    r_k = -1j * beta / denom
    return t_k, r_k

def propagate_packet(phi_k_initial, t_k, r_k, K, tau, origin_direction):
    """
    Propaga el paquete usando una aproximación asintótica suave.
    origin_direction: 'left' (viene de -x) o 'right' (viene de +x)
    """
    # Propagador de evolución temporal libre
    # Dispersión cuadrática E = k^2 (hbar=2m=1)
    time_ev = np.exp(-1j * K**2 * tau)

    # 1. Evolución si fuera libre (incidente)
    psi_inc = np.fft.ifft(phi_k_initial * time_ev)

    # 2. Componente Transmitida (continúa en la misma dirección)
    psi_trans = np.fft.ifft(phi_k_initial * t_k * time_ev)

    # 3. Componente Reflejada (invierte dirección)
    # Para invertir en espacio, usamos flip en el array resultante o k -> -k
    # Aquí usamos la propiedad de simetría del FFT para reflejar
    phi_k_refl = phi_k_initial * r_k * time_ev
    psi_refl_raw = np.fft.ifft(phi_k_refl)
    psi_refl = psi_refl_raw[::-1] # Inversión espacial aproximada para el rebote

    # Combinación suave basada en la posición respecto a la barrera (x=0)
    # Usamos una función sigmoide para mezclar incidentes/reflejados y evitar cortes bruscos
    sigmoid = 1 / (1 + np.exp(-20 * X)) # Transición suave en x=0

    if origin_direction == 'left':
        # Viene de la izquierda:
        # x < 0: Incidente + Reflejado
        # x > 0: Transmitido
        psi_final = (psi_inc + psi_refl) * (1 - sigmoid) + psi_trans * sigmoid
    else:
        # Viene de la derecha:
        # x < 0: Transmitido
        # x > 0: Incidente + Reflejado
        psi_final = psi_trans * (1 - sigmoid) + (psi_inc + psi_refl) * sigmoid

    return psi_final

# --- 3. Inicialización de Estados ---
print("Calculando estados iniciales...")
# Paquetes en espacio de momentos
phi1_k0 = np.fft.fft(gaussian_wave_packet(X, S1, K0_HOM))   # Izquierda -> Derecha
phi2_k0 = np.fft.fft(gaussian_wave_packet(X, S2, -K0_HOM))  # Derecha -> Izquierda

t_k, r_k = get_transmission_reflection(K)

# --- 4. Configuración de la Animación ---
TAU_MAX = 5.0   # Tiempo total
FRAMES = 150    # Cantidad de frames
DT = TAU_MAX / FRAMES

fig = plt.figure(figsize=(18, 10))
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.05, right=0.95, hspace=0.3, wspace=0.25)
gs = fig.add_gridspec(2, 4)

# Definición de Ejes
ax_dens = [fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1]), fig.add_subplot(gs[0, 2])]
ax_corr = fig.add_subplot(gs[0, 3]) # Correlación g2
ax_diag = fig.add_subplot(gs[1, :2]) # Diagonal (Bunching)
ax_sep = fig.add_subplot(gs[1, 2:])  # Separación

titulos = ['Bosones (Simétrico)', 'Fermiones (Antisimétrico)', 'Distinguibles']
cmaps = ['inferno', 'viridis', 'magma']

X1, X2 = np.meshgrid(X, X)

def update(frame):
    tau = frame * DT

    # 1. Calcular funciones de onda individuales
    psi1 = propagate_packet(phi1_k0, t_k, r_k, K, tau, 'left')
    psi2 = propagate_packet(phi2_k0, t_k, r_k, K, tau, 'right')

    # 2. Construir estado de dos partículas
    psi_dist = np.outer(psi1, psi2)       # Distinguibles (x1, x2)
    psi_dist_swap = np.outer(psi2, psi1)  # Intercambiadas (x2, x1) para simetría

    # Estados simetrizados
    psi_B = (psi_dist + psi_dist_swap) / np.sqrt(2) # Bosones
    psi_F = (psi_dist - psi_dist_swap) / np.sqrt(2) # Fermiones

    # Probabilidades
    P_B = np.abs(psi_B)**2
    P_F = np.abs(psi_F)**2
    P_D = np.abs(psi_dist)**2

    probs = [P_B, P_F, P_D]

    # --- PLOT 1-3: Densidades 2D ---
    for i, ax in enumerate(ax_dens):
        ax.clear()
        # Normalizar color
        vmax = np.max(P_B) * 0.8
        ax.pcolormesh(X1, X2, probs[i], cmap=cmaps[i], vmin=0, vmax=vmax, shading='auto')
        ax.plot(X, X, 'w--', alpha=0.3, lw=1) # Línea diagonal x1=x2
        ax.set_title(titulos[i], fontweight='bold')
        ax.set_aspect('equal')
        # Quitar ticks internos para limpiar
        if i > 0: ax.set_yticks([])
        ax.set_xlabel('$x_1$')
        if i == 0: ax.set_ylabel('$x_2$')

    # --- PLOT 4: Función de Correlación g^2(x) en la diagonal ---
    # g2(x) = P(x,x) / (P1(x)*P2(x))
    # Importante: Maskear valores donde la densidad es casi cero para evitar ruido
    ax_corr.clear()

    # Densidades marginales (integrando sobre una coordenada)
    rho1 = np.sum(P_D, axis=1) # Densidad part 1
    rho2 = np.sum(P_D, axis=0) # Densidad part 2
    denom = rho1 * rho2

    # Umbral de visualización (1% del máximo)
    threshold = np.max(denom) * 0.01
    mask = denom > threshold

    # Diagonal de las matrices
    diag_B = np.diagonal(P_B)
    diag_F = np.diagonal(P_F)
    diag_D = np.diagonal(P_D)

    # Calcular g2 solo donde hay densidad significativa
    x_valid = X[mask]
    if len(x_valid) > 0:
        g2_B = diag_B[mask] / denom[mask]
        g2_F = diag_F[mask] / denom[mask]

        ax_corr.plot(x_valid, g2_B, 'r-', lw=2, label='Bosones ($g^2 > 1$)')
        ax_corr.plot(x_valid, g2_F, 'b--', lw=2, label='Fermiones ($g^2 < 1$)')
        ax_corr.axhline(1, color='gray', ls=':', label='Clásico ($g^2=1$)')

    ax_corr.set_ylim(0, 3.0)
    ax_corr.set_title('Correlación Local $g^{(2)}(x,x)$')
    ax_corr.legend(fontsize=8, loc='upper right')
    ax_corr.grid(True, alpha=0.3)

    # --- PLOT 5: Densidad en la Diagonal (Bunching) ---
    ax_diag.clear()
    ax_diag.plot(X, diag_B, 'r-', lw=2, label='Bosones (Agrupamiento)')
    ax_diag.plot(X, diag_F, 'b--', lw=2, label='Fermiones (Exclusión)')
    ax_diag.plot(X, diag_D, 'k:', alpha=0.5, label='Distinguibles')
    ax_diag.set_title(f'Probabilidad de Coincidencia (Diagonal) - t={tau:.2f}')
    ax_diag.legend()
    ax_diag.set_xlim(-X_MAX, X_MAX)
    ax_diag.set_ylim(0, np.max(diag_B)*1.1 if np.max(diag_B)>0 else 1)
    ax_diag.grid(True, alpha=0.2)

    # --- PLOT 6: Distribución de Separación P(x1 - x2) ---
    ax_sep.clear()
    # Usamos correlación cruzada para calcular distribución de distancias rápidamente
    # P(r) = int |psi(x, x+r)|^2 dx

    # Método eficiente: Sumar diagonales desplazadas de la matriz de densidad
    # Nota: Esto es costoso en python puro, usamos una aproximación visual o slicing rápido
    # Haremos un corte rápido para visualización en tiempo real

    r_vals = np.linspace(0, X_MAX, 100)
    sep_B = []
    sep_F = []

    # Muestreo rápido de separación (optimizado para animación)
    for r in r_vals:
        # Indice de desplazamiento aproximado
        idx_shift = int(r / DX)
        if idx_shift < N_POINTS:
            # Traza con desplazamiento (suma de elementos donde |i-j| = idx_shift)
            val_B = np.trace(P_B, offset=idx_shift) + np.trace(P_B, offset=-idx_shift)
            val_F = np.trace(P_F, offset=idx_shift) + np.trace(P_F, offset=-idx_shift)
            sep_B.append(val_B)
            sep_F.append(val_F)
        else:
            sep_B.append(0)
            sep_F.append(0)

    ax_sep.plot(r_vals, sep_B, 'r-', lw=2, label='Bosones')
    ax_sep.plot(r_vals, sep_F, 'b--', lw=2, label='Fermiones')
    ax_sep.set_title('Probabilidad vs Separación $|x_1 - x_2|$')
    ax_sep.set_xlabel('Distancia r')
    ax_sep.set_yticks([]) # Prob relativa
    ax_sep.legend()
    ax_sep.set_xlim(0, X_MAX)

    return

print("Generando animación (esto puede tardar unos segundos)...")
ani = FuncAnimation(fig, update, frames=FRAMES, interval=50)

# Guardar o mostrar
try:
    ani.save('simulacion_cuantica_corregida.gif', writer='pillow', fps=20)
    print("¡Guardado exitoso como 'simulacion_cuantica_corregida.gif'!")
except Exception as e:
    print(f"Error al guardar: {e}")
    plt.show()
