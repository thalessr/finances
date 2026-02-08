# Payback e ROI — Cia. Argo Energy

> Cálculo passo a passo do payback (simples e descontado) e do ROI para os cenários Base, Otimista e Pessimista. Dados extraídos de `dcf_scenarios.csv`.

---

## 1. Fórmulas Utilizadas

### Payback Simples
Tempo necessário para que a soma dos fluxos de caixa recupere o investimento inicial.

```
Payback = ano anterior à recuperação + (saldo negativo restante / fluxo do ano de recuperação)
```

### Payback Descontado
Mesmo conceito, porém os fluxos são descontados à taxa WACC (utilizamos 10% a.a. como referência).

```
FC descontado = FCt / (1 + taxa)^t
```

### ROI (Return on Investment)
Retorno total do investimento sobre o capital aplicado.

```
ROI = (Lucro Líquido Total / Investimento Inicial) × 100%
```

Onde **Lucro Líquido Total** = soma do lucro líquido dos 5 anos do projeto.

---

## 2. Premissas

- **Investimento inicial (CAPEX):** R$ 3.600.000
- **Depreciação anual:** R$ 640.000 (constante em todos os cenários)
- **Lucro Líquido** = OCF − Depreciação (para cálculo do ROI)
- **Taxa de desconto (payback descontado):** 10% a.a.

---

## 3. Cenário Base

### 3.1. Fluxos de Caixa Operacional (OCF)

| Ano | OCF (R$)   | Acumulado Simples (R$) |
|----:|-----------:|------------------------:|
| 0   | -3.600.000 | -3.600.000             |
| 1   | 1.212.550  | -2.387.450             |
| 2   | 1.379.612,50 | -1.007.837,50       |
| 3   | 1.635.775  | +627.937,50            |
| 4   | 2.020.018,75 | —                     |
| 5   | 2.500.323,44 | —                     |

### 3.2. Payback Simples — Passo a Passo

**Passo 1:** Identificar o ano em que o acumulado torna-se positivo.
- Após ano 2: saldo = -1.007.837,50
- Após ano 3: saldo = +627.937,50 → recuperação ocorre no ano 3

**Passo 2:** Calcular a fração do ano 3 necessária para zerar o saldo.
```
Fração = |Saldo negativo após ano 2| / OCF ano 3
Fração = 1.007.837,50 / 1.635.775 = 0,6162
```

**Passo 3:** Payback simples.
```
Payback = 2 + 0,6162 = 2,62 anos
```

**Resultado:** Payback simples ≈ **2,62 anos** (cerca de 2 anos e 7 meses).

### 3.3. Payback Descontado @ 10% — Passo a Passo

**Passo 1:** Descontar cada OCF ao valor presente.
- FC₁ descontado = 1.212.550 / 1,10 = 1.102.318,18
- FC₂ descontado = 1.379.612,50 / 1,10² = 1.139.349,17
- FC₃ descontado = 1.635.775 / 1,10³ = 1.229.244,90
- FC₄ descontado = 2.020.018,75 / 1,10⁴ = 1.380.641,50
- FC₅ descontado = 2.500.323,44 / 1,10⁵ = 1.552.209,27

**Passo 2:** Acumular os fluxos descontados.

| Ano | FC Descontado (R$) | Acumulado (R$)   |
|----:|-------------------:|-----------------:|
| 0   | -3.600.000         | -3.600.000       |
| 1   | 1.102.318,18       | -2.497.681,82    |
| 2   | 1.139.349,17       | -1.358.332,65    |
| 3   | 1.229.244,90       | -129.087,75      |
| 4   | 1.380.641,50       | +1.251.553,75    |

**Passo 3:** Recuperação ocorre entre ano 3 e 4.
```
Fração = 129.087,75 / 1.380.641,50 = 0,0935
Payback descontado = 3 + 0,0935 = 3,09 anos
```

**Resultado:** Payback descontado @ 10% ≈ **3,09 anos**.

### 3.4. ROI — Passo a Passo

**Passo 1:** Calcular o Lucro Líquido de cada ano (OCF − Depreciação).

| Ano | OCF (R$)   | Depreciação (R$) | Lucro Líquido (R$) |
|----:|-----------:|-----------------:|-------------------:|
| 1   | 1.212.550  | 640.000          | 572.550            |
| 2   | 1.379.612,50 | 640.000        | 739.612,50         |
| 3   | 1.635.775  | 640.000          | 995.775            |
| 4   | 2.020.018,75 | 640.000        | 1.380.018,75       |
| 5   | 2.500.323,44 | 640.000        | 1.860.323,44       |

**Passo 2:** Somar o Lucro Líquido total.
```
Lucro Líquido Total = 572.550 + 739.612,50 + 995.775 + 1.380.018,75 + 1.860.323,44
Lucro Líquido Total = 5.547.279,69
```

**Passo 3:** Calcular o ROI.
```
ROI = (5.547.279,69 / 3.600.000) × 100%
ROI = 154,09%
```

**Resultado:** ROI ≈ **154,09%** (retorno total sobre o investimento em 5 anos).

---

## 4. Cenário Otimista

### 4.1. Fluxos de Caixa Operacional (OCF)

| Ano | OCF (R$)   | Acumulado Simples (R$) |
|----:|-----------:|------------------------:|
| 0   | -3.600.000 | -3.600.000             |
| 1   | 1.460.050  | -2.139.950             |
| 2   | 1.664.237,50 | -475.712,50           |
| 3   | 1.977.325  | +1.501.612,50          |
| 4   | 2.446.556,25 | —                     |
| 5   | 3.033.995,31 | —                     |

