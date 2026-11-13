import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    return mo, np, pd, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Trabalho de Física Computacional
    ## Grupo 9 | Trabalho 7 — Simulação do Sistema Solar

    **Integrantes:** Kauai Gomes de Figueiredo Távora, Eduardo William

    ---

    ### Objetivo

    Este trabalho tem como objetivo estudar o movimento planetário por meio da modelagem matemática e de métodos computacionais, utilizando as leis de Newton como fundamento físico.

    A partir de um sistema de equações diferenciais ordinárias (EDOs), serão simuladas as trajetórias dos planetas pelo método de **Runge-Kutta de quarta ordem (RK4)**, verificando numericamente a **terceira lei de Kepler** por meio da **Transformada Rápida de Fourier (FFT)**. Posteriormente, será investigada a influência de diferentes expoentes na lei da gravitação universal sobre a geometria e a estabilidade das órbitas planetárias.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Modelagem do sistema Terra-Sol

    O sistema modelado é composto por dois corpos: O Sol, de massa $Ms$, e a Terra, de massa $Me$.

    <div align="center">
    <img src="public/sistema_terra_sol.png" width="350"/>
    </div>

    O modelo adota as seguintes hipóteses:
    1. O sol permanece fixo no centro do sistema (0,0).
    2. A posição da terra varia com o tempo, de modo que $x = x(t)$ e $y = y(t)$.
    3. A única força que age sobre a terra é a atração gravitacional do Sol.
    4. As influências gravitacionais de outros planetas são desconsideradas.
    5. O movimento ocorre em um plano bidimensional.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Obtenção do sistema de equações diferenciais ordinárias (EDO)

    ### Lei da Gravitação Universal

    Força de atração entre partículas, neste caso aponta sempre da Terra para o Sol.

    \[F_G = \frac{G Ms Me}{r^2} \]

    Decompondo a força gravitacional em componente horizontal e vertical:

    <div align="center">
    <img src="public/sun_earth_Fg.png" width="450"/>
    </div>

    Substituindo a expressão da gravitação:

    \[
    \boxed{F_{G,x}=-\frac{GM_SM_Ex}{r^3}}
    \qquad
    \boxed{F_{G,y}=-\frac{GM_SM_Ey}{r^3}}
    \]
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Aplicando a segunda lei de Newton

    \[\vec F=M_E\vec a\]

    Como a aceleração é a segunda derivada da posição, podemos obter as EDOs que descrevem a aceleração da terra:

    \[F_{G,x}=M_E\frac{d^2x}{dt^2}\]

    \[F_{G,y}=M_E\frac{d^2y}{dt^2}\]

    Substituindo novamente e cancelando a massa da terra:

    \[
    \boxed{\frac{d^2x}{dt^2}=-\frac{GM_Sx}{r^3}}
    \qquad
    \boxed{\frac{d^2y}{dt^2}=-\frac{GM_Sy}{r^3}}
    \]
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Transformando em um sistema de primeira ordem

    Definindo as componentes da velocidade:

    \[
    v_x=\frac{dx}{dt},
    \qquad
    v_y=\frac{dy}{dt}
    \]

    Consequentemente, tem-se que a derivada da velocidade é:

    \[
    \frac{dv_x}{dt}=\frac{d^2x}{dt^2},
    \qquad
    \frac{dv_y}{dt}=\frac{d^2y}{dt^2}
    \]

    Por fim, pode-se montar o seguinte sistema:

    \[
    \boxed{
    \begin{aligned}
    \frac{dv_x}{dt}&=-\frac{GM_Sx}{r^3}\\[6pt]
    \frac{dx}{dt}&=v_x\\[6pt]
    \frac{dv_y}{dt}&=-\frac{GM_Sy}{r^3}\\[6pt]
    \frac{dy}{dt}&=v_y
    \end{aligned}
    }
    \]

    \[
    r=\sqrt{x^2+y^2}
    \]
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Utilizando unidades astronômicas

    O livro explica que usar unidades do Sistema Internacional tornaria os valores não tão convenientes para a simulação. Em razão disso, é adotada a Unidade Astrômica, que baseia-se na distância entre a Terra e o Sol.

    \[ 1 \text{UA} \approx 1,5 \times 10^{11} \text{m} \]

    Para uma órbita circular, a força gravitacional fornece a força centrípeta:
    \[
    \frac{M_Ev^2}{r}=\frac{GM_SM_E}{r^2}
    \]

    Cancelando \(M_E\):
    \[
    v^2=\frac{GM_S}{r}
    \]

    Sabe-se que a velocidade em uma órbita circular é:
    \[
    v=\frac{2\pi r}{T}
    \]

    Substituindo:
    \[
    \frac{4\pi^2r^2}{T^2}=\frac{GM_S}{r}
    \]

    Portanto:
    \[
    GM_S=\frac{4\pi^2r^3}{T^2}
    \]

    Considerando a órbita terrestre como aproximadamente circular, com \(r=1\) UA e \(T=1\) ano:

    \[
    \boxed{GM_S=4\pi^2\ \text{UA}^3/\text{ano}^2}
    \]
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Sistema de EDOs nas unidades astronômicas

    Substituindo $GM_S=4\pi^2$ e $r = \sqrt{x^2 + y^2}$ no sistema de equação definido anteriormente:
    \[
    \boxed{
    \begin{aligned}
    \frac{dx}{dt}&=v_x\\
    \frac{dy}{dt}&=v_y\\
    \frac{dv_x}{dt}&=-\frac{4\pi^2x}{(x^2+y^2)^{3/2}}\\
    \frac{dv_y}{dt}&=-\frac{4\pi^2y}{(x^2+y^2)^{3/2}}
    \end{aligned}
    }
    \]

    O sistema possui 4 variáveis em função do tempo que podem ser agrupadas em um vetor e seu respectivo vetor de derivadas:

    \[\mathbf u =
    \begin{bmatrix}
    x\\
    y\\
    v_x\\
    v_y
    \end{bmatrix},
    \qquad
    \frac{d\mathbf u}{dt}=
    \begin{bmatrix}
    \frac{dx}{dt}\\[4pt]
    \frac{dy}{dt}\\[4pt]
    \frac{dv_x}{dt}\\[4pt]
    \frac{dv_y}{dt}
    \end{bmatrix}
    \]

    Ficando com a única equação diferencial:

    \[\boxed{\frac{d\mathbf u}{dt}=f(t,\mathbf u)}\]

    Portanto, pode-se definir o sistema em python da seguinte maneira:
    """)
    return


@app.cell
def _(np):
    GM = 4 * (np.pi ** 2)

    def f(t, u, beta=2.0):
        x, y, vx, vy = u
        r = np.sqrt(x**2 + y**2)

        d_vx = -GM * x / r**(beta + 1)
        d_vy = -GM * y / r**(beta + 1)

        return np.array([vx, vy, d_vx, d_vy])

    f
    return GM, f


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Resolvendo o sistema utilizando o RK4

    \begin{aligned}
    k_1 &= hf(x,t),  \\
    k_2 &= hf(x+\frac{1}{2}k_1, t+\frac{1}{2}h), \\
    k_3 &= hf(x+\frac{1}{2}k_2, t+\frac{1}{2}h), \\
    k_4 &= h(f(x+k_3, t+h), \\
    x(t+h) &= x(t) + \frac{1}{6}(k_1 + 2k_2 + 2k_3 +k_4)
    \end{aligned}

    As condições iniciais propostas no livro são:

    \[x = 1, \qquad y = 0, \qquad v_x = 0 \qquad v_y = 2\pi, \qquad h=0.002 \]
    """)
    return


