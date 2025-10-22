# Autores (Grupo)
#Adolfo Kentaro Hada** RM:556884
#Bruno Otavio Silva de Oliveira** RM:556196
#Guilherme Flores Pereira de Almeida** RM:554948
#Luiz Fernando de Aragão Souza** RM:555561
#Marcello de Freitas Moreira** RM:557531

# Cada insumo: [reagente_usado, descartavel_usado]
insumos_por_exame = [[2, 3], [3, 4], [4, 5]]  # consumo de recursos
beneficios = [30, 50, 70]  # benefício em economia/eficiência
estoque_disp = [7, 9]  # reagentes e descartáveis disponíveis

#  MEMOIZAÇÃO (Top-Down)
def get_max_beneficio_memo(beneficios, insumos_por_exame, estoque_disp):
    cache = {}
    max_idx = len(beneficios) - 1
    return rec_max(beneficios, insumos_por_exame, estoque_disp, max_idx, cache)

def rec_max(beneficios, insumos_por_exame, estoque_disp, idx_exame, cache):
    cache_key = (idx_exame, estoque_disp[0], estoque_disp[1])
    if cache_key in cache:
        return cache[cache_key]
    
    # Caso base
    if idx_exame < 0:
        return 0
    
    reag, desc = insumos_por_exame[idx_exame]
    solutions = []
    
    # continua exame
    if reag <= estoque_disp[0] and desc <= estoque_disp[1]:
        sobrou = [estoque_disp[0] - reag, estoque_disp[1] - desc]
        sol1 = beneficios[idx_exame] + rec_max(beneficios, insumos_por_exame, sobrou, idx_exame, cache)
        solutions.append(sol1)
    
    sol2 = rec_max(beneficios, insumos_por_exame, estoque_disp, idx_exame - 1, cache)
    solutions.append(sol2)
    
    cache[cache_key] = max(solutions)
    return cache[cache_key]


# ITERATIVA (Bottom-Up)
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



memo_result = get_max_beneficio_memo(beneficios, insumos_por_exame, estoque_disp)
iter_result = get_max_beneficio_iterativo(beneficios, insumos_por_exame, estoque_disp)

print("Benefício máximo (Memoização):", memo_result)
print("Benefício máximo (Iterativo):", iter_result)

assert memo_result == iter_result, "As versões não coincidem!"
print("\nAmbas as versões retornam o mesmo resultado!")