### 4.2. Payback Simples — Passo a Passo

**Passo 1:** Recuperação ocorre no ano 3 (acumulado positivo após ano 2: -475.712,50).

**Passo 2:** Fração do ano 3.
```
Fração = 475.712,50 / 1.977.325 = 0,2406
Payback = 2 + 0,2406 = 2,24 anos
```

**Resultado:** Payback simples ≈ **2,24 anos**.

### 4.3. Payback Descontado @ 10%

| Ano | FC Descontado (R$) | Acumulado (R$)   |
|----:|-------------------:|-----------------:|
| 0   | -3.600.000         | -3.600.000       |
| 1   | 1.327.318,18       | -2.272.681,82    |
| 2   | 1.374.576,03       | -898.105,79      |
| 3   | 1.486.022,73       | +587.916,94      |

```
Fração = 898.105,79 / 1.486.022,73 = 0,6044
Payback descontado = 2 + 0,6044 = 2,60 anos
```

**Resultado:** Payback descontado @ 10% ≈ **2,60 anos**.

### 4.4. ROI — Passo a Passo

| Ano | OCF (R$)   | Lucro Líquido (R$) |
|----:|-----------:|-------------------:|
| 1   | 1.460.050  | 820.050            |
| 2   | 1.664.237,50 | 1.024.237,50     |
| 3   | 1.977.325  | 1.337.325          |
| 4   | 2.446.556,25 | 1.806.556,25     |
| 5   | 3.033.995,31 | 2.393.995,31     |

```
Lucro Líquido Total = 7.382.164,06
ROI = (7.382.164,06 / 3.600.000) × 100% = 205,06%
```

**Resultado:** ROI ≈ **205,06%**.

---

## 5. Cenário Pessimista

### 5.1. Fluxos de Caixa Operacional (OCF)

| Ano | OCF (R$)   | Acumulado Simples (R$) |
|----:|-----------:|------------------------:|
| 0   | -3.600.000 | -3.600.000             |
| 1   | 940.300    | -2.659.700             |
| 2   | 982.375    | -1.677.325             |
| 3   | 1.070.734  | -606.591               |
| 4   | 1.216.922,38 | +610.331,38          |
| 5   | 1.384.180,73 | —                     |

### 5.2. Payback Simples — Passo a Passo

**Passo 1:** Recuperação ocorre no ano 4 (acumulado positivo após ano 3: -606.591).

**Passo 2:** Fração do ano 4.
```
Fração = 606.591 / 1.216.922,38 = 0,4985
Payback = 3 + 0,4985 = 3,50 anos
```

**Resultado:** Payback simples ≈ **3,50 anos**.

### 5.3. Payback Descontado @ 10%

| Ano | FC Descontado (R$) | Acumulado (R$)   |
|----:|-------------------:|-----------------:|
| 0   | -3.600.000         | -3.600.000       |
| 1   | 854.818,18         | -2.745.181,82    |
| 2   | 811.880,17         | -1.933.301,65    |
| 3   | 804.034,05         | -1.129.267,60    |
| 4   | 831.076,92         | -298.190,68      |
| 5   | 859.741,08         | +561.550,40      |

```
Fração = 298.190,68 / 859.741,08 = 0,3468
Payback descontado = 4 + 0,3468 = 4,35 anos
```

**Resultado:** Payback descontado @ 10% ≈ **4,35 anos**.

### 5.4. ROI — Passo a Passo

| Ano | OCF (R$)   | Lucro Líquido (R$) |
|----:|-----------:|-------------------:|
| 1   | 940.300    | 300.300            |
| 2   | 982.375    | 342.375            |
| 3   | 1.070.734  | 430.734            |
| 4   | 1.216.922,38 | 576.922,38       |
| 5   | 1.384.180,73 | 744.180,73       |

```
Lucro Líquido Total = 2.394.512,11
ROI = (2.394.512,11 / 3.600.000) × 100% = 66,51%
```

**Resultado:** ROI ≈ **66,51%**.

---

## 6. Resumo dos Resultados

| Cenário    | Payback Simples | Payback Descontado (10%) | ROI (5 anos) |
|------------|-----------------|--------------------------|--------------|
| **Base**   | 2,62 anos       | 3,09 anos                | 154,09%      |
| **Otimista** | 2,24 anos     | 2,60 anos                | 205,06%      |
| **Pessimista** | 3,50 anos   | 4,35 anos                | 66,51%       |

---

## 7. Interpretação

- **Payback simples:** No cenário base, o investimento é recuperado em cerca de 2,6 anos. No pessimista, em 3,5 anos.
- **Payback descontado:** Considerando o valor do dinheiro no tempo (10% a.a.), o tempo de recuperação aumenta para 3,1 anos (base) e 4,4 anos (pessimista).
- **ROI:** O retorno total sobre o investimento em 5 anos varia de 66,5% (pessimista) a 205% (otimista), indicando viabilidade em todos os cenários.

---

## 8. Observações

1. O payback descontado utiliza taxa de 10% a.a. como referência. Para análise definitiva, utilizar o WACC calculado via CAPM.
2. O ROI apresentado é o retorno total acumulado em 5 anos, não anualizado.
3. Os valores foram calculados com base nos fluxos de `dcf_scenarios.csv`; pequenas diferenças podem ocorrer por arredondamento.