@app.cell
def _(f, mo, np, plt):
    def rk4(f, t, u, h):
        k1 = f(t, u)
        k2 = f(t + h / 2, u + h * k1 / 2)
        k3 = f(t + h / 2, u + h * k2 / 2)
        k4 = f(t + h, u + h * k3)

        return u + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6

    _u = np.array([1, 0, 0, 2 * np.pi])
    h = 0.002
    t = 0.0

    year_one_result = [_u.copy()]

    # 500 iterações correspondem exatamente ao período de 1 ano ao utilizar o passo definido
    for _ in range(500):
        _u = rk4(f, t, _u, h)
        t += h
        year_one_result.append(_u.copy())

    year_one_result = np.array(year_one_result)

    x = year_one_result[:, 0]
    y = year_one_result[:, 1]        


    def plot_orbit(x, y, title=None, label=None, ax=None, show_sun=True):
        if ax is None:
            fig, ax = plt.subplots(figsize=(6, 6))

        ax.plot(x, y, label=label, linewidth=0.8)

        if show_sun:
            ax.scatter(0, 0, color="orange", label="Sol")

        ax.set_xlabel("x (UA)")
        ax.set_ylabel("y (UA)")
        ax.set_aspect("equal", adjustable="box")
        ax.grid(True)

        if title:
            ax.set_title(title)

        if label or show_sun:
            ax.legend()

        return ax

    _ax = plot_orbit(x, y, title="Terra orbitando o Sol")
    mo.center(_ax.figure)
    return plot_orbit, rk4


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Verificação da terceira lei de Kepler usando FFT

    Para cada planeta da Tabela 4.1, usamos o semieixo maior $a$ e a excentricidade $e$. A condição inicial é colocada no periélio:

    \begin{aligned}
    x_0=a(1-e),\quad y_0=0,\quad v_{x,0}=0,\quad
    v_{y,0}=\sqrt{\frac{GM_S(1+e)}{a(1-e)}}.
    \end{aligned}

    A trajetória é calculada com RK4 e passo $h=0,002$ ano. Em seguida, aplicamos a FFT ao sinal $y(t)$. A frequência dominante $f$ fornece o período $T=1/f$. Por fim, calculamos $T^2/a^3$ e comparamos com a Tabela 4.2.

    Os dados de $a$ e $e$ abaixo são os da Tabela 4.1 do livro. A tabela de referência para $T^2/a^3$ é apresentada na Tabela 4.2.
    """)
    return


@app.cell
def _():
    planetas = {
        "Vênus":   {"a": 0.72, "e": 0.007, "referencia": 0.997},
        "Terra":   {"a": 1.00, "e": 0.017, "referencia": 0.998},
        "Marte":   {"a": 1.52, "e": 0.093, "referencia": 1.005},
        "Júpiter": {"a": 5.20, "e": 0.048, "referencia": 1.010},
        "Saturno": {"a": 9.54, "e": 0.056, "referencia": 0.988},
    }

    planetas
    return (planetas,)


@app.cell
def _(GM, f, np, rk4):

    def analisar_fft(a, e, h=0.002, numero_orbitas=30):
        # Condições iniciais no periélio
        x0 = a * (1 - e)
        vy0 = np.sqrt(GM * (1 + e) / (a * (1 - e)))
        u = np.array([x0, 0.0, 0.0, vy0])

        # Duração da simulação
        periodo_estimado = a**1.5
        n = int(np.ceil(numero_orbitas * periodo_estimado / h))

        # Simulação com RK4
        sinal_y = np.empty(n + 1)
        sinal_y[0] = u[1]

        for i in range(n):
            u = rk4(f, i * h, u, h)
            sinal_y[i + 1] = u[1]

        # Transformada de Fourier
        sinal = sinal_y - np.mean(sinal_y)
        janela = np.hanning(len(sinal))

        espectro = np.abs(np.fft.rfft(sinal * janela))
        frequencias = np.fft.rfftfreq(len(sinal), d=h)

        # Frequência dominante
        k = np.argmax(espectro[1:]) + 1

        if 1 <= k < len(espectro) - 1:
            alfa, centro, gama = np.log(espectro[k-1:k+2] + 1e-300)
            denominador = alfa - 2*centro + gama

            delta = (
                0.5 * (alfa - gama) / denominador
                if denominador != 0 else 0.0
            )
        else:
            delta = 0.0

        frequencia_dominante = (k + delta) / (len(sinal) * h)
        periodo = 1 / frequencia_dominante

        return {
            "periodo": periodo,
            "frequencias": frequencias,
            "espectro": espectro
        }

    analisar_fft
    return (analisar_fft,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Espectro de Fourier de cada planeta

    O pico de maior amplitude diferente de zero corresponde à frequência orbital dominante. O inverso dessa frequência é a estimativa do período. Os gráficos abaixo mostram o módulo da FFT em função da frequência.
    """)
    return


