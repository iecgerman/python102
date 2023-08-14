import utils
import read_csv
import charts

def run():
  dataPcymac = read_csv.read_csv('./proyecto/dataPcymac.csv')
  dataPcymac = list(filter(lambda item: item['ProductoStock'] == '1', dataPcymac))
  
  productos = list(map(lambda x: x['ProductoNombre'], dataPcymac))
  stocks = list(map(lambda x: x['ProductoStock'], dataPcymac))
  charts.generate_pie_chart(productos, stocks)
  
  
  """producto = input('Teclea o escanea codigo de producto => ')

  result = utils.precio_por_producto(dataPcymac, producto)

  if len(result) > 0:
    producto = result[0]
    labels, values = utils.obtener_productos(producto)
    charts.generate_bar_chart"""

if __name__ == '__main__':
  run()