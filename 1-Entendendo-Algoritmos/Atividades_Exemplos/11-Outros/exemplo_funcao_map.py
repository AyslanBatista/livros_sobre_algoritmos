
arr1 = [1,2,3,4,5]
arr2 = map(lambda x:2 *x, arr1)
# Cada elemento do arr1 foi dobrado! Dobrar um elemento é uma bem rápida

##########################################################
arr1 = # uma lista de URLs
arr2 = map(download_page, arr1)
# Temos uma lista de URLs e você deseja baixar cada pagina e armazenar
# seu conteúdo no arr2, isso pode levar alguns segundos para cada URls
# se você tiver 1.000 Urls, isto levará algumas horas
