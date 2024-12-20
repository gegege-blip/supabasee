from supabase import Client
from connect_supabase import get_connect_supabase


#tive  que pesquisar boa parte dos códigos

supabase = get_connect_supabase()

response = (
    supabase.table("produtos")
    .insert({"descricao": "Escova de Dente", "preco": 10.00, "quantidade": "32"})
    .execute()
)
response = (
    supabase.table("produtos")
    .insert({"descricao": "Pasta de Dente", "preco": 5.00, "quantidade": "73"})
    .execute()
)
response = (
    supabase.table("produtos")
    .insert({"descricao": "Escova de Cabelo", "preco": 22.00, "quantidade": "51"})
    .execute()
)
response = (
    supabase.table("produtos")
    .insert({"descricao": "Pente de Madeira", "preco": 15.00, "quantidade": 30})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Shampoo Anticaspa", "preco": 25.00, "quantidade": 20})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Condicionador Hidratante", "preco": 28.50, "quantidade": 25})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Gel Fixador", "preco": 12.90, "quantidade": 40})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Creme para Pentear", "preco": 19.99, "quantidade": 18})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Máscara Capilar", "preco": 35.00, "quantidade": 15})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Toalha de Microfibra", "preco": 10.00, "quantidade": 50})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Escova Alisadora", "preco": 55.00, "quantidade": 10})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Secador de Cabelo", "preco": 150.00, "quantidade": 5})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Prancha de Cabelo", "preco": 120.00, "quantidade": 8})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Cera Modeladora", "preco": 22.50, "quantidade": 33})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Pomada Capilar", "preco": 18.90, "quantidade": 27})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Óleo de Argan", "preco": 45.00, "quantidade": 12})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Elástico para Cabelo", "preco": 5.00, "quantidade": 100})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Piranha de Cabelo", "preco": 8.00, "quantidade": 75})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Lâmina de Barbear", "preco": 3.50, "quantidade": 200})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Aparador de Pelos", "preco": 85.00, "quantidade": 7})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Corta Unhas", "preco": 6.50, "quantidade": 45})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Lixa de Unha", "preco": 2.00, "quantidade": 150})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Esmalte para Unhas", "preco": 9.90, "quantidade": 60})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Removedor de Esmalte", "preco": 11.00, "quantidade": 40})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Kit de Maquiagem", "preco": 120.00, "quantidade": 4})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Espelho de Maquiagem", "preco": 35.00, "quantidade": 12})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Algodão Quadrado", "preco": 7.50, "quantidade": 90})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Pinça de Sobrancelha", "preco": 15.00, "quantidade": 28})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Protetor Térmico", "preco": 32.00, "quantidade": 20})
    .execute()
)


response = (
    supabase.table("produtos")
    .insert({"descricao": "Spray Fixador", "preco": 18.00, "quantidade": 35})
    .execute()
)

response = (
    supabase.table("produtos")
    .delete()
    .lt("preco", 10)
    .execute()
)

response = (
    supabase.table("produtos")
    .select("*")
    .gt("quantidade", 100)
    .execute()
)
print(response.data)


response = (
    supabase.table("produtos")
    .update({"quantidade": supabase.fn.increment(10)})
    .lt("preco", 50)
    .execute()
)
print(response)
