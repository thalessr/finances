# Indicadores Financeiros e Fórmulas para AVP — Cia. Argo Energy

## 1. Introdução

Este documento identifica todos os indicadores financeiros e fórmulas necessários para realizar a **Análise de Viabilidade do Projeto (AVP)** da Cia. Argo Energy, com base nas premissas definidas no enunciado do problema e nos conceitos teóricos de finanças corporativas.

---

## 2. Estruturação do Fluxo de Caixa

### 2.1. Componentes do Fluxo de Caixa

O fluxo de caixa é a ferramenta central para a AVP e deve incluir:

**Ano 0 (20X0) - Investimento Inicial:**
- CAPEX Total: R$ 3.600.000,00
  - Investimento Fixo: R$ 3.200.000,00
  - Investimento Pré-Operacional: R$ 220.000,00
  - Capital de Giro Inicial: R$ 180.000,00

**Anos 1 a 5 (20X1 a 20X5) - Operações:**

#### Receitas Brutas
```
Receita = Preço Unitário × Quantidade Vendida
```

Onde:
- Preço Unitário: R$ 375,00/painel
- Vendas Ano 1: 10.000 unidades
- Crescimento:
  - Ano 2: 15% → 11.500 unidades
  - Ano 3: 20% → 13.800 unidades
  - Ano 4: 25% → 17.250 unidades
  - Ano 5: 25% → 21.562 unidades

#### Custos e Despesas

**Custos Variáveis:**
```
CV = 55% × Receita Bruta
```

**Gastos Fixos:**
```
GF = R$ 180.000,00 (constante anual)
```

**Depreciação:**
```
Depreciação Anual = Investimento Fixo / Vida Útil
Depreciação Anual = R$ 3.200.000,00 / 5 anos = R$ 640.000,00/ano
```

### 2.2. Cálculo do LAIR (Lucro Antes do IR)

```
LAIR = Receita Bruta - Custos Variáveis - Gastos Fixos - Depreciação
```

### 2.3. Cálculo do Imposto de Renda

```
IR = LAIR × 34%
```

### 2.4. Cálculo do Lucro Líquido

```
Lucro Líquido = LAIR - IR
```

### 2.5. Fluxo de Caixa Operacional

```
FCO = Lucro Líquido + Depreciação
```

**Observação:** A depreciação é somada de volta porque é uma despesa não desembolsável.

### 2.6. Distribuição de Dividendos

```
Dividendos = Lucro Líquido × 25%
Retenção de Lucros = Lucro Líquido × 75%
```

### 2.7. Fluxo de Caixa Livre do Acionista (FCLA)

```
FCLA = FCO - Dividendos (opcional, depende da perspectiva)
```

ou

```
FCLA = Lucro Líquido + Depreciação
```

---

## 3. Custo de Capital

### 3.1. Modelo CAPM (Capital Asset Pricing Model)

O custo de capital próprio será calculado usando o CAPM:

```
Ke = Rf + β × (Rm - Rf)
```

Onde:
- **Ke** = Custo de capital próprio
- **Rf** = Taxa livre de risco (Risk-free rate)
- **β** = Beta do setor de energia
- **Rm** = Retorno esperado do mercado (Ibovespa)
- **(Rm - Rf)** = Prêmio de risco de mercado

#### Fontes de Dados (conforme referências fornecidas):

| Variável | Fonte Sugerida |
|----------|----------------|
| **Rf** | T-Bond (EUA) ou Títulos do Tesouro Brasileiro (Selic, Tesouro Direto) via Banco Central do Brasil |
| **β setor** | Betas by Sector (Damodaran - NYU Stern) ou empresas similares na B3 |
| **Rm** | Ibovespa - B3 / Historical Returns (Damodaran) |
| **Inflação** | IBGE / Dados Mundiais (Inflação EUA) |

### 3.2. Taxa Livre de Risco (Rf)

**Opções:**
1. **T-Bond (Taxa de Títulos do Tesouro Americano de 10 anos)** - referência internacional
2. **Taxa Selic** - referência brasileira
3. **Tesouro IPCA+ 2035** - título brasileiro de longo prazo

**Fonte:** Banco Central do Brasil, T-Bond (Trading Economics)

### 3.3. Beta (β) do Setor

O Beta mede a sensibilidade do retorno de uma ação em relação ao retorno do mercado.

**Identificação:**
- Buscar Beta do setor de "Green & Renewable Energy" ou "Solar Energy"
- Alternativamente, usar empresas brasileiras do setor de energia na B3

**Fonte:** Damodaran (Betas by Sector), Yahoo Finance, Fundamentus

### 3.4. Retorno do Mercado (Rm)

**Cálculo:**
```
Rm = Média histórica dos retornos do Ibovespa
```

**Período sugerido:** Últimos 5-10 anos

**Fonte:** B3, Historical Returns (Damodaran), Yahoo Finance

