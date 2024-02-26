import csv

def query_city_data(data, city_id):
  """
  Pesquisa por uma cidade em especifico e retorna os dados baseado na faixa etaria e sexo
    data: CSV data
    city_id:  valor CD_MUNICIPIO 

  """

  grouped_data = {}
  for row in data:
    if row["CD_MUNICIPIO"] == city_id:
      municipality = row["NM_MUNICIPIO"]
      gender = row["DS_GENERO"]
      age_range = row["DS_FAIXA_ETARIA"]
      education_level = row["DS_GRAU_ESCOLARIDADE"]
      count = 1

      if municipality not in grouped_data:
        grouped_data[municipality] = {}
      if gender not in grouped_data[municipality]:
        grouped_data[municipality][gender] = {}
      if age_range not in grouped_data[municipality][gender]:
        grouped_data[municipality][gender][age_range] = {}
      if education_level not in grouped_data[municipality][gender][age_range]:
        grouped_data[municipality][gender][age_range][education_level] = 0

      grouped_data[municipality][gender][age_range][education_level] += count

  if grouped_data:
    formatted_data = ""
    for municipality, gender_data in grouped_data.items():
      formatted_data += f"\nCidade: {municipality}\n"
      for gender, age_range_data in gender_data.items():
        formatted_data += f"\t{gender.upper()}\n"
        for age_range, education_data in age_range_data.items():
          formatted_data += f"\t\tFaixa Etária: {age_range}\n"
          for education_level, count in education_data.items():
            formatted_data += f"\t\t\tNível de Educação {education_level}: {count} pessoas\n"
    return formatted_data
  else:
    return "Cidade não encontrada."

with open("../../perfil_eleitorado_2020.csv", "r") as csvfile:
  reader = csv.DictReader(csvfile, delimiter=";")
  data = list(reader)

city_id = input("Insira o ID da cidade (CD_MUNICIPIO): ")

# Pesquisa os dados daquela cidade em especifico
city_data = query_city_data(data, city_id)

print(city_data)




'''

VERSÃO QUE TRÁS TODOS DADOS DE UMA VEZ

import csv

with open("../eleitorado/perfil_eleitorado_2020/perfil_eleitorado_2020.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";") 
    data = list(reader)

grouped_data = {}
for row in data:
    municipality = row["NM_MUNICIPIO"]
    gender = row["DS_GENERO"]
    age_range = row["DS_FAIXA_ETARIA"]
    education_level = row["DS_GRAU_ESCOLARIDADE"]
    count = 1  
    if municipality not in grouped_data:
        grouped_data[municipality] = {}
    if gender not in grouped_data[municipality]:
        grouped_data[municipality][gender] = {}
    if age_range not in grouped_data[municipality][gender]:
        grouped_data[municipality][gender][age_range] = {}
    if education_level not in grouped_data[municipality][gender][age_range]:
        grouped_data[municipality][gender][age_range][education_level] = 0
    grouped_data[municipality][gender][age_range][education_level] += count

# Process and format the data into the desired structure
formatted_data = {}
for municipality, gender_data in grouped_data.items():
    formatted_data[municipality] = {}
    for gender, age_range_data in gender_data.items():
        formatted_data[municipality][gender] = {"ageRange": {}}
        for age_range, education_data in age_range_data.items():
            formatted_data[municipality][gender]["ageRange"][age_range] = {}
            for education_level, count in education_data.items():
                formatted_data[municipality][gender]["ageRange"][age_range][education_level] = count

print(formatted_data)  '''
