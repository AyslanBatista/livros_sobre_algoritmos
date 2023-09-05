"""
- Uma unisão significa "combine os dois conjustos".
- Uma intersecção significa "encontre os itens que aparecem nos dois conjuntos"
- Uma diferença "subtraia os itens de um conjunto dos itens do outro conjunto"        
    """

frutas = set(["abacate", "tomate", "banana"])
vegetais = set(["beterraba", "cenoura", "tomate"])

print(frutas | vegetais)  # isso é uma união
# {'banana', 'cenoura', 'beterraba', 'tomate', 'abacate'}

print(frutas & vegetais)  # Isso é uma intersecção
# {'tomate'}

print(frutas - vegetais)  # Isso é uma diferença
# {'abacate', 'banana'}