### 3.5. Ajuste para Risco Brasil (Opcional)

Para projetos no Brasil, pode-se adicionar o Risco País:

```
Ke = Rf + β × (Rm - Rf) + Risco País
```

**Fonte:** EMBI+ Brasil (J.P. Morgan) via Ipeadata ou Banco Central

---

## 4. Custo Médio Ponderado de Capital (WACC)

Como o projeto será financiado 100% com **recursos próprios**, o WACC será igual ao custo de capital próprio:

```
WACC = Ke
```

**Caso houvesse capital de terceiros:**

```
WACC = (E/V) × Ke + (D/V) × Kd × (1 - T)
```

Onde:
- **E** = Valor do capital próprio (equity)
- **D** = Valor da dívida (debt)
- **V** = E + D (valor total da empresa)
- **Ke** = Custo do capital próprio (via CAPM)
- **Kd** = Custo do capital de terceiros (taxa de juros da dívida)
- **T** = Alíquota de imposto (34%)

---

## 5. Métodos de Avaliação de Viabilidade

### 5.1. Valor Presente Líquido (VPL/NPV)

O VPL é o principal indicador de viabilidade econômica:

```
VPL = Σ [FCt / (1 + WACC)^t] - Investimento Inicial
```

Onde:
- **FCt** = Fluxo de caixa no período t
- **WACC** = Taxa de desconto (custo de capital)
- **t** = Período (ano)

**Critério de decisão:**
- **VPL > 0**: Projeto viável (aceitar)
- **VPL = 0**: Indiferente (retorno igual ao custo de capital)
- **VPL < 0**: Projeto inviável (rejeitar)

**Interpretação:** O VPL positivo representa o valor agregado ao projeto acima do retorno exigido pelos acionistas.

### 5.2. Taxa Interna de Retorno (TIR/IRR)

A TIR é a taxa de desconto que torna o VPL igual a zero:

```
0 = Σ [FCt / (1 + TIR)^t] - Investimento Inicial
```

**Critério de decisão:**
- **TIR > WACC**: Projeto viável (aceitar)
- **TIR = WACC**: Indiferente
- **TIR < WACC**: Projeto inviável (rejeitar)

**Interpretação:** A TIR representa a taxa de retorno anual esperada do projeto.

### 5.3. Período de Payback Descontado

Tempo necessário para recuperar o investimento inicial considerando o valor do dinheiro no tempo:

```
Payback Descontado = n anos (quando Σ VPL acumulado = 0)
```

**Cálculo:**
1. Descontar cada fluxo de caixa à taxa WACC
2. Acumular os fluxos descontados
3. Identificar em que período o acumulado supera o investimento inicial

### 5.4. Índice de Lucratividade (IL)

```
IL = VP dos Fluxos de Caixa Futuros / Investimento Inicial
```

Ou:

```
IL = (VPL + Investimento Inicial) / Investimento Inicial
```

**Critério de decisão:**
- **IL > 1**: Projeto viável
- **IL = 1**: Indiferente
- **IL < 1**: Projeto inviável

**Interpretação:** Mostra quanto de valor presente é gerado para cada R$ 1,00 investido.

### 5.5. Taxa Interna de Retorno Modificada (TIRM)

Para casos onde há múltiplas mudanças de sinal no fluxo de caixa:

**Passos:**
1. Calcular o valor futuro (FV) de todas as entradas de caixa positivas à taxa WACC
2. Calcular o valor presente (PV) de todas as saídas de caixa à taxa WACC
3. Calcular a TIRM:

```
TIRM = [(FV / PV)^(1/n)] - 1
```

---

## 6. Análise de Sensibilidade

### 6.1. Cenários a Considerar

**Cenário Base:**
- Premissas conforme definidas no problema

**Cenário Otimista:**
- Aumento de demanda (exemplo: +10% nas vendas)
- Redução de custos (exemplo: -5% nos custos variáveis)
- Melhoria de produtividade

**Cenário Pessimista:**
- Redução de demanda (exemplo: -10% nas vendas)
- Aumento de custos (exemplo: +10% nos custos variáveis)
- Aumento de tributação
- Variação cambial adversa

### 6.2. Variáveis a Testar

| Variável | Impacto no VPL |
|----------|----------------|
| Preço de venda | Alterar entre R$ 300 - R$ 450 |
| Volume de vendas | Testar crescimento de 10% a 30% |
| Custos variáveis | Testar entre 45% e 65% da receita |
| Gastos fixos | Testar variação de ±20% |
| Taxa de desconto (WACC) | Testar diferentes valores de Ke |

### 6.3. Análise de Break-even

**Ponto de Equilíbrio Operacional:**

```
Qe = Gastos Fixos / (Preço - Custo Variável Unitário)
```

Onde:
```
CVu = (Custos Variáveis % × Preço) = (0,55 × R$ 375) = R$ 206,25
Qe = R$ 180.000 / (R$ 375 - R$ 206,25) = R$ 180.000 / R$ 168,75 ≈ 1.067 unidades/ano
```

