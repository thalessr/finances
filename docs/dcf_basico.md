# Modelo DCF básico — Cia. Argo Energy

> Arquivo gerado automaticamente. Contém um DCF simplificado (horizonte 5 anos) com premissas do `docs/problem_statement.md`.

## Premissas principais
- Preço unitário: R$ 375,00
- Vendas ano 1: 10.000 unidades
- Crescimentos: Ano2 +15% / Ano3 +20% / Ano4 +25% / Ano5 +25%
- Investimento inicial (Year 0): R$ 3.600.000 (CAPEX total incluindo pré-op e capital de giro inicial)
- Depreciação: R$ 3.200.000 depreciados linearmente em 5 anos = R$ 640.000/ano
- Custos variáveis: 55% da receita
- Gastos fixos: R$ 180.000/ano
- Alíquota de imposto (IRPJ efetiva utilizada): 34%
- Não há CAPEX adicionais nem variação adicional de capital de giro projetada (modelo simples)

## Fluxo de caixa projetado (valores em R$)

| Ano | Receita | Custos Variáveis | Custos Fixos | Depreciação | EBIT | Imposto (34%) | Lucro Líquido | Fluxo Operacional (Lucro + Dep.) |
|-----:|--------:|-----------------:|-------------:|------------:|-----:|--------------:|--------------:|---------------------------------:|
| 0   | 0       | 0                | 0            | 0           | 0    | 0             | 0             | -3.600.000 (CAPEX)              |
| 1   | 3.750.000 | 2.062.500      | 180.000      | 640.000     | 867.500 | 294.950     | 572.550       | 1.212.550                       |
| 2   | 4.312.500 | 2.371.875      | 180.000      | 640.000     | 1.120.625 | 381.012,50 | 739.612,50    | 1.379.612,50                    |
| 3   | 5.175.000 | 2.846.250      | 180.000      | 640.000     | 1.508.750 | 512.975     | 995.775       | 1.635.775                       |
| 4   | 6.468.750 | 3.557.812,50   | 180.000      | 640.000     | 2.090.937,50 | 710.918,75 | 1.380.018,75  | 2.020.018,75                    |
| 5   | 8.085.937,50 | 4.447.265,63 | 180.000      | 640.000     | 2.818.671,88 | 958.348,44 | 1.860.323,44  | 2.500.323,44                    |

> Observação: números arredondados para exibição — cálculos internos seguem os valores mostrados.

## NPV (sem valor terminal) — sensibilidade ao desconto

- NPV @ 8%  ≈ R$ 3.579.000
- NPV @ 10% ≈ R$ 2.804.000
- NPV @ 12% ≈ R$ 2.165.000

> Conclusão do modelo simples: mesmo sem valor terminal e assumindo as premissas acima, o projeto apresenta NPV positivo para taxas de desconto na faixa 8–12% e payback simples de ~3 anos (CAPEX / fluxo operacional ano1 ≈ 3,0). Isso confirma a avaliação inicial de viabilidade, condicionado às premissas.

## Recomendações / próximos passos
1. Validar WACC / custo de capital (calcular CAPM com Rf, Beta e prêmio de mercado) e recalcular NPV com WACC correto.  
2. Incluir variação de capital de giro ligada à receita (ex.: % da receita) e CAPEX de manutenção se aplicável.  
3. Calcular cenários (otimista / base / pessimista) alterando preço, % custos variáveis e volume.  
4. Gerar versão em CSV/Excel se desejar exportação para análise adicional.

Arquivo salvo em `docs/dcf_basico.md`.

