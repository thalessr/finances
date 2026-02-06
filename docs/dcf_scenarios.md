# DCF — Cenários Otimista e Pessimista (resumo)

Arquivo gerado automaticamente com base nas premissas de `docs/problem_statement.md` e no DCF básico (`docs/dcf_basico.md`). Os CSV com fluxos estão em `docs/dcf_scenarios.csv`.

## Premissas dos cenários
- Base: preço R$ 375/un, vendas ano1 = 10.000; crescimentos: +15% / +20% / +25% / +25%; custos variáveis = 55% da receita; custos fixos = R$ 180.000; depreciação = R$ 640.000/ano; CAPEX inicial = R$ 3.600.000.
- Otimista: preço +10% (R$ 412,50/un); mesmas quantidades do cenário base; custos variáveis = 50%.
- Pessimista: preço -15% (R$ 318,75/un); crescimento reduzido (ano2 +5%, ano3 +10%, ano4 +15%, ano5 +15%); custos variáveis = 60%.

## Resultados — NPV (sem valor terminal)

NPV calculado para taxas de desconto 8%, 10% e 12%:

- Base: NPV @8% ≈ R$ 3.579.000 ; @10% ≈ R$ 2.804.000 ; @12% ≈ R$ 2.165.000
- Otimista: NPV @8% ≈ R$ 4.610.000 ; @10% ≈ R$ 4.144.000 ; @12% ≈ R$ 3.713.000
- Pessimista: NPV @8% ≈ R$ 798.600  ; @10% ≈ R$ 562.500  ; @12% ≈ R$ 343.900

Observação: todos os números são aproximados e arredondados; o CSV contém os fluxos operacionais anuais usados nos cálculos. Recomendo recalcular NPV com o WACC definitivo (CAPM) e incluir valor terminal caso o projeto tenha continuidade além do horizonte de 5 anos.