---

## 7. Indicadores Complementares

### 7.1. Margem de Contribuição

```
MC unitária = Preço - Custo Variável Unitário
MC% = (Preço - CVu) / Preço × 100%
```

### 7.2. ROI (Return on Investment)

```
ROI = (Lucro Líquido Total / Investimento Inicial) × 100%
```

### 7.3. Rentabilidade Média

```
Rentabilidade = Lucro Líquido Médio / Investimento Inicial × 100%
```

---

## 8. Estrutura de Análise Recomendada

### Ordem de Execução:

1. **Coleta de Dados de Mercado**
   - Taxa livre de risco (Rf)
   - Beta do setor (β)
   - Retorno do mercado (Rm)

2. **Cálculo do Custo de Capital**
   - CAPM → Ke
   - WACC = Ke (100% capital próprio)

3. **Projeção do Fluxo de Caixa**
   - Receitas (anos 1-5)
   - Custos e despesas
   - LAIR e IR
   - Fluxo de caixa livre

4. **Avaliação de Viabilidade**
   - VPL
   - TIR
   - Payback descontado
   - Índice de Lucratividade

5. **Análise de Sensibilidade**
   - Cenários otimista, base e pessimista
   - Variação de variáveis críticas

6. **Recomendação Final**
   - Parecer sobre viabilidade
   - Identificação de riscos
   - Sugestões de mitigação

---

## 9. Fórmulas Resumidas

### Fluxo de Caixa
```
FC₀ = -R$ 3.600.000,00

Para t = 1 a 5:
Receita = Preço × Quantidade
CV = 55% × Receita
LAIR = Receita - CV - GF - Depreciação
IR = LAIR × 34%
LL = LAIR - IR
FCO = LL + Depreciação
```

### Custo de Capital
```
Ke = Rf + β × (Rm - Rf)
WACC = Ke
```

### Indicadores de Viabilidade
```
VPL = Σ[FCt / (1+WACC)^t] - Investimento

TIR: 0 = Σ[FCt / (1+TIR)^t] - Investimento

IL = VP(Fluxos Futuros) / Investimento
```

---

## 10. Checklist de Dados Necessários

### Dados do Projeto (fornecidos):
- ✅ Investimento total: R$ 3.600.000,00
- ✅ Preço de venda: R$ 375,00/unidade
- ✅ Vendas Ano 1: 10.000 unidades
- ✅ Crescimento de vendas: Anos 2-5
- ✅ Custos variáveis: 55% da receita
- ✅ Gastos fixos: R$ 180.000,00/ano
- ✅ Vida útil: 5 anos
- ✅ Alíquota IR: 34%
- ✅ Distribuição dividendos: 25%

### Dados de Mercado (a pesquisar):
- ⬜ Taxa livre de risco (Rf)
- ⬜ Beta do setor energia solar (β)
- ⬜ Retorno esperado do Ibovespa (Rm)
- ⬜ Inflação (opcional para ajustes)
- ⬜ Risco país (opcional)

### Fontes de Consulta:
- Banco Central do Brasil: https://www.bcb.gov.br/
- B3: http://www.b3.com.br/pt_br/
- Yahoo Finance: https://finance.yahoo.com
- Damodaran (NYU Stern): https://pages.stern.nyu.edu/~adamodar/
- Fundamentus: https://www.fundamentus.com.br/
- Ipeadata: http://www.ipeadata.gov.br/

---

## 11. Observações Importantes

1. **Horizonte de Análise:** 5 anos (20X1 a 20X5), com investimento em 20X0

2. **Valor Residual:** O problema não menciona valor residual ao final do projeto. Assumir que não há valor de revenda ou considerar como análise adicional.

3. **Capital de Giro:** O capital de giro inicial (R$ 180.000) é investido no Ano 0 e, teoricamente, deve ser recuperado ao final do projeto (Ano 5).

4. **Depreciação:** A depreciação é 100% linear em 5 anos, afetando o LAIR para cálculo do IR, mas é adicionada de volta no FCO por ser não desembolsável.

5. **Financiamento:** 100% recursos próprios → sem custo de capital de terceiros → WACC = Ke

6. **Dividendos:** Distribuição de até 25% do lucro líquido. Na modelagem do FCL para o projeto, os dividendos podem ou não ser deduzidos, dependendo da perspectiva (projeto vs. acionista).

---

## 12. Conclusão

Este documento estrutura todos os indicadores, fórmulas e premissas necessários para realizar a AVP da Cia. Argo Energy. O próximo passo é coletar os dados de mercado nas fontes indicadas e construir o modelo de avaliação no Excel ou em Python, calculando os indicadores de viabilidade e realizando a análise de sensibilidade.

A decisão de viabilidade será baseada principalmente no **VPL** e na **TIR**, complementada pela análise de cenários e identificação de riscos.