@app.cell
def _(analisar_fft, mo, pd, planetas):
    def gerar_tabela_kepler(planetas):
        resultados = []
        analises = {}

        for nome, dados in planetas.items():
            a = dados["a"]
            e = dados["e"]

            analise = analisar_fft(a, e)
            analises[nome] = analise

            periodo = analise["periodo"]
            razao = periodo**2 / a**3

            resultados.append({
                "Planeta": nome,
                "a (UA)": a,
                "e": e,
                "T FFT (anos)": periodo,
                "T²/a³ FFT": razao,
                "Tabela 4.2": dados["referencia"]
            })

        return pd.DataFrame(resultados), analises


    tabela_kepler, analises_fft = gerar_tabela_kepler(planetas)

    mo.ui.table(tabela_kepler.round(5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Modificação do sistema de EDOs para variar $\beta$

    O texto modifica a lei da força gravitacional para

    \begin{aligned}
    F_G=\frac{GM_SM_E}{r^\beta}.
    \end{aligned}

    A força continua apontando para o Sol. Ao decompor nas direções $x$ e $y$, a aceleração fica

    \begin{aligned}
    \boxed{
    \frac{dv_x}{dt}=-\frac{GM_Sx}{r^{\beta+1}},
    \qquad
    \frac{dv_y}{dt}=-\frac{GM_Sy}{r^{\beta+1}}
    }
    \end{aligned}

    e as outras duas equações permanece$(dx/dt=v_x) e (dy/dt=v_y)$. Assim, basta acrescentar o parâmetro `beta` à função `f`. Para $\beta=2$, recuperamos o sistema original.

    Para comparar com as Figuras 4.5 e 4.6, mantemos as mesmas condições iniciais em todas as simulações: $x_0=1, y_0=0,  v_{x,0}=0, v_{y,0}=5$ UA/ano, com passo $h=0{,}001$ ano. O valor de $\beta=2$ é a órbita de referência.
    """)
    return


@app.cell
def _(f, mo, np, plot_orbit, plt, rk4):
    def simular_beta(beta, tempo_final=10.0, h=0.001):
        u = np.array([1.0, 0.0, 0.0, 5.0])
        n = int(tempo_final / h)

        trajetoria = np.empty((n + 1, 4))
        tempos = np.arange(n + 1) * h
        trajetoria[0] = u

        for i in range(n):
            g = lambda t, estado: f(t, estado, beta=beta)
            u = rk4(g, tempos[i], u, h)
            trajetoria[i + 1] = u

            r = np.hypot(u[0], u[1])
            if not np.all(np.isfinite(u)) or r < 0.005 or r > 100:
                return tempos[:i+2], trajetoria[:i+2]

        return tempos, trajetoria



    def plot_beta_subplots(configuracoes):
      fig, axes = plt.subplots(2, 2, figsize=(10, 10))

      for ax, (beta, tempo_final) in zip(axes.flat, configuracoes):
          tempos, traj = simular_beta(beta, tempo_final, 0.001)

          plot_orbit(
              traj[:, 0],
              traj[:, 1],
              title=f"Órbita para β = {beta}",
              ax=ax
          )

          ax.set_xlim(-1, 1)
          ax.set_ylim(-1, 1)

      fig.tight_layout()
      return fig


    mo.center(plot_beta_subplots([(3, 2), (2.5, 3), (2.1, 5), (2.01, 10)]))
    return (simular_beta,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Comparação direta entre $\beta=2, \beta=2{,}01 , \beta=2{,}1$

    A Figura 4.6 do livro destaca que pequenas alterações em $\beta$ já modificam a orientação da elipse ao longo do tempo. O gráfico seguinte permite observar essa precessão com as mesmas condições iniciais.
    """)
    return


@app.cell
def _(mo, plot_orbit, plt, simular_beta):
    def plot_precession(betas):
        fig, ax = plt.subplots(figsize=(7, 7))

        for beta in betas:
            tempos, traj = simular_beta(
                beta,
                tempo_final=10.0,
                h=0.001
            )

            plot_orbit(
                traj[:, 0],
                traj[:, 1],
                label=f"β = {beta}",
                ax=ax,
                show_sun=False
            )

        ax.scatter(0, 0, color="orange", label="Sol")
        ax.set_title("Precessão das órbitas para β próximo de 2")
        ax.legend()

        fig.tight_layout()
        return fig


    mo.center(plot_precession([2.0, 2.01, 2.1]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Discussão dos resultados

    - Para $\beta=2$, a força segue a lei do inverso do quadrado da distância, e a órbita elíptica mantém sua orientação.
    - Para $\beta=2{,}01$ e $\beta=2{,}1$, a trajetória apresenta precessão: a elipse gira gradualmente em torno do Sol.
    - Para $\beta=2{,}5$, a precessão é mais acentuada.
    - Para $\beta=3$, a trajetória se torna muito instável nas condições iniciais adotadas, podendo passar muito perto do Sol e depois escapar numericamente.

    A comparação mostra a sensibilidade da órbita à forma da dependência da força com a distância. Os resultados para $\beta\ne2$ devem ser interpretados como simulações do modelo modificado, não como órbitas planetárias reais.
    """)
    return


if __name__ == "__main__":
    app.run()
