"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd

    with open('./files/input/clusters_report.txt', 'r', encoding="utf-8") as f:
        lines = f.read().replace('%', '').splitlines()
        
    cluster_row = []
    current_entry = []

    for line in lines[4:]:
        if line.strip():
            current_entry.append(line.strip())
        else:
            if current_entry:
                cluster_row.append(" ".join(current_entry))
                current_entry = []

    cluster_data = []
    for row in cluster_row:
        columns_data = row.split()
        col0 = int(columns_data[0])
        col1 = int(columns_data[1])
        col2 = float(columns_data[2].replace(',', '.'))
        col3 = (
            " ".join(columns_data[3:])
            .replace(' ,', ',')
            .replace(', ', ', ')
            # .strip('%')
            .rstrip('.')
            .strip())
        cluster_data.append({
                    "cluster": col0,
                    "cantidad_de_palabras_clave": col1,
                    "porcentaje_de_palabras_clave": col2,
                    "principales_palabras_clave": col3,
            })
                                                    
    result = pd.DataFrame(cluster_data)

    return(result)

if __name__ == '__main__':
    print(pregunta_01())