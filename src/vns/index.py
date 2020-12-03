import vns
import base64
import json

def return_error(error_msg):
  return {
    'headers': { "Content-type": "application/json"},
    'statusCode': 400,
    'body': json.dumps({ 'error': error_msg }),
    'isBase64Encoded': False,
    'multiValueHeaders': {}
  }

def return_pdf(path):
  with open(path, "rb") as pdf_file:
    encoded_string = base64.b64encode(pdf_file.read())
    return {
      'headers': { "Content-type": "application/pdf", "Content-Disposition": f"attachment;filename={path.split('/')[-1]}" },
      'statusCode': 200,
      'body': encoded_string,
      'isBase64Encoded': True,
      'multiValueHeaders': {}
    }
def handler(event, context):
  print(event)
  try:
    primarylength = float(event['queryStringParameters']['primarylength'])
  except Exception as e:
    print(e)
    return return_error('Missing primarylength')

  try:
    latitude_degree = float(event['queryStringParameters']['latitude_degree'])
  except Exception as e:
    print(e)
    return return_error('Missing latitude_degree')

  try:
    half_string_len = float(event['queryStringParameters']['half_string_len'])
  except Exception as e:
    print(e)
    return return_error('Missing half_string_len')

  try:
    size = event['queryStringParameters']['size']
  except:
    print('No size given, using default A4')
    size = 'A4'

  try:
    pdf_path = vns.generate_pdf(primarylength, latitude_degree, half_string_len, size)
  except Exception as e:
    print(e)
    return return_error(f'Error generating PDF ({e})')

  return return_pdf(pdf_path)