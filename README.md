# Controle de Consumo de Insumos Hospitalares com Programação Dinâmica

## Descrição do Problema

Nas **unidades de diagnóstico**, o controle de consumo de **insumos hospitalares** — como reagentes e descartáveis — é frequentemente impreciso.  
Isso dificulta:
- o **planejamento de reposição** de materiais,  
- a **previsão de demanda**,  
- e o **controle de custos e desperdícios**.

Atualmente, os registros de consumo diário são feitos de forma manual e não permitem **analisar a eficiência do uso dos recursos**.  

Diante desse cenário, este projeto propõe uma **modelagem computacional do problema** usando **Programação Dinâmica (PD)** para encontrar **o uso ótimo do estoque de insumos** ao longo do tempo.

---

## Objetivo

Modelar o problema de consumo de insumos como um **problema de otimização**, em que o objetivo é **maximizar o benefício total (ou economia gerada)** respeitando os **limites de estoque disponíveis**.

Assim, o sistema busca:
- **melhorar a visibilidade** sobre o consumo,  
- **reduzir desperdícios**,  
- e **otimizar a tomada de decisão** sobre o uso e reposição de materiais.
---

## Estrutura do Projeto

O projeto implementa **duas versões** da solução usando **Programação Dinâmica**:

### Recursiva com Memoização (Top-Down)

A função é chamada recursivamente para avaliar **todas as combinações possíveis** de uso de insumos.  
Com o uso de **memoização**, os resultados de subproblemas já resolvidos são armazenados em cache, evitando recomputações desnecessárias.

**Vantagens:**
- Código intuitivo e próximo da formulação matemática.
- Boa para entender a lógica do problema.

**Desvantagens:**
- Pode causar stack overflow em instâncias muito grandes.
- Requer dicionário de cache.

```python
def get_max_beneficio_memo(beneficios, insumos_por_exame, estoque_disp):
    cache = {}
    max_idx = len(beneficios) - 1
    return rec_max(beneficios, insumos_por_exame, estoque_disp, max_idx, cache)
```

---

### Iterativa (Bottom-Up)

A versão iterativa cria uma **tabela de estados possíveis (`dp`)**, onde cada célula representa o **melhor benefício possível** dado um nível de estoque de reagentes e descartáveis.

**Vantagens:**
- Evita recursão profunda.
- Desempenho previsível e eficiente.
- Ideal para grandes volumes de dados.

**Desvantagens:**
- Requer mais memória (matriz bidimensional).

```python
def get_max_beneficio_iterativo(beneficios, insumos_por_exame, estoque_disp):
    max_reag, max_desc = estoque_disp
    dp = [[0] * (max_desc + 1) for _ in range(max_reag + 1)]
    
    for reag in range(max_reag + 1):
        for desc in range(max_desc + 1):
            for idx_exame in range(len(beneficios)):
                reag_usado, desc_usado = insumos_por_exame[idx_exame]
                ganho = beneficios[idx_exame]
                
                if reag >= reag_usado and desc >= desc_usado:
                    novo_benef = dp[reag - reag_usado][desc - desc_usado] + ganho
                    dp[reag][desc] = max(dp[reag][desc], novo_benef)
    
    return dp[max_reag][max_desc]
```

---

## Garantia de Consistência

Ambas as versões (Memoização e Iterativa) são testadas para garantir que retornam **exatamente o mesmo resultado** para qualquer conjunto de dados:

```python
assert memo_result == iter_result, "As versões não coincidem!"
```

Saída esperada:

```
Benefício máximo (Memoização): 140
Benefício máximo (Iterativo): 140

Ambas as versões retornam o mesmo resultado!
```

---

## Resultados e Impactos

Com o uso de **Programação Dinâmica**, a unidade de diagnóstico pode:

- Simular diferentes cenários de estoque e consumo.  
- Identificar o **uso ótimo dos insumos** sem ultrapassar limites de disponibilidade.  
- Prever **momentos ideais de reposição**, evitando falta de materiais e desperdícios.  
- Obter maior **visibilidade sobre o consumo diário**.

---

## Exemplo de Execução

```python
insumos_por_exame = [[2, 3], [3, 4], [4, 5]]
beneficios = [30, 50, 70]
estoque_disp = [7, 9]

# Saída esperada:
# Benefício máximo (Memoização): 120
# Benefício máximo (Iterativo): 120
```

---

## Conclusão

A modelagem de consumo de insumos com **Programação Dinâmica** demonstra como técnicas clássicas de otimização podem ser aplicadas para **problemas reais da área hospitalar**.  

Com base nesses algoritmos, é possível evoluir o projeto para incluir:
- previsão de consumo baseada em histórico (com aprendizado de máquina),  
- dashboards de monitoramento,  
- e integração com sistemas de estoque em tempo real.

---

### Autores (Grupo)
**Adolfo Kentaro Hada** RM:556884
**Bruno Otavio Silva de Oliveira** RM:556196
**Guilherme Flores Pereira de Almeida** RM:554948
**Luiz Fernando de Aragão Souza** RM:555561
**Marcello de Freitas Moreira** RM:557531
